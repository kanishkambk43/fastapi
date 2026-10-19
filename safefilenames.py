from fastapi import FastAPI, UploadFile, File
import os
import uuid

app = FastAPI()


@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):

    extension = os.path.splitext(file.filename)[1]

    unique_filename = f"{uuid.uuid4()}{extension}"

    file_path = f"uploads/{unique_filename}"

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    return {
        "original_filename": file.filename,
        "stored_filename": unique_filename
    }