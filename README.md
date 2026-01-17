# 🧠 BrainTumorAI — AI-Powered Brain Tumor Detection System

**BrainTumorAI** is an advanced medical AI web application that detects brain tumors from MRI images using deep learning.  
The system leverages **YOLOv8 object detection** to accurately localize tumors and presents results through a modern, user-friendly Flask web interface.

---

## 🎯 Objective

To design and develop an AI-based brain tumor detection system that can automatically analyze MRI images and highlight potential tumor regions, helping in early detection and medical research support.

---

## ❗ Problem Statement

Manual analysis of brain MRI scans is:
- Time-consuming  
- Prone to human error  
- Dependent on expert availability  

Early and accurate tumor detection is critical, but manual screening can delay diagnosis.

---

## 💡 Proposed Solution

BrainTumorAI provides an automated AI-driven solution that:

- Accepts brain MRI images (JPG / PNG)
- Uses **YOLOv8 deep learning model** for tumor detection
- Draws bounding boxes around detected tumor regions
- Displays uploaded and predicted images side-by-side
- Offers a clean, responsive, and modern UI
- Ensures fast inference and privacy-friendly processing

---

## 🔄 System Workflow

1. Upload brain MRI image  
2. Image preprocessing  
3. YOLOv8 model inference  
4. Tumor region detection  
5. Bounding-box visualization  
6. Display results to user  

---

## 🧠 Deep Learning Techniques Used

- Convolutional Neural Networks (CNN)
- YOLOv8 Object Detection
- Image preprocessing with OpenCV
- Confidence-based prediction filtering

---

## 🛠️ Tech Stack

### 🔹 Backend
- Python
- Flask
- Ultralytics YOLOv8
- OpenCV
- NumPy

### 🔹 Frontend
- HTML5
- CSS3
- Bootstrap 5
- Animate.css

---

## ⭐ Key Features

- Brain tumor detection from MRI images
- YOLOv8-based bounding box visualization
- Fast and accurate AI inference
- Upload & predicted image comparison
- Modern red-pink gradient UI
- Frequently Asked Questions (FAQ) section
- Deployable on Render / Replit

---

## 📊 Output

- Original uploaded MRI image
- Detected tumor image with bounding boxes
- Visual AI-assisted diagnosis output

---
🌐 Live Demo

🚀 Try BrainTumorAI Live
Experience real-time AI-powered brain tumor detection directly in your browser:

🔗 Live Application:
👉 https://braintumor-ai.onrender.com
---

## 🚀 Quick Start — Clone & Run

### 1️⃣ Clone Repository
```bash
git clone https://github.com/Ankitaghavate/BrainTumorAI.git
cd BrainTumorAI
```

2. Create a virtual environment (recommended)
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Run the Flask application
```bash
python app.py
```

5. Open in your browser
```
http://127.0.0.1:5000/
```
## 🤝 Contributing

Contributions are welcome! To contribute:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/YourFeature`)
3. **Commit** your changes (`git commit -m 'Add some feature'`)
4. **Open** a Pull Request
---

