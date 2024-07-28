import requests
import json
import time

# Configuración de la URL y los parámetros
url = "http://159.65.116.223:5000/post"
serial = "1990002923045"
name = "jsonFILE"

# Crear el archivo JSON de ejemplo
data = {
    "key1": "value1",
    "key2": "value2"
}
json_filename = "test.json"
with open(json_filename, 'w') as json_file:
    json.dump(data, json_file)

# Preparar los parámetros de la consulta
params = {
    "Serial": serial,
    "Name": name
}

# Preparar los archivos para la solicitud
files = {
    "file": (json_filename, open(json_filename, 'rb'), 'application/json')
}

# Realizar la solicitud POST
response = requests.post(url, params=params, files=files)

# Verificar la respuesta del servidor
if response.status_code == 200:
    print("Proceso exitoso, archivo guardado en la base de datos.")
elif response.status_code == 400:
    print("Error en los parámetros, datos inválidos.")
else:
    print(f"Error desconocido: {response.status_code}")
