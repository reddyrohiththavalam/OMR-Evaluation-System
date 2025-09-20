import os
import zipfile
import pandas as pd
from omr_processor import evaluate_sheet

def extract_zip(zip_file, extract_to="temp_extracted"):
    if os.path.exists(extract_to):
        for f in os.listdir(extract_to):
            os.remove(os.path.join(extract_to, f))
    else:
        os.makedirs(extract_to)

    with zipfile.ZipFile(zip_file, "r") as z:
        z.extractall(extract_to)
    return [os.path.join(extract_to, f) for f in os.listdir(extract_to)]

def process_sheets(sheet_files, answer_key_path):
    results = []
    answer_key = pd.read_csv(answer_key_path)

    for sheet in sheet_files:
        student_id, student_name, score = evaluate_sheet(sheet, answer_key)
        results.append({
            "Student ID": student_id,
            "Name": student_name,
            "Score": score
        })

    df = pd.DataFrame(results)
    df.to_csv("results.csv", index=False)
    return df
