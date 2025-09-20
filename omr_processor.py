# ------------------------------------------------------------
# © 2025 Sarthak Raut
# Resume Relevance Check System
# All rights reserved. Unauthorized copying, modification,
# or distribution of this file is prohibited.
# ------------------------------------------------------------

import cv2
import numpy as np
import pytesseract
import json

import pytesseract

# Set tesseract path explicitly if not in PATH
pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"


# Load answer key
with open("answer_keys/version1.json", "r") as f:
    ANSWER_KEY = json.load(f)

options = ["A", "B", "C", "D"]

def read_student_info(img):
    """
    Detect student ID and Name from top of sheet using OCR
    """
    # Crop top area (ID and Name)
    top_crop = img[50:300, 50:1500]  # Adjust based on your sheet
    gray = cv2.cvtColor(top_crop, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray)
    lines = [line.strip() for line in text.split("\n") if line.strip()]
    student_id = lines[0].replace("ID:", "").strip() if len(lines) > 0 else "unknown"
    student_name = lines[1].replace("Name:", "").strip() if len(lines) > 1 else "unknown"
    return student_id, student_name

def detect_answers(img):
    """
    Detect marked option for 100 questions
    Assumes:
    - 4 columns of ~30 questions per column
    - 4 horizontal options (A/B/C/D) per question
    - Bubble positions are known relative to sheet
    """
    height, width = img.shape[:2]
    questions_per_column = 30
    columns = 4
    options_count = 4

    start_y = 400
    start_x = 50
    column_spacing = 600
    row_height = 100
    bubble_radius = 20
    option_spacing = 50

    detected_answers = []

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV)

    for q_idx in range(100):
        col = q_idx // questions_per_column
        row_in_col = q_idx % questions_per_column
        y = start_y + row_in_col * row_height
        x_start = start_x + col * column_spacing

        filled = None
        for o in range(options_count):
            x = x_start + 50 + o * option_spacing
            # Crop around bubble
            x1 = int(x - bubble_radius)
            y1 = int(y + 40 - bubble_radius)
            x2 = int(x + bubble_radius)
            y2 = int(y + 40 + bubble_radius)
            roi = thresh[y1:y2, x1:x2]
            filled_ratio = cv2.countNonZero(roi) / (roi.shape[0]*roi.shape[1])
            if filled_ratio > 0.5:  # threshold for marked bubble
                filled = options[o]
                break
        if filled is None:
            filled = "-"  # no bubble marked
        detected_answers.append(filled)
    return detected_answers

def score_answers(detected_answers):
    score = 0
    for q_idx, ans in enumerate(detected_answers):
        correct = ANSWER_KEY.get(str(q_idx+1))
        if ans == correct:
            score += 1
    return score
