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

And you can login to the server using the following endpoint:
```bash
localhost:8000/api/login/
```

With the body:
```json
{
  "username": "<username>",
  "password": "<password>"
}
```

Of course you're gonna have to insert some username & password in the DB so here's how you can do that. Enter the following command in your terminal:
```bash
python manage.py shell
```

And then:
```python
from django.contrib.auth.models import User
u = User(username="<username>", password="<password>")
u.save()
```

After logging in from the login endpoint, a token is given back to you in a json format:
```json
{
  "token": "<token>"
}
```

Include that token in every of your request's Header:
```
Authorization: Bearer <token>
```

And now you have access to not only reading the database, but also insert, update & deleting an object from the database:

| Method  | endopint                       | permission                 |
| --------|--------------------------------|----------------------------|
| GET     | localhost:8000/purchases/      | anonymous access available |
| GET     | localhost:8000/purchases/{ID}/ | anonymous access available |
| POST    |localhost:8000/purchases/       | authenticated access only  |
| DELETE  | localhost:8000/purchases/{ID}/ | authenticated access only  |
| PUT     | localhost:8000/purchases/{ID}/ | authenticated access only  |

Cheers! :clinking_glasses: 
And have fun. :100: 

## Contribute
I don't know why you'd wanna do that, but PR's are welcomed anytime :relaxed:
