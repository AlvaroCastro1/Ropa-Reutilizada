# Ambiente Virtual

## .env
Este archivo contiene las variables para la conexión a la base de datos MySQL. Necesitas hacer una copia del archivo `.env.bk` en la siguiente ubicación: `\Ropa-Reutilizada\ropa_reutilizada\.env.bk`, y luego reemplazar las variables.

## Instalación de virtualenv
Utilizaremos esta biblioteca para mantener solo las bibliotecas necesarias en nuestro entorno, ya que en caso de despliegue, solo utilizaremos lo necesario.

```sh
pip install virtualenv
```

## Creación de un entorno virtual
```sh
virtualenv venv
```

## Activación del entorno virtual (en Windows)
```sh
venv\Scripts\activate
```

## Activación del entorno virtual (en macOS y Linux)
```sh
source venv/bin/activate
```

## Instalación de los requisitos
Asegúrate de tener el entorno virtual activado antes de ejecutar este comando.

```sh
pip install -r requirements.txt
```

## Guardar los requisitos en un archivo
Asegúrate de tener el entorno virtual activado antes de ejecutar este comando.

```sh
pip freeze > requirements.txt
```

## Creación de un proyecto Django
```sh
django-admin startproject <nombre>
```

# Ejecución del servicio web
```sh
python manage.py runserver
```

# Cambios en la Base de Datos o Restablecimiento del Superusuario
Ir al directorio `Ropa-Reutilizada\ropa_reutilizada`
```sh
python manage.py migrate
python manage.py createsuperuser
python manage.py startapp base
```

# Para Administradores
1. Necesitamos crear el modelo (`models.py`).
2. Registra los modelos en el archivo `admin.py`.
3. Accede a `http://localhost:8000/admin/`.

> **NOTA:** Podemos hacerlo con ChatGPT para facilitarlo, mostrándole la tabla y él nos regresará el modelo.

# Vistas (HTML)
1. Crea el archivo HTML en `ropa_reutilizada\base\templates`.

2. Configura la vista de Django en un archivo views.py:

   ```python
   from django.shortcuts import render

   def mi_pagina(request):
       return render(request, 'mi_pagina.html')
   ```

3. Configura una URL asociada a la vista que has creado en el archivo urls.py:

   ```python
   from django.urls import path
   from . import views

   urlpatterns = [
       path('mi_pagina/', views.mi_pagina, name='mi_pagina'),
   ]
   ```

4. Accede a la página en el navegador:

   `http://localhost:8000/mi_pagina/`
