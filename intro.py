"""Introducción a Python"""

import os
import re

# Directorio donde se encuentran los archivos
directory = "E:/variado"

# Recorrer todos los archivos en el directorio
for filename in os.listdir(directory):
    # Verificar si el nombre del archivo comienza con la forma '(001) -'
    if re.match(r'^\(\d{3}\) -', filename): # \(*\d+\)*[\s-_]+
        # Eliminar los caracteres '(001) -' al inicio del nombre del archivo
        new_name = re.sub(r'^\(\d{3}\) -', '', filename)
        # Renombrar el archivo
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))

print("Renombrado completado.")
""" 
# Recorrer todos los archivos en el directorio
for filename in os.listdir(directory):
    # Verificar si el nombre del archivo comienza con caracteres en blanco
    if filename.startswith(' '):
        # Eliminar los caracteres en blanco al inicio del nombre del archivo
        new_name = filename.lstrip()
        # Renombrar el archivo
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))

print("Renombrado completado.")



# Recorrer todos los archivos en el directorio
for filename in os.listdir(directory):
    # Verificar si el nombre del archivo comienza con '_'
    if filename.startswith('_'):
        # Eliminar el guion bajo al inicio del nombre del archivo
        new_name = filename.lstrip('_')
        # Renombrar el archivo
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))

print("Renombrado completado.")

# Recorrer todos los archivos en el directorio
for filename in os.listdir(directory):
    # Verificar si el nombre del archivo comienza con '_'
    if filename.startswith('. '):
        # Eliminar el guion bajo al inicio del nombre del archivo
        new_name = filename.lstrip('. ')
        # Renombrar el archivo
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))

print("Renombrado completado.")

# Recorrer todos los archivos en el directorio
for filename in os.listdir(directory):
    # Verificar si el nombre del archivo comienza con la forma '(001) -'
    if re.match(r'^\d{1} -', filename):
        # Eliminar los caracteres '(001) -' al inicio del nombre del archivo
        new_name = re.sub(r'^\(\d{3}\) -', '', filename) # r'^\(\d{3}\) -'
        # Renombrar el archivo
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))

print("Renombrado completado.")


 """