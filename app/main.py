from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from .provider.weather import service

app = FastAPI()


@app.get("/temperature")
def get_temperature(city: str, days: int):
    temperature = service.get_temperature(city, days)
    try:
        return JSONResponse(
            content={
                "temperature": temperature,
            }
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/rain")
def will_rain():
    return JSONResponse(content={"rain": True})
