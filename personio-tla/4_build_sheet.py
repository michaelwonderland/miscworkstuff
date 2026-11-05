"""Build data/personio_tla_prospects.xlsx (Prospects / Companies / Method tabs) for upload to Google Sheets."""
import csv
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter

wb = Workbook()
HEAD = PatternFill("solid", fgColor="1F2937")
TIER = {"A": "D1FAE5", "B": "FEF3C7", "C": "F3F4F6"}


def sheet(ws, path, widths, tier_col=None, num_cols=()):
    rows = list(csv.reader(open(path)))
    for r in rows:
        ws.append([float(v) if (i in num_cols and v not in ("", None)) else v for i, v in enumerate(r)] if r is not rows[0] else r)
    for c in ws[1]:
        c.font, c.fill, c.alignment = Font(bold=True, color="FFFFFF"), HEAD, Alignment(wrap_text=True, vertical="top")
    for i, w in enumerate(widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = w
    ws.freeze_panes = "E2" if tier_col is not None else "B2"
    ws.auto_filter.ref = ws.dimensions
    if tier_col is not None:
        for row in ws.iter_rows(min_row=2):
            row[tier_col].fill = PatternFill("solid", fgColor=TIER[row[tier_col].value])


hdr = next(csv.reader(open("data/ranked.csv")))
keep = ["Rank", "Tier", "Score", "Name", "Title", "Title bucket", "Company", "Country", "Followers", "Posts 90d",
        "Reposts 90d", "Median reactions", "Last post", "Personio signal", "Creator mode", "Why", "LinkedIn",
        "Reach pts", "Activity pts", "Title pts", "Topic pts", "Personio pts"]
rows = list(csv.DictReader(open("data/ranked.csv")))  # all candidates
with open("data/_prospects.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=keep, extrasaction="ignore"); w.writeheader(); w.writerows(rows)

ws = wb.active; ws.title = "Prospects"
num = {keep.index(k) for k in ["Rank", "Score", "Followers", "Posts 90d", "Reposts 90d", "Median reactions",
                               "Reach pts", "Activity pts", "Title pts", "Topic pts", "Personio pts"]}
sheet(ws, "data/_prospects.csv", [6, 5, 7, 24, 34, 18, 22, 10, 10, 8, 8, 9, 11, 28, 8, 60, 40, 7, 7, 7, 7, 7],
      tier_col=1, num_cols=num)

ws2 = wb.create_sheet("Companies")
sheet(ws2, "data/companies_summary.csv", [30, 11, 10, 22, 10, 7, 7, 55, 55], num_cols={4, 5, 6})

ws3 = wb.create_sheet("Method")
for line in open("METHOD.md").read().splitlines():
    ws3.append([line])
ws3.column_dimensions["A"].width = 140
wb.save("data/personio_tla_prospects.xlsx")
print("ok", len(rows))
