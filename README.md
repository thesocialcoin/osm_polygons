# OSM Polygons

This service helps all Front End services to recover polygons of the map's regions.

## 💿 Format of the data

### Countries

The country [codes](https://restcountries.com/v3.1/independent?status=true&fields=name,cca2,languages) follows the [ISO 3166](https://www.iso.org/iso-3166-country-codes.html) international standard and they are formatted as an Alpha-2 code.

## 🛠 Build and run the code

- Set up the environment variables:

    ```bash
    cp .env.default .env
    ```

    [Go to the file](.env) and fill the environment variables described there.

- Build the code you can use the following command:
    ```bash
    docker-compose build
    ```

- Run the code with the following command:
    ```bash
    docker-compose up
    ```

## 🔌 API Documentation

For a fully detailed API documentation, you can go to [this URL](http://localhost:6500/docs).
