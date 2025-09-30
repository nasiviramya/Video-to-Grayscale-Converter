import cv2
import os
import uuid
import shutil

UPLOAD_DIR = "uploads"
OUTPUT_DIR = "outputs"
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

def process_video_file(file, filename):
    # Save uploaded video
    input_path = os.path.join(UPLOAD_DIR, f"{uuid.uuid4()}_{filename}")
    output_path = os.path.join(OUTPUT_DIR, f"gray_{filename}")

    with open(input_path, "wb") as buffer:
        shutil.copyfileobj(file, buffer)

    # Open video with OpenCV
    cap = cv2.VideoCapture(input_path)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height), isColor=False)

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        out.write(gray)

    cap.release()
    out.release()

    return output_path
