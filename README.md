# Geocoding com Nominatim

Converte endereços em coordenadas (latitude/longitude) usando a API Nominatim (OpenStreetMap).

## Como usar
```bash
python geocoding.py
```

Digite um endereço quando solicitado e receba as coordenadas.

### Exemplo
```
Endereço: Copacabana, Rio de Janeiro, Brasil
Latitude: -22.9719740
Longitude: -43.1842997
```

## O que é Nominatim?

API gratuita do OpenStreetMap para geocoding. Sem API key necessária.

Documentação: https://nominatim.org/release-docs/latest/api/Search/

## Versões

- **v0.1.0**: Versão básica funcional
- **v0.2.0**: Adicionado try/except para validação
- **v0.3.0**: Suporte a parâmetros estruturados
```