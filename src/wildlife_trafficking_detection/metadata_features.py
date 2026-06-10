from __future__ import annotations

import pandas as pd


def build_vocab(series: pd.Series, max_items: int | None = None) -> list[str]:
    values = series.fillna("unknown").astype(str).value_counts().index.tolist()
    return values[:max_items] if max_items else values


def encode_one_hot(value: str, vocab: list[str]) -> list[float]:
    value = str(value) if value is not None else "unknown"
    return [1.0 if value == token else 0.0 for token in vocab]


def build_metadata_vector(row: pd.Series, country_vocab: list[str], seller_vocab: list[str]) -> list[float]:
    price_usd = float(row.get("price_usd", 0.0) or 0.0)
    country_vec = encode_one_hot(row.get("country", "unknown"), country_vocab)
    seller_vec = encode_one_hot(row.get("seller", "unknown"), seller_vocab)
    return [price_usd] + country_vec + seller_vec