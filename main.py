from typing import Union

from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/temperature") #what will be the temperature in Lisbon in 3 days?
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/rain") #Will it rain in Lisbon in 3 days?
def get_rain():
    return JSONResponse(content={"temperature": 30})
