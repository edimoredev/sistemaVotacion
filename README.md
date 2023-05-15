# votaciones

# Descripción Proyecto

1. Se deberá crear un sistema votaciones donde se deberá registrar la información
de los votantes tales como Nombre, Apellidos, Tipo de documento, No de
documento, Género y Localidad.

2. Se deberá registrar los candidatos en un formulario donde se deberá guardar la
información del candidato, el partido y la localidad

3. Una vez registrado los votantes y los candidatos se deberá registrar en una vista el
voto donde se deberá ingresar el votante y el candidato por el cual votará, para
votar se deben cumplir también las siguientes restricciones:

a) Deben existir tanto el votante como el Candidatos ingresados.
b) El votante no podrá realizar el voto por un candidato de una localidad diferente.
c) Un votante no podrá realizar más de un voto.

# Arquitectura del proyecto

- Version python: Python 3.10.6
- Entorno virtual: virtualenv 20.16.3
- Nombre del Proyecto: votaciones
  - Version Django: Django 4.2.1
  - psycopg2 2.9.6 --> base de datos postgres
  - Archivo requirements.txt: Contenido de las librerias utilizadas

Nota: 
* El proyecto se crea con una base de datos POSTGRES, nombre de la base de datos "sistemavotaciones".
* Se crea una carpeta con nombre mermaiddb, la cual contiene el MER y el DER, de la base de datos
* se deben realizar las migraciones pertinentes, ya que se creo los modelos para cada vista, revisar la sección "Docker"


url vista registro: http://localhost:8000/

![image](https://github.com/edmoredev/sistemaVotacion/assets/125479887/49ee5f2c-e7c2-478f-911e-52e18b617663)

url vista votar:http://localhost:8000/votar/
![image](https://github.com/edmoredev/sistemaVotacion/assets/125479887/7798cd30-88a6-4a06-9b33-4597623123bd)



#Docker

* Para este proyecto se realiza los campos de Tipo Documento, genero y localidad normalizadas, lo cual se agrega los siguientes datos desde el administrador de Django, por tal motivo se debe crear el superUser y agregar la información para la vista de la siguiente manera

![image](https://github.com/edmoredev/sistemaVotacion/assets/125479887/aefa164d-52ad-4dd1-a52e-5d6b7c0a9e0d)


Genero:
* Femenino
* Masculino

TipoDocumento:
* Cedula de ciudadanía
* Cédula de extranjería

Localidad:
A
B
C
D
E

Antes de registrar debemos crear el superusuario
ingresa el siguiente comando 
- docker ps, para saber el nombre del proyecto docker

![image](https://github.com/edmoredev/sistemaVotacion/assets/125479887/e541cf44-40cf-441d-b15d-75ed79e7d33d)


ejecutamos
- docker exec -it nombre del doker /bin/sh

![image](https://github.com/edmoredev/sistemaVotacion/assets/125479887/16eec3fd-a9fe-4b56-9515-f5e50620b95b)

- python manage.py createsuperuser

Ingresamos los datos de usuario, correo y password
![image](https://github.com/edmoredev/sistemaVotacion/assets/125479887/fe898b3c-b522-46f9-9e5b-b3ee4a09685e)

Después de las migraciones

- python manage.py migrate






