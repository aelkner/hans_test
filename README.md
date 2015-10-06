The following are the instructions for cloning the repo and getting it to
run on any unix system (assuming virtualenv-2.7 is installed):

> git clone git@github.com:aelkner/coding_challenge.git
> cd coding_challenge
> virtualenv-2.7 --distribute venv
> source venv/bin/activate
> pip install -r requirements.txt
> python manage.py test challenge_app
    (all tests pass)
> python manage.py migrate
    (not needed as this app has no need for a database, but to avoid the
     red warning message when running the server)
> python manage.py runserver
    (visit http://localhost:8000/ in the browser)

