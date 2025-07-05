import asyncio
import autenticar as auth
import extraer

if __name__ == "__main__":
    """
    Función principal
    Llama a la función 'buscar_tweets'
    """
    # Llaves de autenticación
    auth_token = "auth_token" # auth_token sacado del navegador
    ct0 = "ct0"        # ct0 sacado del navegador
    
    query = "búsqueda" # Palabra o hashtag a buscar
    cantidad = 5 # Número de tweets a extraer de 5 a 30
    
    # Crear un cliente autenticado con las llaves ingresadas
    cliente = auth.crear_cliente(auth_token, ct0)
    
    # Ejecutar el programa de forma asincrónica
    asyncio.run(extraer.buscar_tweets(cliente, query, cantidad))