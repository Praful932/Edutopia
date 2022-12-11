# Edutopia

For Contributing Refer [here](https://github.com/Praful932/Edutopia/blob/master/Contributing.md)

Live [here](https://edutopia.herokuapp.com/)


What is it about? - [Abstract](https://drive.google.com/file/d/1nApaZybBSr71Em6enLdp-okG8q0l-CY3/view?usp=sharing)

My Final Project for [CS50](https://cs50.harvard.edu/college/2020/spring/)

![Demo](demo.gif)

## Development
Note : Make sure you have Python version >=3.8

Environment Setup

`$ git clone https://github.com/Praful932/Edutopia.git`

`$ cd Edutopia/`

Install requirements from [poetry](https://python-poetry.org/docs/#installation) - `poetry install`
    - OR If you prefer the vanilla route using virtual env `poetry export -f requirements.txt --output requirements.txt --without-hashes`

Activate the environment -  `poetry shell`

Migrate and create DB

`python manage.py makemigrations`

`python manage.py migrate`

Create superuser
`python manage.py createsuperuser`

All Set!

`$ python manage.py runserver`

To exit the environment

`$ deactivate `

- For enabling google map API, you may need to add api key in alpha and beta page on 113 & 140 line respectively as requests are disabled for production usage.

