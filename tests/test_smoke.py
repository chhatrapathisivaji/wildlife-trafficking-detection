import torch

from src.wildlife_trafficking_detection.models import MultiModalClassifier


def test_model_forward_pass():
    model = MultiModalClassifier(metadata_dim=8)
    batch_size = 2
    input_ids = torch.zeros((batch_size, 16), dtype=torch.long)
    attention_mask = torch.ones((batch_size, 16), dtype=torch.long)
    image = torch.randn((batch_size, 3, 224, 224))
    metadata = torch.randn((batch_size, 8))

    logits = model(input_ids=input_ids, attention_mask=attention_mask, image=image, metadata=metadata)
    assert logits.shape == (batch_size, 2)