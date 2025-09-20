import cv2
import os
import numpy as np

def evaluate_sheet(image_path, answer_key):
    """
    Dummy evaluation of OMR sheet.
    Extracts student_id and name from filename instead of OCR.
    """
    img = cv2.imread(image_path)
    if img is None:
        raise FileNotFoundError(f"Image not found: {image_path}")

    # --- Extract student info from filename ---
    base = os.path.basename(image_path)
    student_id = base.split("_")[0]
    student_name = " ".join(base.split("_")[1:]).replace(".png", "")

    # --- Fake bubble detection (replace with real logic) ---
    total_questions = len(answer_key)
    score = np.random.randint(0, total_questions + 1)

    return student_id, student_name, score
