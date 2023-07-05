import json

from fastapi import HTTPException


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
    raise HTTPException(status_code=418)
