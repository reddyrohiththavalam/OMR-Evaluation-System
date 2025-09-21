# Automated OMR Evaluation & Scoring System

## 📌 Overview
This project implements an **Automated OMR (Optical Mark Recognition) Evaluation System** for placement readiness assessments.  
It allows evaluators to upload scanned/captured OMR sheets and get instant per-subject & total scores with <0.5% error tolerance.

## 🎯 Features
- ✅ Mobile camera capture of OMR sheets  
- ✅ Auto sheet version detection (A/B/C/D via OCR/fiducials)  
- ✅ Preprocessing: rotation, skew, and perspective correction  
- ✅ Bubble detection via OpenCV with template-driven grid  
- ✅ ML classifier (TensorFlow Lite) for ambiguous bubbles  
- ✅ Answer key matching & scoring (per subject + total)  
- ✅ Web app for uploads, reviews, analytics  
- ✅ Batch processing for multiple sheets  
- ✅ PostgreSQL storage with evaluator authentication  
- ✅ Export results (CSV/Excel) & maintain audit trail  

---

## 🛠 Tech Stack
### Core OMR Evaluation
- Python, OpenCV, NumPy, SciPy, Pillow  
- TensorFlow/Keras → TFLite for bubble classification  

### Web Application
- Flask / FastAPI (backend APIs)  
- Streamlit (MVP frontend dashboard)  
- PostgreSQL (results storage)  

### Deployment
- Docker container for easy deployment  

---

## 📂 Project Structure
