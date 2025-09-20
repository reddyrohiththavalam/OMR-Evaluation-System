import cv2
import numpy as np
from pyzbar.pyzbar import decode
from PIL import Image

def read_student_info_from_qr(img_path):
    """Extract student ID and name from QR code on sheet"""
    img = Image.open(img_path)
    decoded = decode(img)
    if decoded:
        # Expect QR code format: "id:101;name:Ankit Sharma"
        data = decoded[0].data.decode()
        parts = data.split(";")
        student_id = parts[0].split(":")[1].strip()
        student_name = parts[1].split(":")[1].strip()
        return student_id, student_name
    return "Unknown", "Unknown"

def evaluate_sheet(image_path, answer_key):
    """
    Evaluate a single OMR sheet.
    """
    # --- Read student info from QR code ---
    student_id, student_name = read_student_info_from_qr(image_path)

    # --- Dummy bubble detection (replace with real logic) ---
    total_questions = len(answer_key)
    score = np.random.randint(0, total_questions + 1)

    return student_id, student_name, score
