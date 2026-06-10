from __future__ import annotations

import torch
from torch.utils.data import DataLoader


@torch.no_grad()
def evaluate_model(model, loader: DataLoader, criterion=None, device: str = "cpu"):
    model.eval()
    total_loss = 0.0
    total_correct = 0
    total_examples = 0
    predictions = []
    labels_all = []

    for batch in loader:
        input_ids = batch["input_ids"].to(device)
        attention_mask = batch["attention_mask"].to(device)
        image = batch["image"].to(device)
        metadata = batch["metadata"].to(device)
        labels = batch["label"].to(device)

        logits = model(input_ids=input_ids, attention_mask=attention_mask, image=image, metadata=metadata)
        if criterion is not None:
            loss = criterion(logits, labels)
            total_loss += loss.item() * labels.size(0)

        preds = logits.argmax(dim=1)
        total_correct += (preds == labels).sum().item()
        total_examples += labels.size(0)
        predictions.extend(preds.cpu().tolist())
        labels_all.extend(labels.cpu().tolist())

    return {
        "loss": total_loss / max(total_examples, 1) if criterion is not None else None,
        "accuracy": total_correct / max(total_examples, 1),
        "predictions": predictions,
        "labels": labels_all,
    }