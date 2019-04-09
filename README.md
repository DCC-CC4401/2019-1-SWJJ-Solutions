# Smitty Werbenjagermanjensen's Project

Description
(Change title?)


## Getting Started

This project is made in Python (3.6.7) using the IDE PyCharm.
Even though this IDE was used, it should be possible to be executed successfully from the terminal
regardless of the OS.

### Prerequisites

#### Pipenv
A tool that mixes Python's pip, Pipfiles and virtualenv to simplify and automatize the
installation of the packages needed to run the algorithm. To install use the following:

``` pip install pipenv ```


### Installing

The project uses the framework Django and two libraries: "xlrd" and "XlsxWriter",
for reading and writing Excel files respectively.
You can add them both by using Pipenv with the following command inside this project's directory:

``` pipenv install ```

For more details on these libraries, please head to the section [Developed With](#developed-with)
to find their documentation links.


## Executing

First it's necessary to start Pipenv console to install this project's packages and framework.

``` pipenv shell ```

Next, run the following commands to configure Django:

```
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

(You can exit Pipenv's shell using `exit` or by pressing Ctrl + D.Also, remember to replace `python`
with whichever command matching the version you're using). 

From now on, you just need the following command to start this project's local server:

``` pipenv run python manage.py runserver```


## Developed With
* [Django](https://www.djangoproject.com/) - Python's web framework.
* [Pipenv](https://pipenv.readthedocs.io/en/latest/) - Python's packaging tool.
* [xlrd](https://xlrd.readthedocs.io) - Library for reading data and formatting Excel files.
* [XlsxWriter](https://xlsxwriter.readthedocs.io/) - Module for creating Excel XLSX files. 


## Authors
* Sofía Castro - [@cinnamontea](https://github.com/cinnamontea)
* David De La Puente - [@daviddelapuente](https://github.com/daviddelapuente)
* Pablo Torres - [@pabtorres](https://github.com/pabtorres)

