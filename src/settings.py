from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseSettings

import sentry_sdk


class Settings(BaseSettings):
    nominatim_endpoint: str = "http://nominatim.ctb.internal/details"
    sentry_traces_sample_rate: float = 0


settings = Settings()


sentry_sdk.init(
    dsn="https://d579829e2ab94aaf80e043fd0e82efba@issues.citibeats.com/29",
    traces_sample_rate=settings.sentry_traces_sample_rate
)


async def init_db():
    client = AsyncIOMotorClient("mongodb://root:secret@db:27017")

    await init_beanie(
        database=client.polygons,
        document_models=[
            # Insert here the models
            "src.models.city.City",
            "src.models.country.Country",
            "src.models.region.Region",
            "src.models.subregion.Subregion",
        ],
    )
