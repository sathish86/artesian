.. VcCrowd documentation master file, created by
   sphinx-quickstart on Mon Oct  2 11:04:32 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to VcCrowd's documentation!
===================================

The User Guide:
===============
This part of the documentation, which begins with some background information about this project, then focuses on step-by-step instructions to run this project.

Django Project Summary:
=======================
VcCrowd is a simple django project which consist of two Django apps ‘broadcast’ and ‘integrator’ and it has list of features listed below.
1. Registration, Login and authentication using middleware.
2. Create and search Post which will be visible to all the registered users.
3. Integrator app has different models like ‘Startup’, ‘Government’, ‘Corporate’ and ‘Investor‘. This gives them facility to collaborate to each other by adding them as ‘Collaborator’ or removing them from their list of collaborators.
4. It has User and UserProfile models, using these models we can do view profile information and edit profile information.

Highlighting things that are used in this project:
==================================================
1. Django Template Forms
2. Django Many to Many, Foreign key, One to Many Relationship
3. Django Middleware
4. Django Unit test (used factory Boy and fixtures)
5. Generates coverage report for unit test
6. Coding standards checks using flake8 and isort
7. Populates with initial data load
8. Settings file for different environment
9. Requirements file for different environment.
10. Sphinx for documentation
11. Dockerfile and Docker-Compose to run the project in container, if needed.

Technologies Used:
==================
1. Django 1.11 and Python 3.5
2. Docker and docker-compose
3. Sphinx
4. Git
5. PostgreSQL
6. HTML, CSS and JavaScript
7. jQuery
8. Twitter Bootstrap

List of libraries used in this project:
=======================================
1. Current requirements_dev.txt
2. Django>=1.11,<2.0
3. psycopg2
4. flake8
5. isort
6. coverage
7. Sphinx

Read the documentation of this project:
=======================================
1. Open this file 'index.html' under this folder, "project_name/_build/html/index.html"

Installation:
=============

1. Docker and Docker-Compose:
-----------------------------

Using docker method (Assumes docker and docker-compose is already installed in your machine)

1. $ cd /path/to/your/workspace
2. $ git clone git://github.com/sathis86/artesian/ project_name && cd project_name
3. $ docker-compose build
4. $ docker-compose up

Hopefully this will build the image and run in container, it uses postgres and python3 image and link those container using docker-compose. It should server the app in localhost :8000 port.
Goto “Try these operations in this Django application:” section for more details


2. Virtual Env:
---------------

Using virtual environment (Assumes python3 is already installed in your machine)

    a. create virtual env
    python3 -m venv /path/to/new/virtual/environment
    source /path/to/new/virtual/environment/bin/activate

    b. Download the project:
    Now, you need the Django sample project files in your workspace:
    $ cd /path/to/your/workspace
    $ git clone git://github.com/kirpit/django-sample-app.git project_name && cd project_name

    c. Find the requirements/requirements_dev.txt file that has all the libraries that are required. To install them, simply type:

      $ pip install -r requirements/requirements_dev.txt

    d. Tweaks

    Set the right values in settings files:

      (i)  $ export PYTHONPATH=/path/to/your/workspace/project_name/
      (ii) $ export DJANGO_SETTINGS_MODULE=/path/to/your/workspace/project_name/artesian/settings_conf/dev

    Note:

    If we are running under web servers like UWSGI or Nginx, then
    project_name/wsgi.py file is necessary for WSGI gateways to run your Django application under webservers. You have to definitely change value in this file to whatever settings you wanted to use based on environment (e.g. artesian.settings_conf.test)

    e. Initialize the database and run server.

       First set the database engine (PostgreSQL, MySQL, etc..) in your settings files; For instance: projectname/artesian/settings_conf/dev.py and/or projectname/settings/local.py.

      (i) $ ./manage.py migrate
      (ii) $ ./manage.py runserver

    f. Run unit test

      (i) ./manage.py test

    g. Run unit test and coverage report

      (i) $ coverage run ./manage.py test
      (ii)  $ coverage html

Try list of operations below in this Django application:
========================================================
1. Hopefully you should see the project serving in localhost:8000
2. Register new user and login.
3. Change password
4. Try to create new Post and do some search (search results are based multiple fields like Post string, user role and user name).
5. Check profile information and edit.
6. Logout and register many users as you can with different roles ‘startup’,  ‘government’, ‘corporate’ and ‘investor’.
7. Goto ‘Collaborator’ link and check all the registered users listed down on that page. You can add and remove them as your collaborators.


.. toctree::
   :maxdepth: 2
   :caption: Contents:

   modules/broadcast_app
   modules/integrator_app


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
