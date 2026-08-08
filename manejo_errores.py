import requests
import time

def manejar_respuesta(respuesta):
    """
    Función para procesar y evaluar los códigos de estado HTTP devueltos por el servidor.
    """
    codigo = respuesta.status_code
    print(f"\n[HTTP Status: {codigo}]")

   
    if codigo in [200, 201]:
        print("-> Éxito: La solicitud fue procesada correctamente.")
        try:
            datos = respuesta.json()
            print(f"   Datos recibidos: {datos}")
        except ValueError:
            print("   Respuesta del servidor procesada correctamente (sin cuerpo JSON).")

   
    elif codigo == 400:
        print("-> Error (400): Solicitud incorrecta. Verifique la sintaxis o los parámetros enviadas al servidor.")

  
    elif codigo == 401:
        print("-> Error (401): No autorizado. Se requieren credenciales de acceso o una API Key válida.")

   
    elif codigo == 404:
        print("-> Error (404): Recurso no encontrado. La URL consultada no existe en el servidor.")

   
    elif codigo == 429:
        
        espera = respuesta.headers.get("Retry-After", "5")
        print(f"-> Error (429): Demasiadas peticiones. Has superado el límite de tasa. Esperar {espera} segundos.")


    elif codigo == 500:
        print("-> Error (500): Error interno del servidor. El servidor remoto encontró una condición inesperada.")

    else:
        print(f"-> Código de estado HTTP no contemplado: {codigo}")


def probar_url(url, descripcion, timeout=5):
    """
    Función auxiliar para realizar peticiones GET y capturar excepciones de red.
    """
    print("\n" + "=" * 60)
    print(f" PRUEBA: {descripcion}")
    print(f" URL: {url}")
    print("=" * 60)

    try:
        respuesta = requests.get(url, timeout=timeout)
        manejar_respuesta(respuesta)

    except requests.exceptions.ConnectionError:
        print("-> Error de Conexión (ConnectionError): No se pudo establecer comunicación con el servidor. Verifique la red.")

    except requests.exceptions.Timeout:
        print(f"-> Error de Tiempo de Espera (Timeout): La solicitud excedió el tiempo límite configurado ({timeout}s).")

    except requests.exceptions.RequestException as e:
        print(f"-> Excepción de red inesperada: {e}")


def main():
    print("=== DEMOSTRACIÓN Y PRUEBA DE MANEJO DE ERRORES HTTP ===")

    
    probar_url("https://httpbin.org/status/200", "Petición Exitosa (200 OK)")
    probar_url("https://httpbin.org/status/201", "Recurso Creado (201 Created)")
    probar_url("https://httpbin.org/status/400", "Bad Request (400)")
    probar_url("https://httpbin.org/status/401", "Unauthorized (401)")
    probar_url("https://httpbin.org/status/404", "Not Found (404)")
    probar_url("https://httpbin.org/status/429", "Too Many Requests (429)")
    probar_url("https://httpbin.org/status/500", "Internal Server Error (500)")


    probar_url("https://httpbin.org/delay/3", "Prueba de Excepción: Timeout", timeout=1)


    probar_url("https://dominio-falso-inexistente-12345.org", "Prueba de Excepción: ConnectionError")


if __name__ == "__main__":
    main()