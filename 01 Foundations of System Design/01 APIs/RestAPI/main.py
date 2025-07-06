from fastapi import FastAPI
import uvicorn
import os

# Create the app instance
app = FastAPI(
    title="My First FastAPI App",
    description="A simple API using FastAPI framework",
    version="1.0.0"
)


# Root route
@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}


# Dynamic route with parameter
@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hello, {name}!"}


# Query parameters example
@app.get("/items/")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "query": q}


if __name__ == '__main__':
    uvicorn.run("main:app", host=os.getenv("APP_HOST", "localhost"), port=int(os.getenv("APP_PORT", 8000)),
                reload=True)
