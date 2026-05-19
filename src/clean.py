"""Clean raw events data."""
from pathlib import Path

import pandas as pd

VALID_EVENT_TYPES = {"click", "login", "scroll", "view", "purchase"}

INPUT = Path("data/raw/events.csv")
OUTPUT = Path("data/clean/events.csv")


def main() -> None:
    df = pd.read_csv(INPUT)

    df = df.dropna()

    df = df[df["event_type"].isin(VALID_EVENT_TYPES)]

    df = df[pd.to_numeric(df["duration_seconds"], errors="coerce") > 0]
    df["duration_seconds"] = df["duration_seconds"].astype(int)

    parsed = pd.to_datetime(df["timestamp"], errors="coerce", format="mixed")
    df = df.loc[parsed.notna()].copy()
    df["timestamp"] = parsed.loc[df.index].dt.strftime("%Y-%m-%dT%H:%M:%S")

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUTPUT, index=False)


if __name__ == "__main__":
    main()
