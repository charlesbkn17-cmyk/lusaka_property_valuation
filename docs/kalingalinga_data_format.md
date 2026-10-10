# Kalingalinga data requirements

This file documents the expected data structure for the Kalingalinga valuation-gap workflow.

## 1. Valuation roll CSV

The valuation roll must contain at least the following columns:

```csv
property_id,latitude,longitude,valuation_value,property_type,land_area,building_area
KAL_01,-15.3950,28.3230,760000,Residential,320,190
KAL_02,-15.3960,28.3245,820000,Residential,350,210
```

## 2. Building footprints GeoJSON

The building footprint file should include polygon geometries representing all mapped buildings in the study area.

## 3. Amenity data GeoJSON

The amenity file should include point features such as schools, markets, hospitals, roads, and bus stops.

## 4. Expected Kalingalinga result

The project expects to identify a total number of mapped properties greater than the number recorded in the valuation roll. In the sample scenario:

```text
Recorded properties = 12
Mapped properties = 19
Missing properties = 7
```

This demonstrates that the system can show more than 12 properties in Kalingalinga when spatial mismatch analysis is applied.
