from src.models.city import City
from src.models.country import Country
from src.models.region import Region
from src.models.subregion import Subregion

ZOOM_LEVEL_TO_MODELS = {
    "city": City,
    "country": Country,
    "region": Region,
    "subregion": Subregion,
}
