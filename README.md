# Instalar virtualenv
pip install virtualenv

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