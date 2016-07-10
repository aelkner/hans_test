# Project django-cognoma

This repository, under the umbrella of organization Project Cognoma
(https://github.com/cognoma), holds the source code, under open source
licencing, of a runnable django site, a component in the overall system
specified in Project Cognoma that has a flow chart of components of the entire
system.  The django site fulfills the system requirement specified in the
purple box in the middle of the system diagram and will contain the
following:

* an html interface starting at a home page for anonymous scientists to visit
  and try out machine learning algorithms on, as well as admin pages for
  site admins to be able to manipulate site content

* a Rest API for other components of the system to use to read and write data
  found on the django site.

* a task handler, implemented using celery, to allow users to start long
  queries without being blocked while waiting for them to finish

The site is currently only ready to be run on a devloper's machine.  As it
becomes ready for staging, there will need to be instuctions added for the
various cloud instances running.  For now, as a developer, one can get it
running on their machine with the following instructions in a command
window:

> git clone git@github.com:cognoma/django-cognoma.git
> cd django-cognoma
> virtualenv env
> source env/bin/activate
> pip install -r requirements.txt
> python manage.py migrate
> python manage.py createsuperuser
> python manage.py runserver

Visiting localhost:800 should return the home page, currently the 'It worked'
page that comes with a brand new django site.
