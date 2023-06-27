from fastapi import HTTPException


ZOOM_LEVEL_CHOICES = (
    "country",
    "region",
    "subregion",
    "city"
)


def validate_zoom_level(zoom_level: str) -> None:
    if zoom_level not in ZOOM_LEVEL_CHOICES:
        raise HTTPException(
            status_code=400,
            detail=f"'zoom_level' must be one of these choices: {ZOOM_LEVEL_CHOICES}"
        )
