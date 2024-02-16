from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get("/temperature")  # what will be the temperature in Lisbon in 3 days?
def get_temperature():
    return JSONResponse(content={"temperature": 30})


@app.get("/rain")  # Will it rain in Lisbon in 3 days?
def get_rain():
    return JSONResponse(content={"rain": 30})
