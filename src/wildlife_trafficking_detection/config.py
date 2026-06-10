from dataclasses import dataclass
from pathlib import Path


@dataclass
class DataConfig:
    raw_data_path: Path = Path("data/raw/labeled_may_7_2024.parquet")
    csv_data_path: Path = Path("data/raw/animal_products.csv")
    image_root: Path = Path("data/external/images")
    text_column: str = "text"
    title_column: str = "title"
    description_column: str = "description"
    label_column: str = "predictedlabel"
    image_column: str = "imagepath"


@dataclass
class TrainingConfig:
    batch_size: int = 16
    epochs: int = 5
    learning_rate: float = 1e-4
    metadata_dim: int = 64
    image_embedding_dim: int = 128
    text_embedding_dim: int = 128
    hidden_dim: int = 128
    num_classes: int = 2