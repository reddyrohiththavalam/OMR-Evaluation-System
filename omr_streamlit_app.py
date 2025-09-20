import streamlit as st
import pandas as pd
from utils import extract_zip, process_sheets

st.set_page_config(page_title="OMR Evaluation System", layout="wide")
st.title("📄 OMR Evaluation System with QR Student Info")

uploaded_zip = st.file_uploader("Upload ZIP of OMR Sheets", type=["zip"])
uploaded_key = st.file_uploader("Upload Answer Key (CSV)", type=["csv"])

if uploaded_zip and uploaded_key:
    with open("temp.zip", "wb") as f:
        f.write(uploaded_zip.read())

    with open("answer_key.csv", "wb") as f:
        f.write(uploaded_key.read())

    st.info("Processing sheets... ⏳")

    sheet_files = extract_zip("temp.zip", "input_sheets")
    df = process_sheets(sheet_files, "answer_key.csv")

    st.success("✅ Processing complete!")
    st.dataframe(df)

    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button(
        "📥 Download Results CSV",
        data=csv,
        file_name="results.csv",
        mime="text/csv"
    )
