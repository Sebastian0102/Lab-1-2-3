import os
import requests
from dotenv import load_dotenv


load_dotenv()


API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def obtener_clima(ciudad):
    
    if not API_KEY or API_KEY == "tu_clave_aqui":
        print("Error: No se ha configurado una API_KEY válida en el archivo .env")
        return

    
    params = {
        "q": ciudad,
        "appid": API_KEY,
        "units": "metric",  
        "lang": "es"       
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        
        
        if response.status_code == 200:
            datos = response.json()
            temp_actual = datos["main"]["temp"]
            sensacion = datos["main"]["feels_like"]
            descripcion = datos["weather"][0]["description"]
            nombre_ciudad = datos["name"]
            pais = datos["sys"]["country"]

            print("\n" + "=" * 45)
            print(f" CLIMA ACTUAL EN: {nombre_ciudad.upper()}, {pais}")
            print("=" * 45)
            print(f"Temperatura actual: {temp_actual}°C")
            print(f"Sensación térmica:  {sensacion}°C")
            print(f"Descripción:        {descripcion.capitalize()}")
            print("=" * 45)

        elif response.status_code == 404:
            print(f"\nError (404): La ciudad '{ciudad}' no fue encontrada. Verifique la ortografía.")
        elif response.status_code == 401:
            print("\nError (401): API Key inválida o no autorizada. Verifique su archivo .env.")
        else:
            print(f"\nError ({response.status_code}): {response.json().get('message', 'Error desconocido')}")

    except requests.exceptions.Timeout:
        print("\nError: La solicitud superó el tiempo de espera.")
    except requests.exceptions.ConnectionError:
        print("\nError: Fallo de conexión. Verifique su acceso a internet.")
    except Exception as e:
        print(f"\nOcurrió un error inesperado: {e}")

def main():
    print("--- CONSULTA DE CLIMA EN TIEMPO REAL ---")
    ciudad = input("Ingrese el nombre de la ciudad a consultar: ").strip()
    
    if ciudad:
        obtener_clima(ciudad)
    else:
        print("Error: Debe ingresar un nombre de ciudad válido.")

if __name__ == "__main__":
    main()