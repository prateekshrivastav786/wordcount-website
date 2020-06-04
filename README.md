# wordcount-website
This website is created in Django Python. It is locally hosted website which runs on port 8000. 
This website project has main file named manage.py which is used to run the Django server. It has folder named wordcount
which is the main code folder where all the necessary code files are kept. lastly, it contain folder named templete which has
all the html code used for rendering the website.
**********************************************************
How to run the project:
**********************************************************

1.First install Django in your machine:
pip install django==2.0.2 (please make sure you install this specific version only)

2. Create the project folder and get the dump of the code in the same manner it resides in the repositories:
django-admin startproject <folder name>
  
3.run the server by executing the manage.py:
python manage.py runserver
It will show ip address and port please paste that into your browser to access the wordcount website like:
http://127.0.0.1:8000/

Thanks.
******************************************************************************************************************************

Bonus:

Django Cheat Sheet:

Creating a new project:

django-admin startproject projectname
-------------------------------------
Add an app to a project:

python3 manage.py startapp appname
------------------------------------
Starting the server:

python3 manage.py runserver
-----------------------------------
Creating migrations:

python3 manage.py makemigrations
-----------------------------------
Migrate the database:

python3 manage.py migrate
----------------------------------------
Creating a Super User for the admin panel:

python3 manage.py createsuperuser
-----------------------------------------
Collecting static files into one folder:

python3 manage.py collectstatic
