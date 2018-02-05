# pacific-meadow

A Django app, which can easily be deployed to Heroku.

This application supports the [Getting Started with Python on Heroku](https://devcenter.heroku.com/articles/getting-started-with-python) article - check it out.

## Running Locally

Make sure you have Python [installed properly](http://install.python-guide.org). Also, install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) and [Postgres](https://devcenter.heroku.com/articles/heroku-postgresql#local-setup).

```sh
$ git clone https://github.com/AlexisClone/pacific-meadow.git
$ cd python-getting-started

$ pipenv install

$ createdb python_getting_started

$ python manage.py migrate
$ python manage.py collectstatic
```

Lunch this app with ```$ heroku local web``` on linux and ```$ heroku local web -f Procfile.windows``` on windows
Your app should now be running on [localhost:5000](http://localhost:5000/).

## Deploying to Heroku

```sh
$ heroku create
$ git push heroku master

$ heroku run python manage.py migrate
$ heroku open
```
or

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## Documentation

For more information about using Python on Heroku, see these Dev Center articles:

- [Python on Heroku](https://devcenter.heroku.com/categories/python)

## Authors

* **Alexis**


# Notes

 - Using a template for such projects is smart:
    * Pros:
        * You get done faster
        * You can focus on the code part
        * You deploy relatively simply
    * Cons
        * I bet that you have no idea of what decides what.
        * You do not really know what you're using and more importantly why you're using that.
   
 - Flask is waaaay simpler:
 ```python
 # That's an app in Flask
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
 ```
 - I was able to run it, which is a good point
 - Never used `Pipenv` before, I'm used to virtualenv but why not?
