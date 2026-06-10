from __future__ import annotations

from pathlib import Path
from typing import Optional

import pandas as pd

try:
    from minio import Minio
except Exception:
    Minio = None


def load_parquet_data(path: str | Path) -> pd.DataFrame:
    return pd.read_parquet(path)


def load_csv_data(path: str | Path) -> pd.DataFrame:
    return pd.read_csv(path)


def configure_minio_client(
    endpoint: str,
    access_key: str,
    secret_key: str,
    secure: bool = False,
):
    if Minio is None:
        raise ImportError("minio is not installed. Install it to use object storage helpers.")
    return Minio(endpoint, access_key=access_key, secret_key=secret_key, secure=secure)


def resolve_image_path(image_root: str | Path, image_path: Optional[str]) -> Optional[Path]:
    if not image_path:
        return None
    path = Path(image_root) / image_path
    return path if path.exists() else None