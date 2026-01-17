from flask import Flask, render_template, request, url_for
import os
import cv2
from ultralytics import YOLO

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Load YOLO model once
yolo_model = YOLO("best.pt")  # replace with your model path


@app.route("/", methods=["GET", "POST"])
def index():
    uploaded_image = None
    detected_image = None
    faq_list = [
        {
            "question": "What does BrainTumorAI analyze?",
            "answer": "It detects and highlights brain tumors from MRI scans using YOLOv8 deep learning model."
        },
        {
            "question": "Is this tool free?",
            "answer": "Yes! BrainTumorAI is completely free for anyone to use 💖."
        },
        {
            "question": "Do I need to register?",
            "answer": "No registration required. Just upload your MRI scan and get results instantly."
        },
        {
            "question": "How accurate is the detection?",
            "answer": "Accuracy depends on the quality of MRI scans and model training, but it is trained with advanced YOLOv8."
        }
    ]

    if request.method == "POST":
        if "brain_image" in request.files:
            file = request.files["brain_image"]
            if file.filename != "":
                uploaded_path = os.path.join(UPLOAD_FOLDER, file.filename)
                file.save(uploaded_path)
                uploaded_image = uploaded_path

                # Predict brain tumor using YOLO
                results = yolo_model.predict(source=uploaded_path, conf=0.5)
                annotated = results[0].plot()
                detected_path = os.path.join(
                    UPLOAD_FOLDER, "brain_detected.jpg")
                cv2.imwrite(detected_path, annotated)
                detected_image = detected_path

    return render_template(
        "index.html",
        uploaded_image=uploaded_image,
        detected_image=detected_image,
        faq_list=faq_list
    )


if __name__ == "__main__":
    app.run(debug=True)
