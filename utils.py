import os
import zipfile
import pandas as pd
from omr_processor import evaluate_sheet

def extract_zip(zip_file, extract_to="input_sheets"):
    os.makedirs(extract_to, exist_ok=True)
    with zipfile.ZipFile(zip_file, "r") as zip_ref:
        zip_ref.extractall(extract_to)
    return [os.path.join(extract_to, f) for f in os.listdir(extract_to) if f.endswith(".png")]

def process_sheets(sheet_files, answer_key_path):
    if not os.path.exists(answer_key_path):
        raise FileNotFoundError(f"Answer key not found: {answer_key_path}")

    answer_key = pd.read_csv(answer_key_path)
    results = []

    for sheet in sheet_files:
        student_id, student_name, score = evaluate_sheet(sheet, answer_key)
        results.append({
            "student_id": student_id,
            "student_name": student_name,
            "score": score
        })

    return pd.DataFrame(results)
