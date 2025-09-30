from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
from processor import process_video_file

app = FastAPI()

@app.post("/process_video/")
async def process_video(file: UploadFile = File(...)):
    # Call processing logic from processor.py
    output_path = process_video_file(file.file, file.filename)

    return FileResponse(
        output_path,
        media_type="video/avi",
        filename=f"gray_{file.filename}"
    )
