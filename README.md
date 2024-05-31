# Python-Django-MongoDB-CRUD

API REST que permite a los usuarios utilizar una aplicación web para gestionar información de películas mediante operaciones CRUD, además de la funcionalidad de búsqueda mediante el título de la película.

## Tabla de Contenidos

- [Instalación](#instalación)
- [Uso](#uso)
- [API Endpoints](#api-endpoints)

## Instalación

### Prerrequisitos

Antes de comenzar, asegúrate de tener instalado lo siguiente en tu sistema:

- Python (versión 3.12.2)
- MongoDB
- pip (administrador de paquetes de Python)

### Pasos de Instalación

1. **Clona este repositorio:**

```bash
git clone https://github.com/JohannGaviria/Python-Django-MongoDB-CRUD.git
```

2. **Crear el entorno virtual:**

Utiliza `virtualenv` o otro gestor de entornos virtuales

```bash
pip install virtualenv
python -m virtualenv nombre_del_entorno
```

3. **Instalar las dependencias:**

```bash
cd Python-Django-MongoDB-CRUD
pip install -r requirements.txt
```

4. **Configurar la base de datos:**

- Crea una base de datos MongoDB en tu entorno.
- Actualiza los ajustes de conexión a MongoDB en `settings.py`.

5. **Crea las migraciones:**

```bash
python manage.py makemigrations
python manage.py migrate
```

6. **Ejecutar el servidor:**

```bash
python manage.py runserver
```

¡Listo! El proyecto ahora debería estar en funcionamiento en tu entorno local. Puedes acceder a él desde tu navegador web visitando `http://localhost:8000`.

## Uso

1. Ejecuta el servidor de desarrollo: 

```bash
python manage.py runserver
```

2. Accede a la API a través de las URL definidas.

## API Endpoints

### Crear nueva película

```http
POST /api/movies/create
```

| Parámetro       | Tipo     | Descripción        |
| :-------------- | :------- | :----------------- |
| `title`         | `string` | Título             |
| `description`   | `string` | Descripción        |
| `release_date`  | `date`   | Fecha de lanzamiento|
| `rating`        | `float`  | Puntuación         |
| `genres`        | `array`  | Géneros            |

#### Crear nueva película

```http
POST /api/movies/create
Content-Type: application/json

{
    "title": "Título de la película 1",
    "description": "Descripción de la película 1",
    "release_date": "2024-05-31",
    "rating": 9.9,
    "genres": [
        "género 1",
        "género 2",
        "género 3"
    ]
}
```

#### Respuesta exitosa al crear película

```http
HTTP/1.1 201 Created
Content-Type: application/json

{
    "status": "success",
    "message": "Movie created successfully",
    "data": {
        "movie": {
            "id": 1,
            "title": "Título de la película 1",
            "description": "Descripción de la película 1",
            "release_date": "2024-05-31",
            "rating": 9.9,
            "genres": [
                "género 1",
                "género 2",
                "género 3"
            ]
        }
    }
}
```

### Obtener todas las películas

```http
GET /api/movies/gets
```

| Parámetro | Tipo     | Descripción                                    |
| :-------- | :------- | :--------------------------------------------- |
| `page`    | `int`    | (Opcional) Número de página. Por defecto es 1. |

#### Obtener las películas

Obtiene las primeras 10 películas

```http
GET /api/movies/gets
Content-Type: application/json
```

Luego se pagina para obtener de a 10 películas

```http
GET /api/movies/gets?page=2
Content-Type: application/json
```

#### Respuesta exitosa al obtener las películas

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
    "status": "success",
    "message": "Movies found successfully",
    "data": {
        "movies": [
            {
                "id": 1,
                "title": "Título de la película 1",
                "description": "Descripción de la película 1",
                "release_date": "2024-05-31",
                "rating": 9.9,
                "genres": [
                    "género 1",
                    "género 2",
                    "género 3"
                ]
            },
            {
                "id": 2,
                "title": "Título de la película 2",
                "description": "Descripción de la película 2",
                "release_date": "2024-05-31",
                "rating": 5.8,
                "genres": [
                    "género 1",
                    "género 2",
                    "género 3",
                    "género 4"
                ]
            },
            {
                "id": 3,
                "title": "Título de la película 3",
                "description": "Descripción de la película 3",
                "release_date": "2024-05-31",
                "rating": 7.0,
                "genres": [
                    "género 1",
                    "género 2"
                ]
            }
        ]
    }
}
```

### Actualizar película existente

```http
PUT /api/movies/update/<movie_id>
```

| Parámetro      | Tipo     | Descripción                |
| :------------- | :------- | :------------------------- |
| `id`           | `integer`| ID de la película a actualizar|
| `title`        | `string` | Título                    |
| `description`  | `string` | Descripción               |
| `release_date` | `date`   | Fecha de lanzamiento      |
| `rating`       | `float`  | Puntuación                |
| `genres`       | `array`  | Géneros                   |

#### Actualizar película existente

```http
PUT /api/movies/update/<movie_id>
Content-Type: application/json

{
    "title": "Nuevo título de la película 1",
    "description": "Nueva descripción de la película 1",
    "release_date": "2024-05-31",
    "rating": 9.9,
    "genres": [
        "Nuevo género 1",
        "Nuevo género 2",
        "Nuevo género 3"
    ]
}
```

#### Respuesta exitosa al actualizar película existente

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
    "status": "success",
    "message": "Movie updated successfully",
    "data": {
        "movie": {
            "id": 1,
            "title": "Nuevo título de la película 1",
            "description": "Nueva descripción de la película 1",
            "release_date": "2024-05-31",
            "rating": 9.9,
            "genres": [
                "Nuevo género 1",
                "Nuevo género 2",
                "Nuevo género 3"
            ]
        }
    }
}
```

### Eliminar película existente

```http
DELETE /api/movies/<movie_id>
```

| Parámetro | Tipo     | Descripción                  |
| :-------- | :------- | :--------------------------- |
| `id`      | `integer`| ID de la película a eliminar |

#### Eliminar película existente

```http
DELETE /api/movies/<movie_id>
Content-Type: application/json
```

#### Respuesta exitosa al eliminar película existente

```http
HTTP/1.1 204 No Content

{
    "status": "success",
    "message": "Movie deleted successfully"
}
```

### Búsqueda de películas

```http
GET /api/movies/search?query=
```

| Parámetro | Tipo     | Descripción                |
| :-------- | :------- | :------------------------- |
| `query`   | `string` | Consulta de búsqueda       |

**Tipos de búsquedas:**
  - Título de la película

#### Buscar películas

```http
GET /api/movies/search?query=consulta_de_búsqueda
Content-Type: application/json
```

#### Respuesta exitosa a la búsqueda de películas

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
    "status": "success",
    "message": "Movies found successfully",
    "data": {
        "movies": [
            {
                "id": 1,
                "title": "Título de la película encontrada 1",
                "description": "Descripción de la película encontrada 1",
                "release_date": "2024-05-31",
                "rating": 9.9,
                "genres": [
                    "género 1",
                    "género 2",
                    "género 3"
                ]
            },
            {
                "id": 2,
                "title": "Título de la película encontrada 2",
                "description": "Descripción de la película encontrada 2",
                "release_date": "2024-05-31",
                "rating": 5.8,
                "genres": [
                    "género 1",
                    "género 2",
                    "género 3",
                    "género 4"
                ]
            }
        ]
    }
}