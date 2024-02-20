from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from .provider.weather import service

app = FastAPI()


@app.get("/temperature")
def get_temperature(city: str, days: int):
    try:
        temperature = service.get_temperature(city, days)
        return JSONResponse(content={"temperature": temperature})
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/rain")
def will_rain(city: str, days: int):
    try:
        rain = service.will_rain(city, days)
        return JSONResponse(content={"will_rain": rain})
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
