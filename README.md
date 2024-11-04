## Instrucciones para entrar al contenedor y realizar cambios en Bash

#### Consideraciones para las Migraciones en Django

Asegúrarse de tener en cuenta las migraciones luego de clonar o copiar el repositorio ya que de otro modo no funcionara.

##### Para hacer las migraciones
Entrar al contenedor con el comando:

```bash 
docker compose exec web /bin/bash
```

Ya dentro ejecutar lo siguiente para generar las migraciones.

```python
python manage.py makemigrations
```

Ya hecho lo anterior se puede ejecutar las migraciónes

```python
python manage.py migrate
```
El contenedor se llama web, por si acaso 😄. Una vez dentro,se pueden realizar las tareas necesarias

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

