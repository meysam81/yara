# Yara
This repository is a project demanded by an interviewer at [Yara Corp.](https://yaramobile.com/) to implement a simple and basic RESTful server using the following stacks:
* [Django](https://www.djangoproject.com/)
* [Django REST Framework](https://www.django-rest-framework.org/)

## Model
The so-called DB in this project is a single table containing the following fields:


| Field Name    |  Data Type                 | Constraint       |
|---------------|--------------------------- |------------------|
| purchase_date |  `datetime`                |                  |
| purchase_name |  `string`                  | max_length=150   |
| user_id       |  `integer`                 |                  |
| username      |  `string (max_length=150)` | max_length=150   |
| phone_number  |  `string (max_length=20)`  | max_length=20    |
| email         |  `string (max_length=150)` | max_length=150   |
| address       |  `text`                    |                  |

## Prerequisite
This project was written using `python3.7.2`, so you might as well install that before going any further.
[Python Official Website](https://www.python.org/)

You'll have to run this project in an environment, so I recommend installing them first hand.
```bash
pip install -U pip # install the latest pip, as it is updating frequently
pip install virtualenv
```

## Quickstart
You can clone the repository using the following comands in your terminal:
```bash
git clone git@github.com:meysam81/yara.git
```

And then:
```bash
cd yara
```

Now you're gonna have to create a new virtual environment inside the project's root directory.
```bash
virtualenv venv
source ./venv/bin/activate
``` 

Now install the requirements:
```bash
pip install -r requirements.txt
```

Now you are good to go, just run the server and have fun :smiley:
```bash
python manage.py runserver
```

## Contribute
I don't know why you'd wanna do that, but PR's are welcomed anytime :relaxed:
