#!/usr/bin/env bash
set -euo pipefail

mkdir -p data notebooks src/wildlife_trafficking_detection tests models reports assets

cat > README.md <<'EOT'
# Wildlife Trafficking Detection

A collaborative machine learning project focused on wildlife-related image understanding and detection workflows, including data preparation, experimentation, model training, and evaluation.

## Overview

This repository presents a structured, portfolio-ready version of work related to a collaborative wildlife trafficking detection project. It is organized to highlight reproducible experimentation, clear engineering practices, and professional documentation.

## My Contribution

I contributed to the collaborative development of this project through experimentation, model development, and implementation support. This repository is intended as a clean public-facing representation of the project while avoiding disclosure of any sensitive or private details.

## Objectives

- Organize the project into a professional and reproducible repository structure.
- Support experimentation for wildlife-related computer vision tasks.
- Provide a clean training and evaluation workflow.
- Document setup, usage, and project components clearly.

## Repository Structure

```text
src/wildlife_trafficking_detection/   Core training and evaluation code
notebooks/                            Exploratory analysis and experiments
data/                                 Dataset instructions and placeholders
models/                               Saved model documentation or artifacts
reports/                              Results, notes, and experiment summaries
assets/                               Images and visuals for documentation
tests/                                Basic validation and smoke tests
```

## Setup

### Option 1: pip

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Option 2: conda

```bash
conda env create -f environment.yml
conda activate wildlife-trafficking-detection
```

## Usage

Train a baseline model:

```bash
python -m src.wildlife_trafficking_detection.train
```

Run evaluation:

```bash
python -m src.wildlife_trafficking_detection.evaluate
```

## Data

The dataset is not included in this repository. Add dataset details, access instructions, expected folder layout, and preprocessing requirements in `data/README.md`.

## Results

Results and experiment summaries will be added as the project documentation is expanded.

## Notes

This repository is a portfolio-quality organization of collaborative project work. Sensitive or private project details should remain excluded as needed.

## License

This project uses the MIT License.
EOT

cat > .gitignore <<'EOT'
__pycache__/
*.py[cod]
*.so
.venv/
venv/
env/
ENV/
.ipynb_checkpoints/
.pytest_cache/
.mypy_cache/
coverage/
htmlcov/
.dist/
build/
*.egg-info/
.DS_Store
.env
*.log
data/raw/
data/processed/
models/*.pt
models/*.pth
models/*.ckpt
EOT

cat > LICENSE <<'EOT'
MIT License

Copyright (c) 2026 Chhatrapathi Sivaji Lakkimsetty

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
EOT

cat > requirements.txt <<'EOT'
numpy
pandas
scikit-learn
torch
torchvision
matplotlib
jupyter
pytest
EOT

cat > environment.yml <<'EOT'
name: wildlife-trafficking-detection
channels:
  - conda-forge
  - defaults
dependencies:
  - python=3.11
  - pip
  - numpy
  - pandas
  - scikit-learn
  - matplotlib
  - jupyter
  - pytest
  - pip:
      - torch
      - torchvision
EOT

cat > pyproject.toml <<'EOT'
[build-system]
requires = ["setuptools>=68", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "wildlife-trafficking-detection"
version = "0.1.0"
description = "Portfolio-ready collaborative ML project for wildlife trafficking detection workflows"
readme = "README.md"
requires-python = ">=3.11"
authors = [
  {name = "Chhatrapathi Sivaji Lakkimsetty"}
]
dependencies = [
  "numpy",
  "pandas",
  "scikit-learn",
  "torch",
  "torchvision",
  "matplotlib"
]

[tool.pytest.ini_options]
testpaths = ["tests"]
EOT

cat > data/README.md <<'EOT'
# Data

This directory does not contain raw project data.

Document here:
- dataset source,
- access instructions,
- expected folder layout,
- preprocessing steps,
- privacy, ethics, or licensing constraints.
EOT

cat > models/README.md <<'EOT'
# Models

Use this directory to document trained models, checkpoints, and model selection notes.

Avoid committing large binary checkpoint files directly unless necessary.
EOT

cat > reports/README.md <<'EOT'
# Reports

Use this directory for experiment summaries, evaluation notes, result snapshots, and reproducibility notes.
EOT

cat > assets/README.md <<'EOT'
# Assets

Store documentation visuals here, such as architecture diagrams, sample outputs, or project overview images.
EOT

cat > src/wildlife_trafficking_detection/__init__.py <<'EOT'
__all__ = []
EOT

cat > src/wildlife_trafficking_detection/config.py <<'EOT'
from dataclasses import dataclass
from pathlib import Path


@dataclass
class ProjectConfig:
    project_name: str = "wildlife-trafficking-detection"
    data_dir: Path = Path("data")
    models_dir: Path = Path("models")
    reports_dir: Path = Path("reports")
EOT

cat > src/wildlife_trafficking_detection/data.py <<'EOT'
from pathlib import Path


def get_data_directory() -> Path:
    return Path("data")
EOT

cat > src/wildlife_trafficking_detection/utils.py <<'EOT'
def format_experiment_name(name: str) -> str:
    return name.strip().lower().replace(" ", "-")
EOT

cat > src/wildlife_trafficking_detection/train.py <<'EOT'
def main() -> None:
    print("Training entrypoint for wildlife trafficking detection")


if __name__ == "__main__":
    main()
EOT

cat > src/wildlife_trafficking_detection/evaluate.py <<'EOT'
def main() -> None:
    print("Evaluation entrypoint for wildlife trafficking detection")


if __name__ == "__main__":
    main()
EOT

cat > tests/test_smoke.py <<'EOT'
def test_import() -> None:
    import src.wildlife_trafficking_detection  # noqa: F401
EOT

touch notebooks/01_exploration.ipynb

git add .
git commit -m "Initialize professional project structure"
git push origin main