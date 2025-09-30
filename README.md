# 🎥 Video to Grayscale Converter

Convert any video into grayscale instantly with a FastAPI backend, OpenCV processing, and a Streamlit web client.

---

## ✨ Features
- 📤 Upload videos in `.mp4`, `.avi`, `.mov`, `.mkv` formats  
- ⚙️ Automatic frame-by-frame grayscale conversion (OpenCV)  
- 🌐 FastAPI backend with REST API endpoint  
- 🎛 Streamlit frontend for easy uploading, preview, and download  
- 📥 Download processed grayscale video directly  

---

## 🛠 Tech Stack
- **FastAPI** → Backend REST API  
- **OpenCV** → Video frame processing  
- **Streamlit** → Web-based client for upload & preview  
- **Requests** → Client–server communication  

---

## 📂 Project Structure
```
video-grayscale-converter/
│── main.py         # FastAPI server
│── processor.py    # OpenCV grayscale logic
│── client.py       # Streamlit frontend
│── uploads/        # Raw uploaded videos
│── outputs/        # Grayscale processed videos
│── README.md       # Documentation
```

---

## ⚡ Installation & Setup

### 1️⃣ Clone Repository
```bash
git clone https://github.com/yourusername/video-grayscale-converter.git
cd video-grayscale-converter
```

### 2️⃣ Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux / Mac
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies
```bash
pip install fastapi uvicorn opencv-python streamlit requests python-multipart
```

---

## ▶ Running the App

### 1️⃣ Start FastAPI Backend
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```
- API Docs → [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  
- Root → [http://127.0.0.1:8000/](http://127.0.0.1:8000/)  

### 2️⃣ Start Streamlit Frontend
```bash
streamlit run client.py
```
- Opens automatically in your browser.  
- Upload video → Convert → Preview → Download.  

---


## 📸 Screenshots

### 🔹 Upload Page
<img width="805" height="339" alt="image2" src="https://github.com/user-attachments/assets/91352ffc-6e56-476a-9f1d-fa256c3cb4c5" />


### 🔹 After Processing
<img width="752" height="516" alt="image1" src="https://github.com/user-attachments/assets/9b0c84ff-eaaf-4401-b880-a132f1672f69" />




---

## 🚀 Future Improvements
- Add more video filters (blur, edge detection, sepia, etc.)  
- Support real-time video streaming  


---

## 📜 License
This project is licensed under the MIT License – feel free to use and modify.  

