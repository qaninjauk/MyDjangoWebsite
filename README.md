# ProjectLFB Information
> A colaboration project between Andrew Corbett and myself to build a webpage showing data from LFB sources (jSon, csv) using both Powershell and PYTHON.

<br /><br /><br /><br />
## Useful PYTHON Commands

### 1. Create a new PYTHON Virtual Environment:
- python3 -m venv django_venv

### 2. Activate PYTHON Virtual Environment:
- source django_venv/bin/activate

### 3. Deactivate PYTHON Virtual Environment:
- source django_venv/bin/deactivate

### 4. Upgrade pip version:
- pip install --upgrade pip

### 5. Upgrade pip version:
- pip install pip3

### 5. Intall a package/library:
- pip install django

### 6. Create a django installation
cd django_venv
django-admin startproject mysite
django-admin  --version
python3 manage.py runserver

- open a web browser to http://127.0.0.1:8000/

### 7. Create a django app
python3 manage.py startapp main


### 7. Create a database for Django
Configure settings.py by adding to INSTALLED_APPS = [
-     'main.apps.MainConfig',
then run
-   python3 manage.py migrate

### 7. Create a models
see models.py example

### 8. Create a models
make the changes to models.py 
- python3 manage.py makemigrations main

### 9. Editt database from Python command line
make the changes to models.py 
python3  manage.py shell

Add to database 

>>> from main.models import Item,ToDoList
>>> t = ToDoList (name="Tims\'s List")
>>> t.save()
>>> ToDoList.objects.all()

>>> ToDoList.objects.get(id=1)

>>> t.item_set.all()

>>> t.item_set.create(text="Go to the mall",complete=False)
