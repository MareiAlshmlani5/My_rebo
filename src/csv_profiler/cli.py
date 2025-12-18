import typer
import time 
import json
from pathlib import Path

from csv_profiler.io import read_csv_rows
from csv_profiler.profiling import profile_rows
from csv_profiler.render import render_markdown


app = typer.Typer() 




@app.command(help="profile a csv  file and write json + markdown")
def profile(
    file_path: Path= typer.Argument(...,help="input csv file"),
    out_dir:Path=typer.Option(Path("outputs"),"--out-dir",help="output folder"),
    report_name: str = typer.Option("report", "--report-name", help="Base name for outputs"),
    preview: bool = typer.Option(False, "--preview", help="Print a short summary"),
):
    rows=read_csv_rows(file_path)
    profile=profile_rows(rows)
    md=render_markdown(profile)
    out_dir.mkdir(parents=True,exist_ok=True)
    json_path=out_dir/f"{report_name}.json"
    json_path.write_text(json.dumps(profile))
    md_path=out_dir/f"{report_name}.md"
    md_path.write_text(md)


    if preview:
         print(md)
    

if __name__=="__main__":
    app()