A **minimal working example** of using **GraphQL with FastAPI** in Python.

We’ll use:

* `FastAPI` (web framework)
* `Strawberry` (GraphQL library for Python that integrates smoothly with FastAPI)

---

### ✅ Final result

You’ll be able to query:

```graphql
query {
  hello(name: "Alice")
}
```

And get:

```json
{
  "data": {
    "hello": "Hello, Alice!"
  }
}
```

---

### 📁 Project Structure

```
fastapi_graphql_example/
├── main.py
```

---

## 🔧 1. Install dependencies

```bash
pip install fastapi uvicorn strawberry-graphql
```

---

## 🧠 2. `main.py` — FastAPI + GraphQL

```python
from fastapi import FastAPI
import strawberry
from strawberry.fastapi import GraphQLRouter

# Define the GraphQL schema
@strawberry.type
class Query:
    @strawberry.field
    def hello(self, name: str = "world") -> str:
        return f"Hello, {name}!"

# Create the Strawberry schema
schema = strawberry.Schema(Query)

# Create a GraphQL route
graphql_app = GraphQLRouter(schema)

# FastAPI app
app = FastAPI()

# Mount the GraphQL route
app.include_router(graphql_app, prefix="/graphql")
```

---

## ▶️ 3. Run the server

```bash
uvicorn main:app --reload
```

Visit:

```
http://localhost:8000/graphql
```

You’ll see the **GraphiQL playground**, where you can run GraphQL queries interactively.

---

### ✅ Example Query

```graphql
{
  hello(name: "Bob")
}
```

Result:

```json
{
  "data": {
    "hello": "Hello, Bob!"
  }
}
```


