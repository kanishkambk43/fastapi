from fastapi import FastAPI, UploadFile, File

app = FastAPI()


@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):

    file_path = f"uploads/{file.filename}"

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    return {
        "message": "File uploaded successfully",
        "filename": file.filename
    }