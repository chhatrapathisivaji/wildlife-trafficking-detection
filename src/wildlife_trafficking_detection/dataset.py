from __future__ import annotations

from pathlib import Path
from typing import Callable, Optional

import numpy as np
import pandas as pd
import torch
from PIL import Image
from torch.utils.data import Dataset

from .metadata_features import build_metadata_vector


class WildlifeAdsDataset(Dataset):
    def __init__(
        self,
        df: pd.DataFrame,
        image_root: str | Path,
        country_vocab: list[str],
        seller_vocab: list[str],
        tokenizer: Optional[Callable] = None,
        image_transform: Optional[Callable] = None,
        max_length: int = 128,
        label_col: str = "predictedlabel",
    ):
        self.df = df.reset_index(drop=True)
        self.image_root = Path(image_root)
        self.country_vocab = country_vocab
        self.seller_vocab = seller_vocab
        self.tokenizer = tokenizer
        self.image_transform = image_transform
        self.max_length = max_length
        self.label_col = label_col

    def __len__(self) -> int:
        return len(self.df)

    def _load_image(self, image_path: Optional[str]):
        if not image_path:
            image = Image.fromarray(np.zeros((224, 224, 3), dtype=np.uint8))
        else:
            full_path = self.image_root / image_path
            if full_path.exists():
                image = Image.open(full_path).convert("RGB")
            else:
                image = Image.fromarray(np.zeros((224, 224, 3), dtype=np.uint8))
        if self.image_transform is not None:
            return self.image_transform(image)
        return torch.tensor(np.asarray(image)).permute(2, 0, 1).float() / 255.0

    def __getitem__(self, idx: int):
        row = self.df.iloc[idx]
        text = " ".join(
            [
                str(row.get("title", "") or ""),
                str(row.get("text", "") or ""),
                str(row.get("description", "") or ""),
            ]
        ).strip()

        if self.tokenizer is not None:
            encoded = self.tokenizer(
                text,
                truncation=True,
                padding="max_length",
                max_length=self.max_length,
                return_tensors="pt",
            )
            input_ids = encoded["input_ids"].squeeze(0)
            attention_mask = encoded["attention_mask"].squeeze(0)
        else:
            input_ids = torch.zeros(self.max_length, dtype=torch.long)
            attention_mask = torch.zeros(self.max_length, dtype=torch.long)

        metadata = torch.tensor(
            build_metadata_vector(row, self.country_vocab, self.seller_vocab),
            dtype=torch.float,
        )
        image_tensor = self._load_image(row.get("imagepath"))
        label = int(row.get(self.label_col, 0))

        return {
            "input_ids": input_ids,
            "attention_mask": attention_mask,
            "image": image_tensor,
            "metadata": metadata,
            "label": torch.tensor(label, dtype=torch.long),
        }