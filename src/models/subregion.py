from typing import Dict

from beanie import Document, Indexed


class Subregion(Document):
    id: str  # OSM ID
    country_code: Indexed(str)  # ISO 3166 alpha-2
    type: str
    properties: Dict
    geometry: Dict
