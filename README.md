# OSM Polygons

This service helps all Front End services to recover polygons of the map's regions.

## 💿 Format of the data

### Countries

The country [codes](https://restcountries.com/v3.1/independent?status=true&fields=name,cca2,languages) follows the [ISO 3166](https://www.iso.org/iso-3166-country-codes.html) international standard and they are formatted as an Alpha-2 code.

## 🛠 Build and run the code

To build the code you can use the following command:
```bash
docker-compose build
```

To run it:
```bash
docker-compose up
```

## 🔌 API

### `/polygons`

- Parameters

    - `zoom_level`
        The zoom level of the features (choices are country, region, subregion and city)
    - `country_codes`
        List of country codes of the features you want
    
    Example: `/polygons?zoom_level=country&country_codes=ES,FR`

- Returns

    An object of features with key being the code of the polygon and the value the features itself

### `/add_polygon`

- Parameters

    - `zoom_level`
        The zoom level of the features (choices are country, region, subregion and city)
    - `code`
        Code of the feature you want to add to the DB
    
    Example: `/add_polygon?zoom_level=country&code=R127534`

- Returns

    The feature related to the code.
