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



## A summary of software installed on the server

## Summary of configuration changes

## List of any third-party resources you made use of to complete this project.

## Included files

| File | Comment |
| ------ | ------ |
| database_setup.py | application that creates database |
| load_categories.py | application that loads categories into database |
| load_dummy_data | optional application that loads some dummy data |
| application.py | main application that runs Flask web server |
| README.md | this file |
| client_secrets.json | Google OAuth web app client secrets  |
| templates/main.html | main html template; all others extends this one  |
| templates/catalog.html | catalog template, main app navigation page  |
| templates/item.html | item template that shows catalog item  |
| templates/newItem.html | template that allows creating new item  |
| templates/editItem.html | template that allows edditing an item  |
| templates/deleteItem.html | template that allows delleting an item  |
| static/styles.css | CSS file, addition to Bootstrap invoked in main.html |
| static/favicon.ico | Web app icon, required by browsers |


## Dependencies

| Software | Version | Download |
| ------ | ------ | ------ |
| Python | Python 3.5.2 | [link](https://www.python.org/downloads/release/python-352/) |
| VirtualBox | 5.2.16 | [link](https://download.virtualbox.org/virtualbox/5.2.16/) |
| Vagrant | 2.1.2 | [link](https://releases.hashicorp.com/vagrant/2.1.2/) |

Also, you must have gmail address and Google credentials. If you don't have it, or want to create a test account for this purpose, you can follow instructions on the [link](https://accounts.google.com/signup/v2/webcreateaccoun). 


## Setup and run instructions:

1. Install Vagrant and VirtualBox
2. Clone the [fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm/) to your local machine
3. Within cloned directory, run:
    #### cd fullstack/vagrant
4. Run your virtual machine using command:
    #### vagrant up
5. Login to your vagrant session with command:
    #### vagrant ssh
6. Copy included files into /vagrant/catalog within the virtual machine.
7. Insinde your vagrant session, create database by running command:
    #### python3 /vagrant/catalog/database_setup.py
8. Insinde your vagrant session, oad cathegories by running command:
    #### python3 /vagrant/catalog/load_categiries.py
    You can safely run this command several times, to add additional categories, without risk to overide any existing data.
9. Optionally, you may load some dummy data with command 
    #### python3 /vagrant/catalog/load_dummy_data.py
    Multiple execution of this file will not overide added users, but it will be keep adding items, and it is save to run it multiple times, depending of the desired amount of dummy data.
10. Insinde your vagrant session, ran Flask web server application with command 
    #### python3 /vagrant/catalog/application.py
11. On your local machine, access web application by using following URL in your browser 
    #### http//localhost:8000
    Note: testing of this application is done with Chrome Version 70.0.3538.110, on Mac OS 10.13.6, with "SystemPreference/General/Show scroll bars" set to "Always".

12. Use your own Google credentials to sign in with "Catalog App"


## Packages used in development environment


| Package | Version |
| ------ | ------ |

|chardet | 2.3.0 |
|Click               |7.0|
|Flask               |1.0.2|
|httplib2            |0.12.0|
|itsdangerous        |1.1.0|
|Jinja2              |2.10|
|language-selector   |0.1|
|MarkupSafe          |1.1.0|
|oauth2client        |4.1.3|
|pip                 |18.1|
|pyasn1              |0.4.4|
|pyasn1-modules      |0.2.2|
|pycurl              |7.43.0|
|pygobject           |3.20.0|
|python-apt          |1.1.0b1+ubuntu0.16.4.2|
|python-debian       |0.1.27|
|python-systemd      |231|
|requests            |2.9.1|
|rsa                 |4.0|
|setuptools          |20.7.0|
|six                 |1.10.0|
|SQLAlchemy          |1.2.14|
|ssh-import-id       |5.5|
|ufw                 |0.35|
|unattended-upgrades |0.1|
|urllib3             |1.13.1|
|Werkzeug            |0.14.1|
|wheel               |0.29.0|
