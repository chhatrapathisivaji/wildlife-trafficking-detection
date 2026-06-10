from dataclasses import dataclass
from pathlib import Path


@dataclass
class ProjectConfig:
    project_name: str = "wildlife-trafficking-detection"
    data_dir: Path = Path("data")
    models_dir: Path = Path("models")
    reports_dir: Path = Path("reports")
