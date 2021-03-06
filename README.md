![Django CI](https://github.com/lugnitdgp/glug_website_backend/workflows/Django%20CI/badge.svg?branch=master)
# GLUG Website Public Repo
We are using django REST framework for backend api. <br />
And Vue.js for frontend. <br />

#### Click [here](https://documenter.getpostman.com/view/5813355/RzZ7mzS4) to refer to the api documentation.

---
Use a virtual envionment for installing this, 
i.e `venv` or `pipenv`.
### Install Dependencies
For debian based distro, *in virtual evironment* terminal type
```shell
pip install -r requirements.txt
```
### To run the project on local machine
Create a PostgresSQL database.</br>
Then `cp .env.example .env` and change `.env` file according to your need.

Inside project directory type
```shell
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py collectstatic

# To run with development settings
python3 manage.py runserver --settings=glug_website.dev-settings
```
