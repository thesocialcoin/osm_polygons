from fastapi import FastAPI

from src import __version__


app = FastAPI(
    version=__version__
)


@app.get("/")
def home():
    return {"version": app.version}
