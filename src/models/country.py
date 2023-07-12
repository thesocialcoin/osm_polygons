from typing import Dict

from beanie import Document


class Country(Document):
    id: str  # osm_id
    type: str
    properties: Dict
    geometry: Dict
