# reproducible-data-pipelines

A small reproducible analysis built with [`uv`](https://docs.astral.sh/uv/),
[DVC](https://dvc.org/), and [Marimo](https://marimo.io/).

## Pipeline

`dvc.yaml` defines three stages, each implemented as a script under `src/`:

1. **clean** — `src/clean.py`: drops rows with missing fields, invalid
   `event_type` values, or non-positive `duration_seconds`, and normalizes
   `timestamp` to ISO 8601. Writes `data/clean/events.csv`.
2. **transform** — `src/transform.py`: adds a `date` column
   (`YYYY-MM-DD`). Writes `data/transformed/events.csv`.
3. **features** — `src/features.py`: adds `duration_minutes`
   (`duration_seconds / 60`) and `weekday` (full day name). Writes
   `data/features/events.csv`.

## Reproducing

```bash
uv sync
uv run dvc repro
```

This regenerates everything under `data/clean/`, `data/transformed/`, and
`data/features/`.

## Report

`notebooks/report.py` is a Marimo notebook that loads
`data/features/events.csv` and plots a histogram of `duration_minutes`.
Run it with:

```bash
uv run marimo edit notebooks/report.py
```
