import csv
from pathlib import Path

def read_csv_rows(file_path: str) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []

    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)
        if not rows:
            raise ValueError("CSV file is empty")
    return rows
