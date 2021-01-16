# Casting Agency

## Introduction:

The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. You are an Executive Producer within the company and are creating a system to simplify and streamline your process.

## Motivation

This is the capstone project of the Udacity*Full*Stack*Nanodegree Course. It covers a set of technicals topics in 1 app.

### Technologies

* Python
* PostgreSQL
* SQLAlchemy
* Flask
* Flask*CORS
* Flask*Migrate
* Unittest
* Postman
* Auth0

# Getting Started

## Installation

#### Python 3.8

Follow instructions to install the latest version of python for your platform in the <a href= 'https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python' target="_blank"> python docs </a> 

#### Virtual Enviornment

It is recommended to work within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the <a href= 'https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/' target="_blank"> python docs </a>


#### PIP Dependencies
Once you have your virtual environment setup and running, install dependencies by navigating to the ptoject directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) and [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) are libraries to handle the lightweight sqlite database. Since we want you to focus on auth, we handle the heavy lift for you in `./src/database/models.py`. We recommend skimming this code first so you know how to interface with the Drink model.

- [jose](https://python-jose.readthedocs.io/en/latest/) JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.

## Running the server

From within the `./starter` directory first ensure you are working using your created virtual environment.

Each time you open a new terminal session, run:

- On linux : `export`
- On Windows : `set`

```
set FLASK_APP=app.py

set FLASK_ENV=development

set FLASK_DEBUG=true 

flask run
```

## Base URL: 

* The APP will be run locally at ``http://127.0.0.:5000/``
* Online URL:  `https://fsnd2020-casting-agency.herokuapp.com/`
* Authentication: This app has 3 users. Each has his own token which are provided in `setup.sh` file. Details about each user privilege are provided below.


### Users Authentication: ([RBAC Controls]

Access of reading, editing and writing to the database is restricted to specific roles. Those roles are:

#### Casting Assistant:

- GET /movies
- GET /actors

#### Casting Director:

- GET /movies
- GET /actors
- POST /actors
- PATCH /movies
- PATCH /actors
- DELETE /actors

#### Executive Producer:

- GET /movies
- GET /actors
- POST /movies
- POST /actors
- PATCH /movies
- PATCH /actors
- DELETE /movies
- DELETE /actors



## Endpoints
- GET '/actors'
- GET '/movies'
- POST '/actors/new'
- POST '/movies/new'
- PATCH '/actors/<int:actorId>'
- PATCH '/movies/<int:movieId>'
- DELETE '/actors/<int:actorId>'
- DELETE '/movies/<int:movieId>'

### Log-in:
```
https://dev-yxusw3rb.us.auth0.com/authorize?audience=CastingAgency&response_type=token&client_id=s4X97UzotmaoXgWqHTXCmXtuP5pHPX86&redirect_uri=https://127.0.0.1:8100/result
```


### Account:

* Casting Assistant
````
 Email: Assistant@Casting.Agency.com
 Password: Assistant123 
````

* Casting Director 
````
Email: Director@Casting.Agency.com
Password: Director456
````
* Casting Producer
````
Email: Producer@Casting.Agency.com
Password: Producer789
````
Following is the demonstration of each endpoint.



# Testing

Testing by postman:

`import Casting Agency Collection`

### GET '/actors'
- General: Returns all available actors.
- Sample:  http://127.0.0.1:5000/actors
```
{
    "Actors List":[
        {
            "age": "44",
            "gender": "Female",
            "id": 21,
            "name": "Ali Alali"
        },
        {
            "age": "25",
            "gender": "Female",
            "id": 22,
            "name": "Fatimah Alhela"
        },
        {
            "age": "15",
            "gender": "Female",
            "id": 23,
            "name": "Noone"
        }
    ],
    "Success": true,
    "Total Actors": 26
}
```

### GET '/movies'
- General: Returns all available movies
- Sample:  http://127.0.0.1:5000/movies
```
{
    "Movies List": [
        {
            "id": 6,
            "relase_date": "Fri, 07 Aug 2018 00:00:00 GMT",
            "title": "Birth Love"
        },
        {
            "id": 8,
            "relase_date": "Sun, 16 Aug 2020 00:00:00 GMT",
            "title": "PK"
        },
        {
            "id": 9,
            "relase_date": "Sun, 16 Aug 2020 00:00:00 GMT",
            "title": "Noone"
        }
    ],
    "Success": true,
    "Total Movies": 5
}
```

### POST '/actors/new'
- General: Create new actor
- Sample:  http://127.0.0.1:5000/actors/new
```
{
    "Actor": [
        {
            "age": "29",
            "gender": "M",
            "id": 29,
            "name": "HELAL"
        }
    ],
    "Success": true,
    "Total Actor": 28
}
```
### POST '/movie/new'
- General: Create new movie
- Sample:  http://127.0.0.1:5000/movie/new
```
{
    "Total Movies": 6,
    "movie": [
        {
            "id": 10,
            "relase_date": "Sat, 16 Jan 2021 00:00:00 GMT",
            "title": "First Love"
        }
    ],
    "success": true
}
```

### PATCH '/actor/<int:actorId>'
- General: Update Actor information by its id 
- Sample:  http://127.0.0.1:5000/actor/2
```
{
    "actor": [
        {
            "age": "12",
            "gender": "M",
            "id": 10,
            "name": "Quen of KSA"
        }
    ],
    "success": true,
    "total_actor": 28,
}
```

### PATCH '/movie/<int:movieId>'
- General: Update Movie information by its id 
- Sample:  http://127.0.0.1:5000/movie/6
```
{
    "movie": [
        {
            "id": 6,
            "relase_date": "Fri, 07 Aug 2015 00:00:00 GMT",
            "title": "2020 die"
        }
    ],
    "success": true,
    "total_actor": 6,
}
```
### DELETE '/actor/<int:actorId>'
- General: Delete Actor information by its id 
- Sample:  http://127.0.0.1:5000/actor/8
```
{
    "Total Actors": 27,
    "delete": 8,
    "success": true
}
```
### DELETE '/movie/<int:movieId>'
- General: Delete Movie information by its id 
- Sample:  http://127.0.0.1:5000/movie/8
```
{
    "Total Movies": 5,
    "delete": 8,
    "success": true
}
```

## Error Handling
Errors are returned as JSON objects in the following format:
```
{
    "success": False, 
    "error": 400,
    "message": "bad request"
}
```
The API will return six error types when requests fail:

- 400: Bad Request
- 403: Forbidden
- 404: Resource Not Found
- 405: Method Not Allowed
- 422: Not Processable
- 500: Internal server error
