from __future__ import annotations

import torch
import torch.nn as nn


class MultiHeadCrossAttention(nn.Module):
    def __init__(self, embed_dim: int, num_heads: int = 4, dropout: float = 0.1):
        super().__init__()
        self.attention = nn.MultiheadAttention(embed_dim, num_heads, dropout=dropout, batch_first=True)
        self.norm = nn.LayerNorm(embed_dim)

    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor) -> torch.Tensor:
        attended, _ = self.attention(query, key, value)
        return self.norm(attended + query)


class MultiModalClassifier(nn.Module):
    def __init__(self, vocab_size: int = 30522, metadata_dim: int = 32, hidden_dim: int = 128, num_classes: int = 2):
        super().__init__()
        self.text_embedding = nn.Embedding(vocab_size, hidden_dim)

        self.image_encoder = nn.Sequential(
            nn.Conv2d(3, 16, kernel_size=3, stride=2, padding=1),
            nn.ReLU(),
            nn.Conv2d(16, 32, kernel_size=3, stride=2, padding=1),
            nn.ReLU(),
            nn.AdaptiveAvgPool2d((1, 1)),
            nn.Flatten(),
            nn.Linear(32, hidden_dim),
        )

        self.metadata_encoder = nn.Sequential(
            nn.Linear(metadata_dim, hidden_dim),
            nn.ReLU(),
        )

        self.cross_attention = MultiHeadCrossAttention(embed_dim=hidden_dim)
        self.classifier = nn.Sequential(
            nn.Linear(hidden_dim * 3, hidden_dim),
            nn.ReLU(),
            nn.Dropout(0.1),
            nn.Linear(hidden_dim, num_classes),
        )

    def forward(self, input_ids: torch.Tensor, attention_mask: torch.Tensor, image: torch.Tensor, metadata: torch.Tensor) -> torch.Tensor:
        text_emb = self.text_embedding(input_ids)
        text_feat = text_emb.mean(dim=1)
        image_feat = self.image_encoder(image)
        metadata_feat = self.metadata_encoder(metadata)

        attn_out = self.cross_attention(
            text_feat.unsqueeze(1),
            image_feat.unsqueeze(1),
            image_feat.unsqueeze(1),
        ).squeeze(1)

        fused = torch.cat([attn_out, image_feat, metadata_feat], dim=1)
        return self.classifier(fused)