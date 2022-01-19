"""A sample package that uses `flit`"""

from fastapi import FastAPI


__version__ = "0.1"
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


def serve():
    import uvicorn
    uvicorn.run("flit_sample:app", host="0.0.0.0", port=8000, reload=True)
