from fastapi import FastAPI, Path

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
def get_student(student_id: int = Path(None)):
    student = students.get(student_id)
    if student:
        return student
    return {"error": "Student not found"}