from typing import Dict

from beanie import Document


class City(Document):
    id: str  # OSM ID
    country_code: str  # ISO 3166 alpha-2
    type: str
    properties: Dict
    geometry: Dict
