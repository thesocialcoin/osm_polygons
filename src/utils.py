import json


def get_features_from_file(file: str, codes: str):
    with open(f"geojsons/{file}.json", "r") as file:
        all_features = json.load(file)

    features = {}
    for code in set(codes.split(",")):
        try:
            feature = all_features[code]
            features[code] = feature
        except KeyError:
            continue

    return features
