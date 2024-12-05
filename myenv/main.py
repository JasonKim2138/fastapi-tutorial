from fastapi import FastAPI, Path

app = FastAPI()

students = {
    1: {
        "name": "jason",
        "age": "23",
        "what": "the fuck"
    }
}

@app.get("/")
def read():
    return {"hello": "world"}

@app.get("/student/{student_id}")
def get_student(student_id: int):
    return students[student_id]