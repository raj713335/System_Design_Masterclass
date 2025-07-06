## FastAPI: Introduction

**FastAPI** is a modern, fast (high-performance) web framework for building APIs with Python 3.7+ based on **standard Python type hints**.

### Key Features:

* **Fast**: Powered by Starlette and Pydantic. Very high performance.
* **Easy**: Designed to be easy to use and learn.
* **Type-safe**: Automatic data validation using Python type hints.
* **Automatic Docs**: Swagger UI and ReDoc are auto-generated.
* **Async Ready**: Full support for asynchronous endpoints using `async/await`.

---

## 🧠 FastAPI Starter Code

### `main.py`

```python
from fastapi import FastAPI

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
```

---

## `requirements.txt`

```
fastapi
uvicorn
```

---

## How to Run

1. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

2. **Run the app**

   ```bash
   uvicorn main:app --reload
   ```

3. **Visit in browser:**

   * API: [http://localhost:8000](http://localhost:8000)
   * Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
   * ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## Example Response from `/hello/Alice`

```json
{
  "message": "Hello, Alice!"
}
```

---
