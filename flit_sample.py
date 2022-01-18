"""Example package that uses `flit`"""

from fastapi import FastAPI


__version__ = "0.1"
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
