# ------------------------------------------------------------
# © 2025 Sarthak Raut
# Resume Relevance Check System
# All rights reserved. Unauthorized copying, modification,
# or distribution of this file is prohibited.
# ------------------------------------------------------------

from fastapi import FastAPI, File, UploadFile
import shutil
import os
from utils import extract_zip, process_sheets
import traceback

app = FastAPI(
    title="OMR Evaluation System",           # This changes the header
    description="Automated OMR scoring app", # Optional description
    version=None                        # Optional version
    )

UPLOAD_DIR = "input"
OUTPUT_CSV = "output/results.csv"
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs("output", exist_ok=True)

@app.post("/upload_zip/")
async def upload_zip(file: UploadFile = File(...)):
    try:
        zip_path = os.path.join(UPLOAD_DIR, file.filename)
        with open(zip_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        extracted_folder = os.path.join(UPLOAD_DIR, file.filename+"_extracted")
        extracted_files = extract_zip(zip_path, extracted_folder)

        results = process_sheets(extracted_files, OUTPUT_CSV)
        return {"message": "Processed successfully", "results": results}

    except Exception as e:
        # Return full traceback for debugging
        return {"error": str(e), "trace": traceback.format_exc()}
