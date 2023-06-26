//index.js

import cities from './geojson/cities.json'
import countries from './geojson/countries.json'
import regions from './geojson/regions.json'
import subregions from './geojson/subregions.json'

export function getCityPolygon(code) {
    try {
        return cities[code]
    } catch {
        return {}
    }
}

export function getCountryPolygon(code) {
    try {
        return countries[code]
    } catch {
        return {}
    }
}

export function getRegionPolygon(code) {
    try {
        return regions[code]
    } catch {
        return {}
    }
}

export function getSubregionPolygon(code) {
    try {
        return subregions[code]
    } catch {
        return {}
    }
}
