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
![image](https://github.com/edmoredev/votaciones/assets/125479887/6dfeb6a1-434e-419f-aa26-7207e9a702c7)

url vista votar:http://localhost:8000/votar/
![image](https://github.com/edmoredev/votaciones/assets/125479887/7495020f-b4a4-4438-9cfa-09aec2fcc7d1)


#Docker

* Para este proyecto se realiza los campos de Tipo Documento, genero y localidad normalizadas, lo cual se agrega los siguientes datos desde el administrador de Django, por tal motivo se debe crear el superUser y agregar la información para la vista de la siguiente manera

![image](https://github.com/edmoredev/votaciones/assets/125479887/5994efca-e152-44af-af80-6b0d32ea0e0e)

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

![image](https://github.com/edmoredev/votaciones/assets/125479887/2e62156c-5b8d-4422-80a1-2b1b88386bd5)

ejecutamos
- docker exec -it nombre del doker /bin/sh

![image](https://github.com/edmoredev/votaciones/assets/125479887/f65ab2bc-3023-46bb-8a6d-eefb8207eb6b)


- python manage.py createsuperuser

![image](https://github.com/edmoredev/votaciones/assets/125479887/7b3e0df8-aa60-4b59-80d7-79b78d3075cf)

Ingresamos los datos de usuario, correo y password



Después de las migraciones

- python manage.py migrate

![image](https://github.com/edmoredev/votaciones/assets/125479887/b3fedb38-cf87-4b84-920f-5aa0080dc6e9)




