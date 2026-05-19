"""Add a date column derived from timestamp."""
from pathlib import Path

import pandas as pd

INPUT = Path("data/clean/events.csv")
OUTPUT = Path("data/transformed/events.csv")


def main() -> None:
    df = pd.read_csv(INPUT)
    df["date"] = pd.to_datetime(df["timestamp"]).dt.strftime("%Y-%m-%d")

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUTPUT, index=False)


if __name__ == "__main__":
    main()
