# Project: Item Catalog @ Udacity Full Stack Nanodegree
# "Catalog App" web application

This project is a web application "Catalog App" in Flask that provides a general purpose catalog of items. Users can review catalog items without signing in. Users can also add new items, as well as edit and delete the items they have created upon signin in using Google OAuth.

Catalog is organized per categories of items. Before accessing data about items, users select the category. Categories are under control of web administrator only, so users cannot create, delete or change categories using "Catalog App" web application. 

Besides real categories, users also have on their disposal two helper cathegories: 

"Latest Items" showing the last 10 items created in the application by all users, and

"My Items" showing the list of items currently logged in user owns.


## Deployment Info

| Parameter | Value |
| ------ | ------ |
| IP Address of the server | 52.58.31.5 |
| SSH port | 2200 |
| URL of the web application | http://52.58.31.5.xip.io/catalog |


## Notes:

Followed [instructions](http://flask.pocoo.org/docs/1.0/deploying/mod_wsgi/) to integrate Flesk with Apache2

## Summary of other configuration and changes

Added support for PostgreSQL
Adjusted code so that new directory structure is considered
Updated AWS configuration to reflect te same ports opening as on Ubuntu
Updated Google credentials with validated domain (used meta tag method)

## Files included in Git repository:

| File | Comment |
| ------ | ------ |
| database_setup.py | application that creates database |
| load_categories.py | application that loads categories into database |
| application.py | main application that runs Flask web server |
| README.md | this file |
| templates/main.html | main html template; all others extends this one  |
| templates/catalog.html | catalog template, main app navigation page  |
| templates/item.html | item template that shows catalog item  |
| templates/newItem.html | template that allows creating new item  |
| templates/editItem.html | template that allows edditing an item  |
| templates/deleteItem.html | template that allows delleting an item  |
| static/styles.css | CSS file, addition to Bootstrap invoked in main.html |
| static/favicon.ico | Web app icon, required by browsers |


## Files nessesary bit not included in Git repository (transfer to server done using scp)

| File | Comment |
| ------ | ------ |
| client_secrets.json | Google OAuth web app client secrets  |
| db_secrets.json | PostgreSQL database credentials   |

## Dependencies

| Software | Version | Download |
| ------ | ------ | ------ |
| Python | Python 3.5.2 | [link](https://www.python.org/downloads/release/python-352/) |
| Flask | 1.0.2 | [link](http://flask.pocoo.org/docs/1.0/installation/) |
| PostgreSQL | 9.5 | [link](https://www.postgresql.org/download/) |


## catalog.wsgi:

\#!/usr/bin/python3

import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/CatalogApp/CatalogApp/")

from application import app as application
application.secret_key = 'super_secret_key'