from fastapi import FastAPI, UploadFile, File, HTTPException

app = FastAPI()

MAX_SIZE = 5 * 1024 * 1024


@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):

    allowed_types = ["image/jpeg", "image/png"]

    # Check file type
    if file.content_type not in allowed_types:
        raise HTTPException(
            status_code=400,
            detail="Only JPG and PNG files are allowed"
        )

    # Read file
    contents = await file.read()

    # Check file size
    if len(contents) > MAX_SIZE:
        raise HTTPException(
            status_code=400,
            detail="File is too large. Maximum size is 5 MB"
        )

    return {
        "message": "File accepted",
        "filename": file.filename
    }