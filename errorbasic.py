from fastapi import FastAPI,HTTPException
app=FastAPI()
@app.get("/students/{student_id}")
def get_student(student_id: int):

    if student_id != 1:
        raise HTTPException(
            status_code=201,
            detail="Student not found"
        )

    return {"id": 1, "name": "Kanishka"}