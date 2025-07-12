from fastapi import FastAPI 
from enum import Enum

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

app = FastAPI() 

@app.get("/")
async def root():
    return {"message": "Hello World"}

# @app.get("/items/{item_id}")
# async def read_item(item_id: int): # with type declaration , fast api gives us automatic request parsing
#     return {"item_id": item_id}

# http://127.0.0.1:8000/redoc
# http://127.0.0.1:8000/docs


@app.get("/users/me")
async def read_user_me(): 
    return {"user_id": "the current user"}

@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName): 
    if model_name is ModelName.alexnet: 
        return {"model_name": model_name, "message": "Deep Learning FTW"}
    if model_name is ModelName.resnet: 
        return {"model_name": model_name, "message": "LeCNN all the images"}
    if model_name.value == "lenet": 
        return {"model_name": model_name, "message": "leCNN all the images"}
    return {"model_name": model_name, "message": "Have some residuals"}


fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip+limit]

@app.get("/items/{item_id}") #here item_id is a path parameter and q is a query parameter
async def read_item(item_id: str, q: str|None = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}

@app.get("/things/{thing_id}")
async def read_things(thing_id: str, q: str | None = None , short: bool = False):
    thing = {"thing_id": thing_id}
    if q:
        thing.update({ "q": q })
    if not short: 
        thing.update({ "description": "This is an amazint thing" })
    return thing

#multiple path and query parameters

@app.get("/toms/{tom_id}/cat/{cat_id}")
async def read_kitten_profile(
    tom_id: int, cat_id: int, q:str | None = None, short: bool = False
):
    item = {"cat_id": cat_id, "owner_id": tom_id}
    if q: 
        item.update({ "q": q })
    if not short: 
        item.update(
            {"description" :"this is a long description"}
        )
    return item

@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}