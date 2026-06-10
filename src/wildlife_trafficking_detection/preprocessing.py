from __future__ import annotations

from typing import Optional

import pandas as pd


COUNTRY_KEYWORDS = {
    "usa": "United States",
    "united states": "United States",
    "uk": "United Kingdom",
    "united kingdom": "United Kingdom",
    "india": "India",
    "china": "China",
    "vietnam": "Vietnam",
    "thailand": "Thailand",
    "indonesia": "Indonesia",
    "australia": "Australia",
}


def extract_country(location: Optional[str]) -> Optional[str]:
    if not isinstance(location, str):
        return None
    location_lower = location.lower()
    for keyword, country in COUNTRY_KEYWORDS.items():
        if keyword in location_lower:
            return country
    return None


def normalize_country_from_location(df: pd.DataFrame, location_col: str = "location") -> pd.DataFrame:
    result = df.copy()
    result["country"] = result.get("country")
    if "country" not in result.columns:
        result["country"] = None
    mask = result["country"].isna()
    result.loc[mask, "country"] = result.loc[mask, location_col].apply(extract_country)
    return result


def convert_prices_to_usd(
    df: pd.DataFrame,
    price_col: str = "price",
    currency_col: str = "currency",
    rates: Optional[dict] = None,
) -> pd.DataFrame:
    rates = rates or {"USD": 1.0, "EUR": 1.08, "GBP": 1.27, "INR": 0.012}
    result = df.copy()
    result[price_col] = pd.to_numeric(result[price_col], errors="coerce")
    result["price_usd"] = result.apply(
        lambda row: row[price_col] * rates.get(str(row.get(currency_col, "USD")).upper(), 1.0)
        if pd.notna(row[price_col])
        else None,
        axis=1,
    )
    return result


def build_clean_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    result = df.copy()
    required_cols = ["imagepath", "price", "predictedlabel"]
    existing = [c for c in required_cols if c in result.columns]
    if existing:
        result = result.dropna(subset=existing)
    if "text" in result.columns:
        result["text"] = result["text"].fillna("")
    if "title" in result.columns:
        result["title"] = result["title"].fillna("")
    if "description" in result.columns:
        result["description"] = result["description"].fillna("")
    return result.reset_index(drop=True)