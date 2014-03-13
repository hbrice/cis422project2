

======================================
LunarShift's Developer Documentation 
======================================

-------------------
The software used:
-------------------
1. Django - a web platform written in the python programming language. We are using django to simplify the database functionality of our program.
#. Heroku - is a cloud platform as a service. We are using heroku as our server hosting our web app and the database.
#. South -  is a tool to facilitate migration of django databases. We are using South to update our database as we change our source code.
#. dj-database-url - a system that allows more database options for django apps. We are using dj-database-url to allow the use of a Postgres database instead of the default sqlite database.
#. dj-static - Is a tool to override a setting in django allowing for a static file server. We are using dj-static to 
#. ajax - is tool allowing asynchronous presentation logic in web applications. We are using ajax to update a page without a refresh.
#. django-toolbelt - Is a collection of python components. We are using django-toolbelt for several utilities including gunicorn, and dj-static.