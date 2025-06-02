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
