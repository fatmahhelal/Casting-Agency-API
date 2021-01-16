import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc
from flask_cors import CORS
from sqlalchemy.sql.expression import func
from models import *
from auth import AuthError, requires_auth
import json
from jose import jwt

# defined a paginating actors function
ACTORS_PER_PAGE = 20


def pagination(request, selection):
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * ACTORS_PER_PAGE
    end = start + ACTORS_PER_PAGE

    formated_page = [actor.format() for actor in selection]
    current = formated_page[start:end]

    return current


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    # set up CORS, allowing all origins
    CORS(app)

# CORS Headers
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type, Authorization, true'
                             )
        response.headers.add('Access_Control-Allow-Headers',
                             'GET, POST, DELETE, PATCH, OPTIONS'
                             )
        return response

    # Home page for all users

    @app.route('/')
    def index():
        actors = Actors.query.all()
        movies = Movies.query.all()
        return jsonify({
            'success': True,
            'application': 'Casting Agency API',
            'Total Movies': len(movies),
            'Total Actors': len(actors),
        })

# endpoint to handle GET requests for all available actors
    @app.route('/actors')
    def get_actors():
        try:
            actors = Actors.query.all()
            formated_actor = pagination(request, actors)
            # abort 404 if no actors available
            if len(actors) == 0:
                abort(404)
            # return success response
            return jsonify({
                'success': True,
                'Actors List': formated_actor,
                'Total Actors': len(actors)
            })
        # abort 422 if the request is un processable
        except Exception as e:
            abort(422)

# endpoint to DELETE actor using a its ID.
    @app.route('/actors/<int:actoreId>', methods=['DELETE'])
    @requires_auth('delete:actor')
    def delete_actors(jwt, actoreId):
        # get the actor by its id to DELETE
        actore = Actors.query.filter(Actors.id == actoreId).one_or_none()

        # abort 404 if the actor not found
        if actore is None:
            abort(404)

        # delete the actor
        actore.delete()

        # return success response
        return jsonify({
            'success': True,
            'delete': actoreId,
            'Total Actors': len(Actors.query.all())

          })

# endpoint to handle POST requests for Create a new actors
    @app.route('/actors/new', methods=['POST'])
    @requires_auth('post:actor')
    def add_actors(payload):
        body = request.get_json(force=True)
        try:
            # get the new newActor's informatin
            newName = body.get('name')
            newAge = body.get('age')
            newGender = body.get('gender')
            newActor = Actors(name=newName, age=newAge, gender=newGender)

            # abort 400 if the requst is bad
            if (newName == '' or newAge == '' or newGender == ''):
                abort(400)

            # insert the actor
            newActor.insert()
            actor = [Actors.query.get(newActor.id).format()]

            # return success response
            return jsonify({
                'success': True,
                'Actor': actor,
                'Total Actor': len(Actors.query.all())
            })
        # abort 422 if the request is un processable
        except Exception as e:
            abort(422)

# endpoint to PATCH actors using a its ID
    @app.route('/actors/<int:actore_id>', methods=['PATCH'])
    @requires_auth('patch:actor')
    def update_actors(jwt, actore_id):
        actors = Actors.query.filter(Actors.id == actore_id).one_or_none()

        body = request.get_json(force=True)
        try:

            name = body.get('name')
            age = body.get('age')
            gender = body.get('gender')

            if body is None:
                abort(404)

            actors.name = name
            actors.age = age
            actors.gender = gender
            actors.update()

            return jsonify({
                'success': True,
                'actor': [actors.format()],
                'total_actor': len(Actors.query.all())
            })
        # abort 422 if the request is un processable
        except Exception as e:
            abort(422)

# endpoint to handle GET requests for all available Movies
    @app.route('/movies')
    def get_movies():
        try:
            movies = Movies.query.all()
            formated_movie = pagination(request, movies)

            # abort 404 if no movies available
            if len(movies) == 0:
                abort(404)

            # return success response
            return jsonify({
                'success': True,
                'Movies List': formated_movie,
                'Total Movies': len(movies)
            })
        # abort 422 if the request is un processable
        except Exception as e:
            abort(422)

# endpoint to DELETE movie using a its ID.
    @app.route('/movies/<int:movieId>', methods=['DELETE'])
    @requires_auth('delete:movie')
    def delete_movies(jwt, movieId):
        # get the movie by its id to DELETE
        movie = Movies.query.filter(Movies.id == movieId).one_or_none()

        # abort 404 if the movie not found
        if movie is None:
            abort(404)

        # delete the movie
        movie.delete()

        # return success response
        return jsonify({
          'success': True,
          'delete': movieId,
          'Total Movies': len(Movies.query.all())
        })

# endpoint to handle POST requests for Create a new actors
    @app.route('/movies/new', methods=['POST'])
    @requires_auth('post:movie')
    def add_movies(jwt):
        # get the new newMoview's informatin
        body = request.get_json(force=True)
        try:
            newTitle = body.get('title')
            newRelease_date = body.get('relase_date')
            movies = Movies(title=newTitle, relase_date=newRelease_date)

            # abort 400 if the requst is bad
            if newTitle == '' or newRelease_date == '':
                abort(404)

            # insert the movie
            movies.insert()
            movie = [Movies.query.get(movies.id).format()]

            # return success response
            return jsonify({
                'success': True,
                'movie': movie,
                'Total Movies': len(Movies.query.all())
                })
        # bort 422 if the request is un processable
        except Exception as e:
            abort(422)

# endpoint to PATCH movies using a its ID.
    @app.route('/movies/<int:movieId>', methods=['PATCH'])
    @requires_auth('patch:movie')
    def update_movie(jwt, movieId):
        movie = Movies.query.filter(Movies.id == movieId).one_or_none()
        # returns a 404 error if movie is not found
        if movie is None:
            abort(404)

        # get the enterd data from client
        body = request.get_json(force=True)
        newTitle = body.get('title')
        newRelase_date = body.get('relase_date')

        # returns a 400 error if  title None
        if newTitle == '' or newRelase_date == '':
            abort(404)

        try:
            # update movie in the database
            movie.title = newTitle
            movie.relase_data = newRelase_date
            movie.update()

            # return success response
            return jsonify({
                'success': True,
                'movie': [movie.format()],
                'total_movie': len(Movies.query.all())
            })
        # abort 422 if the request is un processable
        except Exception:
            abort(422)

# Error Handling for all expected errors 400, 403, and AuthError.
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "resource not found"
        }), 404

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "un processable"
        }), 422

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "bad request"
        }), 400

    @app.errorhandler(403)
    def forbidden(error):
        return jsonify({
            "success": False,
            "error": 403,
            "message": "Forbidden"
        }), 403

    @app.errorhandler(405)
    def unallowed_method(error):
        return jsonify({
            "success": False,
            "error": 405,
            "message": "Method not Allowed"
        }), 405

    @app.errorhandler(500)
    def server_error(error):
        return jsonify({
            "success": False,
            "error": 500,
            "message": "internal server error"
        }), 500

    # error handler for AuthError
    @app.errorhandler(AuthError)
    def auth_error(ex):
        response = jsonify(ex.error)
        response.status_code = ex.status_code
        return response

    return app


app = create_app()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
