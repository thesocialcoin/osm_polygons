from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src import __version__
from src.settings import init_db
from src.utils import get_features_from_file, get_feature_from_nominatim
from src.validators import validate_zoom_level


app = FastAPI(version=__version__)

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_headers=["*"],
    allow_methods=["*"],
    allow_origins=["*"],
)


@app.on_event("startup")
async def start_db():
    await init_db()


@app.get("/")
def home():
    return {"version": app.version}


@app.get("/polygons")
def polygons(zoom_level: str, country_codes: str = ""):
    validate_zoom_level(zoom_level)

    return get_features_from_file(zoom_level, country_codes)


@app.post("/add_polygon")
def add_polygon(zoom_level: str, country_code: str):
    validate_zoom_level(zoom_level)

    return get_feature_from_nominatim(zoom_level, country_code)
