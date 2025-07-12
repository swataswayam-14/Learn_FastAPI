from fastapi import FastAPI , Query
from enum import Enum
from pydantic import BaseModel, AfterValidator
from typing import Annotated
import random

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

data = {
    "isbn-9781529046137": "The Hitchhiker's Guide to the Galaxy",
    "imdb-tt0371724": "The Hitchhiker's Guide to the Galaxy",
    "isbn-9781439512982": "Isaac Asimov: The Complete Stories, Vol. 2",    
}

def check_valid_id(id: str):
    if not id.startswith(("isbn-", "imdb-")):
        raise ValueError('Invalid ID format, it must start with isbn- or imdb-')
    return id

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

@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax is not None: 
        price_with_tax = item.price + item.tax
        item_dict.update({ "price with tax": price_with_tax })
    return item_dict

# @app.put("/items/{item_id}")
# async def create_item(item: Item, item_id: int):
#     item_dict = item.dict()
#     item_dict.update( {"item_id" : item_id} )
#     if item.tax is not None:  
#         price_with_tax = item.price + item.tax
#         item_dict.update({ "price with tax": price_with_tax })
#     return item_dict

@app.put("/items/{item_id}")
async def update_item(item: Item, item_id: int, q: str | None = None, short: bool | None = False):
    item_dict = item.dict()
    item_dict.update({"item_id": item_id})
    if short is False:
        item_dict.update({"long_description": "this is a long description"})
    if q:
        item_dict.update({"q":q})
    return item_dict

# If the parameter is of a singular type (like int, float, str, bool, etc) it will be interpreted as a query parameter.
# If the parameter is declared to be of the type of a Pydantic model, it will be interpreted as a request body.





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

@app.get("/jinsa/")
async def read_items(q: Annotated[str | None, Query(max_length=50)] = None):
    results = {
        "items":[
            {"item_id": "foo"},
            {"item_id": "bar"}
        ]
    }
    if q: 
        results.update({"q": q})
    return results

# q: str | None = None ===>  q: Annonated[str|None] = None


#older versions had Query as the default value of the parameter, instead of putting it in Annotated

@app.get("/pariba")
async def get_pariba(q: str | None = Query(default=None, max_length=50)):
    results = {
        "pariba": [
            {"baigana": "10kg"},
            {"tomato": "20kg"}
        ]
    }
    if q:
        results.update({ "q": q})
    return results

@app.get("/rook")
async def more_parameters (q: Annotated[str | None, Query(min_length=3, max_length= 50)] = None):
    results = {"item1": "bhendi", "item2": "alu"}
    if q:
        results.update({"q":q})
    return results

@app.get("/rookie")
async def regular_expressions (q: Annotated[str | None, Query(min_length=3, max_length= 50, pattern="^fixedquery$")] = None):
    results = {"item1": "bhendi", "item2": "alu"}
    if q:
        results.update({"q":q})
    return results

#pattern was previously called regex , now its deprecated

@app.get("/horse")
async def regular_expressions (q: Annotated[str | None, Query(min_length=3, max_length= 50)] = "fixedquery"):
    results = {"item1": "bhendi", "item2": "alu"}
    if q:
        results.update({"q":q})
    return results

# Query parameter list / multiple values
#here we need to explicitly use Query, otherwise it would be interpreted as a Request Body
@app.get("/multiplequery")
async def read_item(q: Annotated[list[str] | None , Query()] = None):
    query_items = {"q": q}
    return query_items

@app.get("/mwd")
async def read_item(q: Annotated[list[str] | None , Query()] = ["foo", "bar"]):
    query_items = {"q": q}
    return query_items

#declaring more metadata
@app.get("/meta")
async def read_item(q: Annotated[str | None, Query(title="This is a metadata of what the query is", description="query is querying")]=None):
    if q:
        return {"item_id": "item1", "q": q}
    return {"item_id": "foo"}

#alias parameter
#item-query is not a valid Python variable name, but we want it so....
@app.get("/alias/example")
async def read_items(q: Annotated[str|None, Query(alias="item-query")] = None):
    results = {"items": 1}
    if q:
        results.update({"q": q})
    return results

#if a parameter is depricaiated but used my clients , to show that its depricated: 

@app.get("/depriciated/param/example")
async def read_items( q: Annotated[str|None, Query(alias="item-query", title="Query string", description="query string for searching item in the DB",min_length=3, max_length=50, deprecated=True)] = None):
    results = {"items": [{"item1": "1"}, {"item2": "2"}]}
    if q:
        results.update({"q":q})
    return results

# Exclude parameters from OpenAPI

@app.get("/random")
async def read_items(hidden_query: Annotated[str | None, Query(include_in_schema=False)] = None):
    if hidden_query:
        return {"hidden_querry": hidden_query}
    else:
        return {"hidden_query": "Not found"}
    

# Custom Validation
@app.get("/custom/validator/example")
async def read_items( id: Annotated[str | None, AfterValidator(check_valid_id)] = None):
    if id: 
        item = data.get(id)
    else:
        id, item = random.choice(list(data.items()))
    return {"id":id, "name": item}