import streamlit as st
from csv_profiler.profiling import profile_rows
from csv_profiler.render import render_markdown
import json
st.set_page_config(page_title="Welcoome", layout="wide")
st.title("Welcome to CSV Profiler")
st.caption("Week 01 • Day 04 — Streamlit GUI")

st.sidebar.header("Inputs")
source = st.sidebar.selectbox("Data source", ["Upload", "Local path"])
st.write("Selected:", source)
st.caption("This is a short description of the application.")

selected_item = st.sidebar.selectbox(
    "Choose an option:",  
    ("Option A", "Option B", "Option C", "Option D") 
)


st.write("You selected:", selected_item)


import streamlit as st
import csv
import json
from io import StringIO

selected_item = st.selectbox("Choose option", ["Option A", "Option B"])
if selected_item == "Option A":
    st.info("This is Option A's content!")
else:
    st.write("Select Option A to see special content.")

uploaded_file = st.file_uploader("Choose CSV", type=["csv"])
rows = []  

if uploaded_file is not None:
    st.write("File name:", uploaded_file.name)
    
    text = uploaded_file.getvalue().decode("utf-8-sig")
<<<<<<< HEAD
else:
    st.info("Please upload a CSV file")
    
file_like = StringIO(text)
reader = csv.DictReader(file_like)   
rows = list(reader)                  
if st.checkbox("Preview first 5 rows"):
    st.write(rows[:5])
=======
    file_like = StringIO(text)
    reader = csv.DictReader(file_like)
    rows = list(reader)
    if not rows:
        st.error("The uploaded CSV file has no rows.")
        st.stop()
>>>>>>> 654c71f (Add README and update project files)

    elif len(rows[0]) == 0:
        st.warning("No column headers detected in the CSV file.")

    if st.checkbox("Preview first 5 rows"):
        st.write(rows[:5])

    rows_len = len(rows)
    col_num = len(rows[0]) if rows else 0
    st.write(f"Number of rows in the uploaded file: {rows_len}")    
    st.write(f"Number of columns in the uploaded file: {col_num}")

    if st.button("Generate report"):
        profile = profile_rows(rows)
        st.write("Profile generated!")
        st.json(profile)
        md = render_markdown(profile)
        st.markdown(md)

    json_text = json.dumps(profile_rows(rows))
    md_text = render_markdown(profile_rows(rows))
    st.download_button("Get JSON", data=json_text, file_name="report.json")
    st.download_button("Get Markdown", data=md_text, file_name="report.md")





