from fastapi import FastAPI
from pydantic import BaseModel

from db_integration import SessionLocal, engine
from db_model import Base, Student


app = FastAPI()


# Create the database tables
Base.metadata.create_all(bind=engine)


class StudentSchema(BaseModel):
    name: str
    age: int
    class_name: str


# CREATE
@app.post("/students")
def create_student(student: StudentSchema):

    db = SessionLocal()

    new_student = Student(
        name=student.name,
        age=student.age,
        class_name=student.class_name
    )

    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    db.close()

    return new_student


# READ ALL
@app.get("/students")
def get_students():

    db = SessionLocal()

    students = db.query(Student).all()

    db.close()

    return students


# READ ONE
@app.get("/students/{student_id}")
def get_student(student_id: int):

    db = SessionLocal()

    student = db.query(Student).filter(Student.id == student_id).first()

    db.close()

    return student


# UPDATE
@app.put("/students/{student_id}")
def update_student(student_id: int, updated_student: StudentSchema):

    db = SessionLocal()

    student = db.query(Student).filter(Student.id == student_id).first()

    if student is None:
        db.close()
        return {"message": "Student not found"}

    student.name = updated_student.name
    student.age = updated_student.age
    student.class_name = updated_student.class_name

    db.commit()
    db.refresh(student)

    db.close()

    return student


# DELETE
@app.delete("/students/{student_id}")
def delete_student(student_id: int):

    db = SessionLocal()

    student = db.query(Student).filter(Student.id == student_id).first()

    if student is None:
        db.close()
        return {"message": "Student not found"}

    db.delete(student)
    db.commit()

    db.close()

    return {"message": "Student deleted successfully"}