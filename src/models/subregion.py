from datetime import timedelta
from typing import Dict

from beanie import Document


class Subregion(Document):
    id: str  # OSM ID
    country_code: str  # ISO 3166 alpha-2
    type: str
    properties: Dict
    geometry: Dict

    class Settings:
        use_cache = True
        cache_expiration_time = timedelta(seconds=60)
