import cv2
import numpy as np
import pytesseract

def read_student_info(img):
    # Crop top part of sheet where name & id are printed
    h, w = img.shape[:2]
    roi = img[0:int(h*0.2), 0:w]

    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray)

    # crude parsing
    student_id = "Unknown"
    student_name = "Unknown"

    for line in text.split("\n"):
        if "ID" in line.upper():
            student_id = line.split(":")[-1].strip()
        elif "NAME" in line.upper():
            student_name = line.split(":")[-1].strip()

    return student_id, student_name

def evaluate_sheet(sheet_path, answer_key):
    img = cv2.imread(sheet_path)
    if img is None:
        return "NA", "Invalid Sheet", 0

    student_id, student_name = read_student_info(img)

    # Dummy evaluation: Random score until bubble detection is implemented
    total_questions = len(answer_key)
    score = np.random.randint(0, total_questions + 1)

    return student_id, student_name, score
