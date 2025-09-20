# omr_streamlit_app.py
import streamlit as st
import zipfile
import os
from utils import extract_zip, process_sheets

st.set_page_config(page_title="OMR Evaluation System", layout="wide")

st.title("📄 Automated OMR Evaluation System")
st.write("Upload a ZIP of OMR sheets to get student scores instantly.")

uploaded_file = st.file_uploader("Upload OMR sheets ZIP", type="zip")

if uploaded_file:
    with open("input/temp.zip", "wb") as f:
        f.write(uploaded_file.getbuffer())
    extracted_files = extract_zip("input/temp.zip", "input/temp_extracted")
    results = process_sheets(extracted_files, "output/results.csv")
    
    st.success("✅ Processing complete!")
    st.write("### Results")
    st.dataframe(results)
    
    # Download button
    with open("output/results.csv", "rb") as f:
        st.download_button("Download CSV", f, file_name="results.csv")
