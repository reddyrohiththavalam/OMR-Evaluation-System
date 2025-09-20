import streamlit as st
import pandas as pd
from utils import extract_zip, process_sheets

st.set_page_config(page_title="OMR Evaluation System", layout="wide")

st.title("📄 OMR Sheet Evaluation System")
st.write("Upload a ZIP file containing scanned OMR sheets.")

uploaded_file = st.file_uploader("Upload ZIP of OMR Sheets", type=["zip"])
answer_key_file = "answer_key.csv"

if uploaded_file is not None:
    with st.spinner("Processing sheets..."):
        extracted_files = extract_zip(uploaded_file)
        df = process_sheets(extracted_files, answer_key_file)
        st.success("✅ Evaluation complete!")

        st.subheader("Results")
        st.dataframe(df)

        st.download_button(
            label="Download Results CSV",
            data=df.to_csv(index=False),
            file_name="results.csv",
            mime="text/csv"
        )
