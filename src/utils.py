import json
import requests

from fastapi import HTTPException

from osm_mapping import countries

from src.settings import settings


def get_features_from_file(zoom_level: str, codes: str):
    with open(f"geojsons/{zoom_level}.json", "r") as file:
        all_features = json.load(file)

    features = {}
    for code in set(codes.split(",")):
        if zoom_level == "country":
            try:
                feature = all_features[code.upper()]
                features[code.upper()] = feature
            except KeyError:
                continue
        else:
            try:
                for key, value in all_features[code.upper()].items():
                    features[key] = value
            except KeyError:
                continue

    return features


def get_feature_from_nominatim(zoom_level: str, code: str):
    if zoom_level == "country":
        osm_id = countries.get_osm_id(code)
        osmtype, osmid = osm_id[0], osm_id[1:]
    else:
        osmtype, osmid = code[0], code[1:]

    endpoint = settings.nominatim_endpoint
    parameters = f"?osmtype={osmtype}&osmid={osmid}&polygon_geojson=1&format=json"
    response = requests.get(endpoint + parameters)
    if response.status_code == 200:
        osm_polygon = response.json()
    elif response.status_code == 400:
        raise HTTPException(status_code=400)

    feature = format_geojson(osm_polygon)
    country = feature["properties"]["country_code"].upper()

    with open(f"geojsons/{zoom_level}.json", "r") as file:
        all_features = json.load(file)

    if zoom_level == "country":
        if code not in all_features.keys():
            all_features[code] = feature
        else:
            print("OUT!")
            return
    else:
        country_features = all_features.get(country, {})
        if code not in country_features.keys():
            country_features[code] = feature
        else:
            print("OUT!")
            return

        all_features[country] = country_features

    with open(f"geojsons/{zoom_level}.json", "w") as file:
        json.dump(all_features, file, ensure_ascii=False, indent=2)

    return feature


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
