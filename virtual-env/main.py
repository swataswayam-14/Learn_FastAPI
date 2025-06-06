from fastapi import FastAPI #FastAPI is a class that inherits directly from Starlette

app = FastAPI() # app is a FastAPI instance

@app.get("/")
async def root():
    return {"message": "Hello World"}

#Path : (endpoint / route)
# "Path" here refers to the last part of the URL starting from the first /.
# URL : https://example.com/items/foo, path: "/items/foo"


# http://127.0.0.1:8000/
# http://127.0.0.1:8000/docs : interactive API doc by Swagger UI
# http://127.0.0.1:8000/redoc : alternative automatic documentation (provided by ReDoc
# FastAPI automatically generates a JSON (schema) with the descriptions of all your API : http://127.0.0.1:8000/openapi.json


#in OPEN API (HTTP Methods (GET, POST, PUT, DELETE)) are called Operations

#@something : is a decorator , tells FastAPI that the function below corresponds to the path / with an operation get/put etc