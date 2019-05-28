# vocabulearn-api

## Setup
This is a Django project (www.djangoproject.com), using the Django Rest Framework (www.django-rest-framework.org) for building a RESTful API for Vocabulearn. It is specifically optimized to be run on Heroku (www.heroku.com). The Django-project is in the subfolder **vocabulearn**.

The project is designed to be run with an external PostgreSQL database, e.g. hosted on Heroku. All the confidential settings are excluded from git and have to be added manually in different ways for local or heroku-hosted setup.

### Running locally
For running a local debug Django server, you need to use the template file **vocabulearn/vocabulearn/env_secrets.template.py** to create a file **vocabulearn/vocabulearn/env_secrets.py** (which is in .gitignore). Here you can specify your settings, most notably:
* `SECRET_KEY`: The Django secret key that will be used for generating hashes.
* `DATABASE_URL`: The URL to your PostgreSQL database, including full login information.

Afterwards create a python virtual environment and install the requirements with
```
pip install -r vocabulearn/requirements.txt
```
Now you can simply start your debug server with
```
python vocabulearn/manage.py runserver
```

### Running on Heroku
Running on Heroku is a bit more complicated, mostly because of the Django project folder not being at the root of this repository. While this is the way recommended by Heroku, I feel more comfortable with having code in subfolders of the repository. Fortunately there's a custom buildpack available on github, for specifically that purpose which I forked for this project: https://github.com/pfaion/subdir-heroku-buildpack. Go to your app's settings on Heroku and add a new buildpack with the following URL:
```
https://github.com/pfaion/subdir-heroku-buildpack.git
```
Make sure that you drag the buildpack to the top of the list, e.g. before the python buildpack.

Now you have to set up your environment variables, also in the settings section of your Heroku app:
* `SECRET_KEY` - The Django secret key that will be used for generating hashes.
* `DATABASE_URL` - The URL to your PostgreSQL database, including full login information.
* `DJANGO_DEBUG: 0` - This should be 0 for production servers, as otherwise Django will include sensitive error information. Only set to 1 for specifically debugging Heroku, use a local setup otherwise.
* `ALLOWED_HOSTS: <youappname>.herokuapp.com` - For being able to send requests to Django from your Heroku URL. 
* `DISABLE_COLLECSTATIC: 1` - Since we don't use static files for the RESTful API and otherwise had to setup Heroku-specific static file handling in Django.
* `PROJECT_PATH: vocabulearn` - This is for making the subdirs buildpack work, which needs an environment variable with the subfolder name where it should run the application from.

Now you can deploy your app on Heroku, e.g. through GitHub integration.
