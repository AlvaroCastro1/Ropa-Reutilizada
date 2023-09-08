# Instalar virtualenv
```sh
pip install virtualenv
```

# Crea un entorno virtual
```sh
virtualenv venv
```
### Activa el entorno virtual (en Windows)
```sh
venv\Scripts\activate
```

### Activa el entorno virtual (en macOS y Linux)
```sh
source venv/bin/activate
```

## Instalar los requisitos
```sh
pip install -r requirements.txt
```
## Guardar los requisitos en un archivo 
```sh
pip freeze > requirements.txt
```

# Crear un proyecto Django
```sh
django-admin startproject <nombre>
```
# Ejecutar el servicio web
```sh
python manage.py runserver
```

```sh
python manage.py migrate
python manage.py createsuperuser
python manage.py startapp base
```

# Para Administradores
1. necesitamos crear el modelo (*models.py*)
2. Registra los modelos en el archivo *admin.py*
3. `http://localhost:8000/admin/`
> **_NOTA:_**  Podemos hacerlo con chatGPT para facilitarlo, mostrandole la tabla echa nos regresa el modelo

# Vistas (*HTML*)
1. Crea el archivo HTML en `ropa_reutilizada\base\templates`

2. Configura la vista de Django
    ```python
    from django.shortcuts import render

    def mi_pagina(request):
        return render(request, 'mi_pagina.html')
    ```
3. Configura una URL
Configurar una URL que esté asociada con la vista que se ha creado.

    ```python
    from django.urls import path
    from . import views

    urlpatterns = [
        path('mi_pagina/', views.mi_pagina, name='mi_pagina'),
    ]
    ```

6. Accede a la página en navegador
`http://localhost:8000/mi_pagina/`