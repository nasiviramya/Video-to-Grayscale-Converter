# Video-to-Grayscale-Converter
This project lets you upload a video, process it into grayscale using OpenCV, and download the result.
✨ Features

📤 Upload videos in .mp4, .avi, .mov, .mkv formats

⚙️ Automatic frame-by-frame grayscale conversion (OpenCV)

🌐 FastAPI backend with REST API endpoint

🎛 Streamlit frontend for easy uploading, preview, and download

📥 Download processed grayscale video directly

🛠 Tech Stack

FastAPI → Backend REST API

OpenCV → Video frame processing

Streamlit → Web-based client for upload & preview

Requests → Client–server communication

📂 Project Structure
video-grayscale-converter/
│── main.py         # FastAPI server
│── processor.py    # OpenCV grayscale logic
│── client.py       # Streamlit frontend
│── uploads/        # Raw uploaded videos
│── outputs/        # Grayscale processed videos
│── README.md       # Documentation
