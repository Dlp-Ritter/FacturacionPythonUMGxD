## Instrucciones para entrar al contenedor y realizar cambios en Bash

Para acceder al contenedor y hacer cambios desde Bash, usa el siguiente comando:


```bash 
docker compose exec web /bin/bash
```

El contenedor se llama web, por si acaso 😄. Una vez dentro,se pueden realizar las tareas necesarias

### Acceder a PostgreSQL usando psql
Para acceder a la línea de comandos de PostgreSQL con psql (en lugar de usar python manage.py dbshell como en el curso), utilizar:

```bash
docker compose exec db psql -d postgresdbProject -U admin
```

#### Ejemplo para consultar datos de una tabla
Para ver los datos de la tabla inv_categoria, ejecuta:

```sql
SELECT * FROM inv_categoria;
```

#### Consideraciones para las Migraciones en Django

Asegúrate de tener en cuenta las migraciones de cada app de Django para la versión en Linux. Revisa los videos:

* Migraciones en Django y primera migración
* Migración del modelo categoría
* Migración del modelo subcategoría

##### Para hacer las migraciones
Entrar al contenedor con el comando del principio

```bash 
docker compose exec web /bin/bash
```

Ya dentro ejecutar lo siguiente para generar las migraciones.

```python
python manage.py makemigrations
```

Ya hecho lo anterior se puede ejecutar la migración de uno o todos los modelos

```python
python manage.py migrate
```