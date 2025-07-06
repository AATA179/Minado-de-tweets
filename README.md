# Minado de tweets
Este proyecto permite la extracción de tweets usando autenticación por cookies.

## Estructura del proyecto
```
MinadoTweets/
├── main.py       # Flujo principal del programa
├── autenticar.py # Crea un cliente autenticado con las cookies ingresadas
├── extraer.py    # Busca tweets con un 'query' ingresado y los extrae con ayuda de la biblioteca -twikit-
├── guardar.py    # Guarda los tweets extraidos en un archivo .JSON
```

## Requisitos
- Python 3.13 o superior
- Biblioteca twikit

## Funcionalidades
- Extracción de tweets recientes usando twikit (sin necesidad de la API X)
- Almacenamiento estructurado en archivos .json
- Soporte para búsquedas por palabra clave

## Ejemplo de formato de guardado de los tweets
```
{
  "Fecha": "2025-07-06 12:12:12",
  "Usuario": "@aata179",
  "Contenido": "Texto dentro del tweet",
  "Tema": "Ejemplo"
},
```

## Limitaciones
- La cuenta de X con la que se sacaron las cookies puede quedar limitada (bloqueo de ciertas funciones dentro de X, como publicar o reaccionar a publicaciones)
- El programa puede correrse una vez cada 15 minutos
- Twikit puede generar bloqueos temporales en la cuenta de X si se hacen muchas consultas seguidas

## NOTA
Este código es de uso académico y fue probado en entornos controlados. Se recomienda revisar las políticas de uso de X antes de tratar de realizar una extracción masiva de datos.
