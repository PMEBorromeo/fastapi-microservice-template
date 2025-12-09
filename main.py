from fastapi import FastAPI

app = FastAPI(title="Simple FastAPI Service")


# Health endpoint
@app.get("/health")
def health():
    return {"status": "ok"}


# Example list endpoint
@app.get("/tasks")
def get_tasks():
    return [
        {"id": 1, "title": "Write README"},
        {"id": 2, "title": "Build FastAPI endpoint"},
    ]
