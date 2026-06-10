# Notebooks

This folder contains the original working notebooks used during development of the wildlife trafficking detection project. They are included as reference artifacts to document the experimentation, data access flow, model development process, and intermediate analysis carried out during the project.

## Note

These notebooks are not polished tutorial notebooks. They reflect real project work, so they may include exploratory code, repeated cells, debug steps, environment-specific setup, long outputs, and implementation details that were useful during development but are not optimized for presentation.

## Why they are here

The notebooks are kept in this repository for transparency and technical reference. They show the underlying workflow behind the project more directly than a cleaned summary alone, especially for data retrieval, preprocessing, experimentation, and inference-related work.

## Contents

### `minio_get_data.ipynb`
This notebook contains the data access and retrieval workflow used during project development. It is mainly useful for understanding how project data was sourced, organized, and prepared before modeling.

### `inference.ipynb`
This notebook contains model-side experimentation and inference-related work, including analysis, feature handling, and evaluation steps used during development. It is the main technical reference for understanding how the modeling process evolved.

## How to use these notebooks

Treat these notebooks as engineering notes rather than step-by-step documentation. For a cleaner overview of the project, start with the repository root `README.md` and the project reports, then use these notebooks if you want to inspect the original implementation details.

## Scope and limitations

Some code in these notebooks depends on the original environment, external storage setup, local paths, or project-specific runtime assumptions from the development phase. As a result, the notebooks may not run end-to-end in a fresh environment without adaptation.

## Purpose

The goal of keeping these notebooks in the repository is to preserve the project record and provide additional technical context for collaborators, reviewers, or recruiters who want to see the raw workflow behind the final project deliverables.
