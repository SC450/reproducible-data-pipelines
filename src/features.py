"""Add duration_minutes and weekday feature columns."""
from pathlib import Path

import pandas as pd

INPUT = Path("data/transformed/events.csv")
OUTPUT = Path("data/features/events.csv")


def main() -> None:
    df = pd.read_csv(INPUT)
    df["duration_minutes"] = df["duration_seconds"] / 60
    df["weekday"] = pd.to_datetime(df["date"]).dt.day_name()

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUTPUT, index=False)


if __name__ == "__main__":
    main()
