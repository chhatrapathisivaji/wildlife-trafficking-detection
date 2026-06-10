# Wildlife Trafficking Detection

A machine learning project for detecting potentially illegal wildlife-related advertisements using multimodal signals from online listings, including images, text, price, seller metadata, and location features.

## Overview

Illegal wildlife trade threatens biodiversity, ecosystems, and public health. Online marketplaces make enforcement especially difficult because listings appear at scale, change quickly, and often disappear in a short amount of time.

This project focuses on identifying wildlife-related trafficking signals from advertisement data through data collection, cleaning, feature engineering, and multimodal classification. The approach combines computer vision, natural language processing, and structured metadata analysis to classify listings more effectively than using text or images alone.

## Problem Statement

The core task is to determine whether an online advertisement is associated with wildlife trade based on information such as:

- Listing image
- Title
- Description
- Price
- Seller information
- Geographic metadata

The project breaks this into three major parts:

1. Data gathering
2. Image analysis
3. Text and metadata analysis

These components are then combined into a final classification pipeline.

## Approach

The project is organized around two major pipelines:

### 1. Data Collection Pipeline

This pipeline gathers advertisement data from online sources and stores fields such as:

- Image URLs
- Titles
- Descriptions
- Seller information
- Prices
- Locations

The goal is to build a dataset that captures both visual and textual signals from wildlife-related listings.

### 2. Data Inference Pipeline

This pipeline cleans, transforms, and models the collected data for classification. It includes:

- Data cleaning for duplicates, missing values, and inconsistent location fields
- Price normalization to reduce outlier effects caused by mixed currencies
- Feature engineering using structured attributes such as seller, country, category, and price ranges
- Multimodal learning using image, text, and tabular inputs together

## Model Design

The project uses a multimodal model built from four main components:

- **Image encoder:** EfficientNet-based image feature extraction
- **Text encoder:** DistilBERT for transforming listing descriptions into contextual text embeddings
- **Cross-attention layer:** Learns interactions between visual and textual information
- **Fusion head:** Combines image features, text features, normalized price, and encoded country information for final prediction

This design helps capture richer patterns than a unimodal baseline because suspicious listings often reveal useful clues across multiple types of data.

## Data

The dataset is built from crawled online listings and includes fields such as:

- URL
- Title
- Text
- Domain
- Description
- Image
- Price
- Seller
- Location
- Coordinates
- Country
- Image path

To keep data collection manageable while still capturing a broad set of animal-related product listings, the project focuses on advertisement data collected from e-commerce sources such as eBay.

> **Note:** The raw dataset is not included in this public repository. Only documentation, code, and safe project artifacts should be shared publicly.

## Results

After cleaning and augmentation, the multimodal model was trained for 20 epochs using an 80/20 train-test split.

| Dataset  | Precision | Recall | Accuracy |
|----------|----------:|-------:|---------:|
| Training | 99.07     | 99.53  | 99.58    |
| Testing  | 85.11     | 93.02  | 94.08    |

The model performed strongly on the testing dataset, especially in recall, showing that it was effective at identifying positive cases. Precision can likely be improved further with more data and additional tuning.

## Repository Structure

```text
wildlife-trafficking-detection/
├── assets/                         # Images, figures, and README visuals
├── data/                           # Data documentation, schemas, and safe placeholders
├── models/                         # Saved model artifacts or model notes
├── notebooks/                      # Experiments, exploration, and prototype workflows
├── reports/                        # Preliminary and final project reports
├── src/
│   └── wildlife_trafficking_detection/
│       ├── data/                   # Data loading and preprocessing utilities
│       ├── features/               # Feature engineering and transformations
│       ├── models/                 # Training and inference code
│       ├── evaluation/             # Metrics and validation logic
│       └── utils/                  # Shared helpers
├── tests/                          # Smoke tests and validation checks
├── README.md
└── LICENSE
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

Train the model:

```bash
python -m src.wildlife_trafficking_detection.train
```

Run evaluation:

```bash
python -m src.wildlife_trafficking_detection.evaluate
```

## Tech Stack

- Python
- PyTorch
- EfficientNet
- DistilBERT
- Jupyter Notebook
- DuckDB
- MinIO
- Pandas
- NumPy

## My Contribution

Contributed to the project through:

- Data preparation and repository organization for reproducible experimentation
- Multimodal modeling across image, text, and structured listing features
- Training, evaluation, and documentation of project workflows and results

This public repository is intended to showcase the project structure and technical approach without exposing sensitive data or private project assets.

## Future Work

Possible next steps include:

- Expanding the training dataset to improve generalization
- Improving precision through hyperparameter tuning and architecture refinement
- Strengthening data cleaning and label quality for harder edge cases
- Comparing the multimodal model against simpler text-only and image-only baselines
- Exploring stronger fusion strategies for image, text, and metadata features

## License

This project is licensed under the MIT License.
