#!/bin/bash

git pull
git commit
git push
git push heroku master
heroku run python manage.py test
