import streamlit as st
import pandas as pd
from utils import extract_zip, process_sheets
import os

st.set_page_config(page_title="OMR Evaluation System", layout="wide")
st.title("📄 OMR Evaluation System")

uploaded_zip = st.file_uploader("Upload ZIP of OMR Sheets", type=["zip"])
uploaded_key = st.file_uploader("Upload Answer Key CSV", type=["csv"])

if uploaded_zip and uploaded_key:
    # Save uploaded files
    os.makedirs("input_files", exist_ok=True)
    zip_path = os.path.join("input_files", "temp.zip")
    key_path = os.path.join("input_files", "answer_key.csv")

    with open(zip_path, "wb") as f:
        f.write(uploaded_zip.read())

    with open(key_path, "wb") as f:
        f.write(uploaded_key.read())

    st.info("Processing OMR sheets... ⏳")

    # Extract sheets and process
    sheet_files = extract_zip(zip_path, "input_sheets")
    df = process_sheets(sheet_files, key_path)

    st.success("✅ Processing complete!")
    st.dataframe(df)

    # Save results
    os.makedirs("output_results", exist_ok=True)
    result_csv_path = os.path.join("output_results", "results.csv")
    df.to_csv(result_csv_path, index=False)

    # Download button
    csv_bytes = df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="📥 Download Results CSV",
        data=csv_bytes,
        file_name="results.csv",
        mime="text/csv"
    )
