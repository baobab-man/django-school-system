#!/usr/bin/env zsh

source /Users/romeo/.zshrc
pyenv shell school
./manage.py makemigrations
./manage.py migrate