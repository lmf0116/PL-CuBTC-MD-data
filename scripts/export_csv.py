"""Export every sheet of md_simu4data.xlsx to a flat CSV.

The source workbook stores several logically distinct sub-tables (MSD time
series, RDF curves, interaction energies, system composition, ...) inside a
single sheet, so the sheets use stacked multi-row headers. This script does a
faithful cell-by-cell dump (empty cells stay empty) rather than inferring a
single header row: the CSVs are the raw records, and the authoritative,
human-readable layout remains the .xlsx workbook.

Usage:
    python scripts/export_csv.py path/to/md_simu4data.xlsx data/csv
"""

import csv
import sys
from pathlib import Path

from openpyxl import load_workbook

# Original (Chinese) sheet name -> English file slug. Order matches the workbook.
SHEET_SLUGS = [
    ("Sheet1", "sheet01_raw-summary"),
    ("电荷", "sheet02_partial-atomic-charges"),
    ("PL-Cu-x吸附量", "sheet03_gcmc-adsorption"),
    ("PL-Cu-x系统物理组成", "sheet04_md-composition-linkers"),
    ("PL-CuBTC不同温度", "sheet05_temperature-series"),
    ("不同聚合度 298k 1atm", "sheet06_chain-length-series"),
    ("PL-Cu-BTC不同阴离子浓度", "sheet07_salt-concentration-series"),
    ("PL-Cu-BTC不同CuBTC", "sheet08_loading-series"),
    ("力学性能", "sheet09_mechanical-properties"),
]


def cell_text(value):
    if value is None:
        return ""
    if isinstance(value, float):
        # Keep full precision; trim redundant trailing zeros only when safe.
        return repr(value)
    return str(value)


def main() -> None:
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(1)

    src = Path(sys.argv[1])
    out_dir = Path(sys.argv[2])
    out_dir.mkdir(parents=True, exist_ok=True)

    wb = load_workbook(src, data_only=True, read_only=True)

    exported = []
    for ws, (_cn, slug) in zip(wb.worksheets, SHEET_SLUGS):
        dst = out_dir / f"{slug}.csv"
        with dst.open("w", encoding="utf-8", newline="") as fh:
            writer = csv.writer(fh)
            for row in ws.iter_rows(values_only=True):
                writer.writerow([cell_text(v) for v in row])
        exported.append((ws.title, dst.name))
        print(f"  {ws.title}  ->  {dst.name}")

    wb.close()
    print(f"Exported {len(exported)} sheets to {out_dir}")


if __name__ == "__main__":
    main()
