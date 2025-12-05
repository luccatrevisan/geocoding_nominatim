# Geocoding with Nominatim

Convert addresses to geographic coordinates (latitude/longitude) using the Nominatim API (OpenStreetMap).

## How to Use
```bash
python geocoding.py
```

Enter an address when prompted and receive the coordinates.

### Example
```
Address: Copacabana, Rio de Janeiro, Brazil
Latitude: -22.9719740
Longitude: -43.1842997
```

## What is Nominatim?
Free geocoding API from OpenStreetMap. No API key required.
Documentation: https://nominatim.org/release-docs/latest/api/Search/

## Versions
- **v0.1.0**: Basic functional version
- **v0.2.0**: Added try/except for validation
- **v0.3.0**: Support for structured query parameters
