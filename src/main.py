from fastapi import FastAPI

from src import __version__
from src.utils import get_features_from_file
from src.validators import validate_zoom_level


app = FastAPI(
    version=__version__
)


@app.get("/")
def home():
    return {"version": app.version}


@app.get("/polygons")
def polygons(zoom_level: str, codes: str = ""):
    validate_zoom_level(zoom_level)

    return get_features_from_file(zoom_level, codes)
