import cv2
import os
import numpy as np

def evaluate_sheet(image_path, answer_key):
    """
    Evaluate a single OMR sheet.
    Extracts student ID & name from filename:
        expected format: studentID_studentName.png
    Returns: student_id, student_name, score
    """
    # Extract student info from filename
    base = os.path.basename(image_path)          # e.g., "101_Ankit_Sharma.png"
    name_part, _ = os.path.splitext(base)
    parts = name_part.split("_", 1)

    if len(parts) == 2:
        student_id = parts[0]
        student_name = parts[1].replace("_", " ")
    else:
        student_id = parts[0]
        student_name = "Unknown"

    # --- Dummy OMR evaluation ---
    # Replace with actual OpenCV bubble detection
    total_questions = len(answer_key)
    score = np.random.randint(0, total_questions + 1)

    return student_id, student_name, score
