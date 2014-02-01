========================
django-project
========================

A project template for Django projects based on (https://github.com/twoscoops/django-twoscoops-project).

To use this project follow these steps:

#. Create your working environment
#. Install Django
#. Create the new project using the django-project template
#. Install additional dependencies
#. Use the Django admin to create the project

*note: these instructions show creation of a project called "myproject".  You
should replace this name with the actual name of your project.*

Working Environment
===================

You have several options in setting up your working environment.  We recommend
using virtualenv to separate the dependencies of your project from your system's
python environment.  If on Linux or Mac OS X, you can also use virtualenvwrapper to help manage multiple virtualenvs across different projects.

Virtualenv Only
---------------

First, make sure you are using virtualenv (http://www.virtualenv.org). Once
that's installed, create your virtualenv::

    $ virtualenv --distribute myproject

You will also need to ensure that the virtualenv has the project directory
added to the path. Adding the project directory will allow `django-admin.py` to
be able to change settings using the `--settings` flag.

Virtualenv with virtualenvwrapper
--------------------------

In Linux and Mac OSX, you can install virtualenvwrapper (http://virtualenvwrapper.readthedocs.org/en/latest/),
which will take care of managing your virtual environments and adding the
project path to the `site-directory` for you::

    $ mkdir myproject
    $ mkvirtualenv -a myproject myproject-dev
    $ cd myproject && add2virtualenv `pwd`

Windows
----------

In Windows, or if you're not comfortable using the command line, you will need
to add a `.pth` file to the `site-packages` of your virtualenv. If you have
been following the Two Scoops of Django (https://django.2scoops.org) book's example for the virtualenv directory (pg. 12), then
you will need to add a python pathfile named `_virtualenv_path_extensions.pth`
to the `site-packages`. If you have been following the book, then your
virtualenv folder will be something like::

`~/.virtualenvs/myproject/lib/python2.7/site-directory/`

In the pathfile, you will want to include the following code (from
virtualenvwrapper):

    import sys; sys.__plen = len(sys.path)
    /home/<youruser>/myproject/myproject/
    import sys; new=sys.path[sys.__plen:]; del sys.path[sys.__plen:]; p=getattr(sys,'__egginsert',0); sys.path[p:p]=new; sys.__egginsert = p+len(new)

Installing Django
=================

To install Django in the new virtual environment, run the following command::

    $ pip install django

Creating your project
=====================

To create a new Django project called '**myproject**' using
django-project, run the following command::

    $ django-admin.py startproject --template=https://github.com/archen/django-project/archive/master.zip --extension=py,rst,html my_project
    

Installation of Dependencies
=============================

Depending on where you are installing dependencies:

In development::

    $ pip install -r requirements/local.txt

For production::

    $ pip install -r requirements.txt

*note: We install production requirements this way because many Platforms as a
Services expect a requirements.txt file in the root of projects.*

Acknowledgements
================

Thanks to:
    Audrey Roy / @audreyr
    Daniel Greenfeld / @pydanny

: for writing a wonderful book on best practices for Django development, and providing the skeleton for this project.

If you haven't read/used Two Scoops of Django (https://django.2scoops.org)
#. Shame on you
#. Go buy it!
