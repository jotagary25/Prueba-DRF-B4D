### DOCUMENTACION

1. Tecnologías usadas:

   - python 3.12.2
   - postgresql: latest
   - docker
   - git
   - django

2. Despligue:

   - Tener docker instalado
   - ejecutar `docker compose up`
   - Aplicación ejecutandose en el puerto 8000
   - Base de datos ejecutandose en el puerto 8765

3. Enpoinds

   - Es posible ejecutar los endpoints desde la interfaz grafica **_/admin/_** con los usuarios y contraseñas indicados en el archivo **docker-compose.yml**, también estos valores pueden ser cambiados desde dicho archivo.
   - Los endpoinst también están sueltos y funcionan desde un gestor de peticiones como postman:
     1. GET, POST: **_/api/v1/blog/posts/_**
     2. PUT, PATCH, DELETE: **_/api/v1/blog/posts/#id_**

4. Anotaciones
   - Debido a la lentitud a la hora de levantar la base de datos en el primer despliegue se establecio un periodo de 30 segundos de retraso para la aplicación.
   - el archivo **config_script.py** se encarga de setear un usuario adminitrador inicial para acceder a traves de la ruta **_/admin/_**
   - las librerias necesarias para la construcción de la aplicación se encuentran en: **requirements.txt**
   - CORS habilitado
   - Las variables de entorno se pueden cambiar desde **docker-compose.yml**
