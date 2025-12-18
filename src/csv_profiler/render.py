from .profiling import profile_rows
from datetime import datetime

def render_markdown(report: dict) -> str:
    """
    تحويل التقرير إلى صيغة Markdown
    """
    lines = []
    lines.append("# CSV Profiling Report")
    lines.append(f"Generated on: {datetime.now().isoformat(timespec='seconds')}\n")
    lines.append("## Summary \n")
    lines.append("| name | type | missing | missing_percent | unique |")
    lines.append("|---|---:|---:|---:|---:|")

    for col_profile in report["columns"]:
        lines.append(
            f"| {col_profile['column']} | {col_profile['type']} | {col_profile['missing']} | {col_profile['missing_percent']:.2f}% | {col_profile['unique']} |"
        )

    lines.append("\nNotes\n")
    lines.append("Missing values are: None, empty strings, 'NA', 'N/A', 'nan', and 'none' (case insensitive).")
    return "\n".join(lines)

# اختبار مستقل
if __name__ == "__main__":
    from .io import read_csv_rows
    rows = read_csv_rows("../data/sample.csv")
    report = profile_rows(rows)
    print(render_markdown(report))
