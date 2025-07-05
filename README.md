# Minado de tweets
Este proyecto permite la extracción de tweets usando autenticación por cookies.

## Estructura del proyecto
MinadoTweets/
├── main.py       # Flujo principal del programa
├── autenticar.py # Crea un cliente autenticado con las cookies ingresadas
├── extraer.py    # Busca tweets con un 'query' ingresado y los extrae con ayuda de la biblioteca -twikit-
├── guardar.py    # Guarda los tweets extraidos en un archivo .JSON

## Requisitos
- Python 3.13 o superior
- Biblioteca twikit

## Funcionalidades
- Extracción de tweets recientes usando twikit (sin necesidad de la API X)
- Almacenamiento estructurado en archivos .json
- Soporte para búsquedas por palabra clave
