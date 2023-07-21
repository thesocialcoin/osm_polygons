import requests

from beanie.operators import In
from fastapi import HTTPException

from osm_mapping import countries

from src.models.country import Country
from src.models.utils import ZOOM_LEVEL_TO_MODELS
from src.settings import settings


async def get_features_from_db(zoom_level: str, country_codes: str):
    splitted_codes = country_codes.split(",")
    if zoom_level == "country":
        features = await Country.find(
            In(Country.id, splitted_codes)
        ).to_list()
    else:
        model = ZOOM_LEVEL_TO_MODELS[zoom_level]
        features = await model.find(
            In(model.country_code, splitted_codes)
        ).to_list()

    return {feature.id: feature for feature in features}


async def get_feature_from_nominatim(zoom_level: str, code: str):
    model = ZOOM_LEVEL_TO_MODELS[zoom_level]
    if feature := await model.get(code):
        return feature, True

    if zoom_level == "country":
        osm_id = countries.get_osm_id(code)
        osmtype, osmid = osm_id[0], osm_id[1:]
    else:
        osmtype, osmid = code[0], code[1:]

    osm_polygon = get_osm_polygon(osmtype, osmid)
    feature = format_geojson(osm_polygon)

    country = feature["properties"]["country_code"].upper()
    new_polygon = model(id=code, country_code=country, **feature)
    await new_polygon.create()

    return new_polygon, False


def get_osm_polygon(osmtype: str, osmid: str):
    endpoint = settings.nominatim_endpoint
    query_params = f"?osmtype={osmtype}&osmid={osmid}&polygon_geojson=1&format=json"
    response = requests.get(endpoint + query_params)

    if not response.ok:
        raise HTTPException(status_code=400)

    return response.json()


def format_geojson(osm_polygon: dict):
    geojson = {
        'type': 'Feature',
        'properties': osm_polygon,
        'geometry': osm_polygon.pop('geometry'),
    }

    geojson['properties']['place_id'] = '{}{}'.format(
        geojson['properties']['osm_type'],
        geojson['properties']['osm_id']
    )

    return geojson
