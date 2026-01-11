from fastapi import FastAPI, Path
from typing import Optional
app = FastAPI()

students = {
    1: {"name": "Alice", "age": 20, "major": "Computer Science"},
    2: {"name": "Bob", "age": 22, "major": "Mathematics"},
    3: {"name": "Charlie", "age": 21, "major": "Physics"},
    
}


@app.get("/")
def root():
    return students

# @app.get("/student/{student_id}")
# def get_student(student_id: int):
#     student = students.get(student_id)
#     if student:
#         return student
#     return {"error": "Student not found"}

@app.get("/student/{student_id}")
# For Path we have gt(greater than), lt(less than), ge(greater equal), le(less equal), etc.
def get_student(student_id: int = Path(None, description="The ID of the student to retrieve"), gt=0):
    student = students.get(student_id)
    if student:
        return student
    return {"error": "Student not found"}

# query parameter
@app.get("/student/get-by-name")
def get_student_by_name(name: Optional[str] = None):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"error": "Student not found"}

# request body
@app.post("/student/{student_id}")
def create_student(student_id: int, student: dict):
    if student_id in students:
        return {"error": "Student ID already exists"}
    students[student_id] = student
    return students[student_id]