import requests


BASE_URL = "https://jsonplaceholder.typicode.com/posts"

def mostrar_separador(titulo):
    print("\n" + "=" * 50)
    print(f" {titulo}")
    print("=" * 50)

def main():

    mostrar_separador("1. OPERACIÓN GET - Obtener los primeros 2 posts")
    try:
        response = requests.get(BASE_URL, timeout=10)
        response.raise_for_status()  
        
        print(f"Código de estado: {response.status_code}")
        posts = response.json()[:2]  
        
        for post in posts:
            print(f"\n[ID: {post['id']}]")
            print(f"Título: {post['title']}")
            print(f"Cuerpo: {post['body']}")
            
    except requests.exceptions.Timeout:
        print("Error: La solicitud GET superó el tiempo de espera.")
    except requests.exceptions.ConnectionError:
        print("Error: No se pudo conectar con el servidor.")
    except requests.exceptions.HTTPError as http_err:
        print(f"Error HTTP en GET: {http_err}")
    except Exception as err:
        print(f"Ocurrió un error inesperado en GET: {err}")

    
    mostrar_separador("2. OPERACIÓN POST - Crear un nuevo post")
    nuevo_post = {
        "title": "Práctica Automatización Digital I",
        "body": "Ejecutando operaciones CRUD con la librería requests en Python.",
        "userId": 1
    }
    
    try:
        response = requests.post(BASE_URL, json=nuevo_post, timeout=10)
        response.raise_for_status()
        
        datos_respuesta = response.json()
        print(f"Código de estado: {response.status_code}")
        print("¡Post creado exitosamente en el servidor!")
        print(f"ID Generado: {datos_respuesta.get('id')}")
        print(f"Respuesta completa: {datos_respuesta}")
        
    except requests.exceptions.RequestException as err:
        print(f"Error en la petición POST: {err}")


    mostrar_separador("3. OPERACIÓN PUT - Actualizar el post con ID 1")
    url_post_1 = f"{BASE_URL}/1"
    datos_actualizados = {
        "id": 1,
        "title": "Título Actualizado - Examen 3er Parcial",
        "body": "Se ha modificado el contenido del post ID 1 mediante petición PUT.",
        "userId": 1
    }
    
    try:
        response = requests.put(url_post_1, json=datos_actualizados, timeout=10)
        response.raise_for_status()
        
        print(f"Código de estado: {response.status_code}")
        print("¡Post ID 1 actualizado correctamente!")
        print(f"Respuesta del servidor: {response.json()}")
        
    except requests.exceptions.RequestException as err:
        print(f"Error en la petición PUT: {err}")


    mostrar_separador("4. OPERACIÓN DELETE - Eliminar el post con ID 1")
    try:
        response = requests.delete(url_post_1, timeout=10)
        response.raise_for_status()
        
        print(f"Código de estado: {response.status_code}")
        if response.status_code in [200, 204]:
            print("¡Éxito! El post con ID 1 fue eliminado satisfactoriamente.")
        print(f"Respuesta del servidor (Cuerpo): {response.json()}")
        
    except requests.exceptions.RequestException as err:
        print(f"Error en la petición DELETE: {err}")

if __name__ == "__main__":
    main()