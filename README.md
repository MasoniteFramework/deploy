# deploy
Deployment package for Masonite

# Instructions

## Heroku CLI Tool

Make sure you have the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) tool. This package is simply a wrapper about several commands

## Installation

install the package:

```
$ pip install masonite_deploy
```

Then add the Service Provider to your `PROVIDERS` list:

```python
from masonite_heroku.providers import DeployProvider

...

PROVIDERS = [
    # Framework Providers
    AppProvider,
    SessionProvider,
    RouteProvider,
    # 'entry.providers.ApiProvider.ApiProvider',
    StatusCodeProvider,
    
    ...
    # Third Party Providers
    DeployProvider, # Here
    ...
]
```

You now have access to several new commands. You can see your command by running `craft` and looking under the `heroku` namespace.

## Setting Up

First you will need to create `Procfile` in the root of your project (where wsgi.py is located) and put this into it:

```
web: gunicorn -w 2 wsgi:application
```

Then add `masonite-cli` and `gunicorn` and `psycopg2` (or `psycopg2-binary`) and this package (`masonite_deploy`) to your requirements.txt:

```
waitress==1.1.0
masonite==2.0.11

...
masonite_cli
gunicorn
psycopg2-binary
masonite_deploy==0.0.1
```

Lastly, commit to your origin master branch.

# Usage

**This package is still in development and you may experience bugs**

## Deployment

If you have everything above configured then we can deploy with a single command:

```
craft heroku:deploy --app nameofapp
```

Let the command run and provision your app

## Configs

It's a little annoying to handle configuration files with Heroku if you are used to them being local so you can grab all the configuration variables
in Heroku and add them to a local environment file:

```
$ craft heroku:config --get
```

This will add all the variables of your heroku app to a `.env.production` file.

You can do the opposite by using:


```
$ craft heroku:config --set
```

This will take all the environment variables and set them into Heroku
