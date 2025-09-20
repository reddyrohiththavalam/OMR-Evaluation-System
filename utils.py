import os
import zipfile
import csv
import cv2
from omr_processor import read_student_info, detect_answers, score_answers

def extract_zip(zip_path, extract_to):
    os.makedirs(extract_to, exist_ok=True)
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    return [os.path.join(extract_to, f) for f in os.listdir(extract_to) if f.endswith(".png")]

def process_sheets(sheet_files, output_csv):
    results = []
    for file in sheet_files:
        img = cv2.imread(file)
        student_id, student_name = read_student_info(img)
        detected_answers = detect_answers(img)
        score = score_answers(detected_answers)
        results.append([student_id, student_name, score])
    # Save CSV
    if os.path.exists(output_csv):
        # append new results
        with open(output_csv, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(results)
    else:
        with open(output_csv, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["student_id", "student_name", "score"])
            writer.writerows(results)
    return results
