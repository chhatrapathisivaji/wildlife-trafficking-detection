# Data

The original dataset is not included in this repository.

## Expected inputs

The archived project notebooks indicate that the pipeline used:
- A parquet file containing listing metadata and labels.
- A CSV file variant for experimentation.
- Images stored separately and referenced through `imagepath` or related fields.
- Optional remote object storage access for images.

## Suggested layout

```text
data/
├── raw/
├── interim/
├── processed/
└── external/
```