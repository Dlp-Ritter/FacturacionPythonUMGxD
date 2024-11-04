## Instrucciones ejecutar el proyecto

Como es evidente el proyecto utiliza Docker, por lo que es necesario tenerlo instalado.
 - Instalar Docker Desktop (Esto también instalada Docker compose).
 - Clonar o copiar del pendrive el proyecto.
 - Ya estando en el directorio del proyecto, en una terminal ejecutarlo siguiente:

```bash 
docker compose up
```

Esto descargara la imagen de Python, Django, PostgreSQL, lo implementara en un entorno conjunto utilizando docker compose y quedara listo para las migraciones.
#### Consideraciones para las Migraciones en Django

Asegurarse de realizar las migraciones correspondientes luego de clonar o de copiar del pendrive el proyecto, ya que estos son necesarios para el funcionamiento del proyecto.

##### Para hacer las migraciones
Entrar al contenedor con el comando del principio

```bash 
docker compose exec web /bin/bash
```

Ya dentro ejecutar lo siguiente para generar las migraciones.

```python
python manage.py makemigrations
```

Ya hecho lo anterior se puede ejecutar las migraciones 

```python
python manage.py migrate
```

El contenedor se llama web, por si acaso 😄. Una vez dentro, se pueden realizar las tareas necesarias, como crear un superusuario en Django:

```bash
python manage.py createsuperuser
```

Luego de realizar las migraciones simplemente ejecutar nuevamente el siguiente comando y ya todo estará listo:

```bash 
docker compose up
```

### Acceder a PostgreSQL usando psql
Para acceder a la línea de comandos de PostgreSQL con psql (en lugar de usar python manage.py dbshell como en el curso), utilizar:

```bash
docker compose exec db psql -d postgresdbProject -U admin
```

#### Ejemplo para consultar datos de una tabla
Para ver los datos de la tabla inv_categoria, ejecutar:

```sql
SELECT * FROM inv_categoria;
```

