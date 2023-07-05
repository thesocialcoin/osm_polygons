from pydantic import BaseSettings

import sentry_sdk


class Settings(BaseSettings):
    nominatim_endpoint: str
    sentry_traces_sample_rate: float = 0


settings = Settings()


sentry_sdk.init(
    dsn="https://d579829e2ab94aaf80e043fd0e82efba@issues.citibeats.com/29",
    traces_sample_rate=settings.sentry_traces_sample_rate
)
