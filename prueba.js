const fs = require('fs');
const path = require('path');

// Directorio donde se encuentran los archivos
const directory = 'E:/varidos';

// Obtener todos los archivos en el directorio
fs.readdir(directory, (err, files) => {
  if (err) {
      console.error('Error al leer el directorio:', err);
      return;
  }

  files.forEach(file => {
      // Verificar si el nombre del archivo comienza con caracteres que no sean letras
      if (/^[^a-zA-Z]+/.test(file)) {
          // Eliminar los caracteres no deseados al inicio del nombre del archivo
          const newName = file.replace(/^[^a-zA-Z]+/, '');
          // Renombrar el archivo
          fs.rename(path.join(directory, file), path.join(directory, newName), err => {
              if (err) {
                  console.error('Error al renombrar el archivo:', err);
              } else {
                  console.log(`Renombrado: ${file} -> ${newName}`);
              }
          });
      }
  });
});
