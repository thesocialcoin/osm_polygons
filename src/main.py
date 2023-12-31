from fastapi import FastAPI, Request, Response, status
from fastapi.middleware.cors import CORSMiddleware

from src import __version__
from src.settings import init_db
from src.utils import get_features_from_db, get_feature_from_nominatim
from src.validators import authenticate, validate_zoom_level


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
async def polygons(zoom_level: str, codes: str, request: Request):
    authenticate(request)

    validate_zoom_level(zoom_level)

    return await get_features_from_db(zoom_level, codes)


@app.post("/add_polygon", status_code=201)
async def add_polygon(zoom_level: str, code: str, request: Request, response: Response):
    authenticate(request)

    validate_zoom_level(zoom_level)

    feature, from_db = await get_feature_from_nominatim(zoom_level, code)

    if from_db:
        response.status_code = status.HTTP_200_OK

    return feature
