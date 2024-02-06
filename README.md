# Create a virtual environment (replace 'venv' with your preferred name)
python -m venv venv

# Activate the virtual environment
# On Windows
venv\Scripts\activate
# On Unix or MacOS
source venv/bin/activate

pip install django mysql-connector-python
django-admin startproject myproject
cd myproject

python manage.py startapp myapp
python manage.py makemigrations
python manage.py migrate
python manage.py runserver


paths

myproject/
|-- myproject/
|-- myapp/
|   |-- templates/
|   |   |-- signup.html
|   |   |-- login.html
|   |-- models.py
|   |-- views.py
|   |-- urls.py
|-- myenv/
|-- manage.py


