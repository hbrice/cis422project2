#!/bin/bash

git pull
git push
git push heroku master
heroku run python manage.py test
