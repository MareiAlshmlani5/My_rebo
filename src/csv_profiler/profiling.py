
values = [
    "10",
    "3.5",
    "42",
    "hello",
    None,
    "",
    "NA",
    "n/a",
    "world",
    "7.2"
]



MISSING = {"", "na", "n/a", "null", "none", "nan"}

def is_missing(value: str | None) -> bool:
    if value is None:
        return True
    return value.strip().casefold() in MISSING

def try_float(value: str) -> float | None:
    try:
        return float(value)
    except ValueError:
        return None

def infer_type(values: list[str]) -> str:
    usable = []
    for v in values:
        if not is_missing(v):
            usable.append(v)
    for v in usable:
        if try_float(v) is None:
            return "string"
    if not usable:
        return "text"
    return "number"

        


print(infer_type(values))

rows = [
    {"age": "25",   "city": "Riyadh"},
    {"age": "30",   "city": "Jeddah"},
    {"age": None,   "city": "Dammam"},
    {"age": "22.5", "city": ""},
    {"age": "NA",   "city": "Mecca"},
    {"age": "40",   "city": None},
]


def column_values(rows: list[dict[str, str]], col:str) -> list[str]:
    values = []
    for row in rows:
        values.append(row.get(col, ""))
    return values   
print(column_values(rows, "city"))





def profile_column(rows: list[dict], col: str) -> dict: # احتاج افهم الارقمنت اكثر
    values = [row.get(col, "") for row in rows]
    total = len(values)
    list_with_out_missing = []
    for v in values:
        if not is_missing(v):
            list_with_out_missing.append(v)

 
    
    missing_count = 0
    for v in values:
        if is_missing(v):
            missing_count += 1

    missing_percent = (missing_count / total * 100)

    
    unique_count = len(set(list_with_out_missing))


    col_type = infer_type(values)

    return {
        "column": col,
        "type": col_type,
        "missing": missing_count,
        "missing_percent": round(missing_percent, 2),
        "unique": unique_count
    }


def profile_rows(rows: list[dict]) -> list[dict]:
    if not rows:
        return []
    
    rows_num = len(rows)
    columns = rows[0].keys()
    col_profiles = [profile_column(rows, col) for col in columns]
    return {"n_rows": rows_num, "n_cols": len(columns), "columns": col_profiles}

print(profile_rows(rows))










    
    




