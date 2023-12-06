""" 
simple script to read a json and change its content
"""

import json

# Nombre del archivo JSON
archivo_json = 'database.json'

# Abrir el archivo en modo lectura
with open(archivo_json, 'r') as file:
    # Cargar el contenido del archivo JSON en un diccionario
    data = json.load(file)

    print(data)


# Realizar alguna manipulación en el diccionario (por ejemplo, cambiar un valor)
data['instruction'] = False

# Abrir el archivo en modo escritura
with open(archivo_json, 'w') as file:
    # Escribir el diccionario modificado de nuevo al archivo JSON
    json.dump(data, file, indent=4)

print(f'Contenido del archivo {archivo_json} modificado con éxito.')
