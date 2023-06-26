//index.js

import cities from './geojson/cities.json'
import countries from './geojson/countries.json'
import regions from './geojson/regions.json'
import subregions from './geojson/subregions.json'

function getCityPolygon(code) {
    try {
        return cities[code]
    } catch {
        return {}
    }
}

function getCountryPolygon(code) {
    try {
        return countries[code]
    } catch {
        return {}
    }
}

function getRegionPolygon(code) {
    try {
        return regions[code]
    } catch {
        return {}
    }
}

function getSubregionPolygon(code) {
    try {
        return subregions[code]
    } catch {
        return {}
    }
}

export default {
    getCityPolygon,
    getCountryPolygon,
    getRegionPolygon,
    getSubregionPolygon
}
