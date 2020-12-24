#!/usr/bin/env bash

source /Users/romeo/.bash_profile
pyenv shell school
./manage.py makemigrations
./manage.py migrate