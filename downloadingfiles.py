from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
import os

app = FastAPI()


@app.get("/download")
async def download_file():

    file_path = "uploads/resume.pdf"

    if not os.path.exists(file_path):
        raise HTTPException(
            status_code=404,
            detail="File not found"
        )

    return FileResponse(
        file_path,
        filename="resume.pdf"
    )