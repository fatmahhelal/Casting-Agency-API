import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import setup_db, Actors, Movies

class agencytest(unittest.TestCase):
    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "agencytest"
        self.database_path = "postgres://{}:{}@{}/{}".format('postgres', '123456','localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)
       
        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

        self.actor = {
            'name': 'Fatimah Alhelal',
            'age': '25',
            'gender': 'Female'
        }
        self.actor2 = {
            'name': 'Fatimah Alhelal',
            'age': '26',
            'gender': 'Female'
        }
        self.delete_actor = {
            'name': 'Fatimah Alhelal',
            'age': '25',
            'gender': 'Female'
        }
        self.movie = {
            {
                'relase_date': '2020-08-12 00:00:00',
                'title': 'FSND'
            }
        }
        self.movie2 = {
            {
                'relase_date': '2020-08-12 00:00:00',
                'title': 'Full Love'
            }
        }
        self.delete_movie = {
            {
                'relase_date': '2020-08-12 00:00:00',
                'title': 'FSND'
            }
        }
ASSISTANT = "Bearer {}".format(os.environ.get('ASSISTANT'))
DIRECTOR = "Bearer {}".format(os.environ.get('DIRECTOR'))
PRODUCER = "Bearer {}".format(os.environ.get('PRODUCER'))

def tearDown(self):
    """Executed after reach test"""
    pass


# -----------------------------------#
# ----------- Actors Test -----------#
# -----------------------------------#

def test_get_actors(self):
    # test GET requests for actors
    # get actors endpoint test function
    res = self.client().get('/actors',
                            headers={'Authorization': ASSISTANT}
                            )
    data = json.loads(res.data)
    # check status code and message
    self.assertEqual(res.status_code, 200)
    self.assertEqual(data['success'], True)
    self.assertTrue(len(data['Actors List']))
    self.assertTrue(data['Total Actors'])


def test_error_get_actors(self):
    # test GET requests for actors
    # get actors endpoint test function
    res = self.client().get('/actors/',
                            headers={'Authorization': ASSISTANT}
                            )
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 404)
    self.assertEqual(data['success'], False)
    self.assertEqual(data['message'], 'resource not found')


def test_delete_actore(self):
    # test delete requests for actors
    res = self.client().delete('/actors/1',
                               json=self.delete_actor,
                               headers={'Authorization': PRODUCER}
                               )
    data = json.loads(res.data)
    self.assertEqual(res.status_code, 200)
    self.assertEqual(data['success'], True)
    self.assertTrue(data['actoreId'])
    self.assertTrue(data['Total Actors'])


def test_error_delete_actore(self):
    res = self.client().delete('/actors/1',
                               json=self.delete_actore,
                               headers={'Authorization': ASSISTANT}
                               )
    data = json.loads(res.data)
    self.assertEqual(res.status_code, 403)
    self.assertEqual(data['success'], False)


def test_post_actor(self):
    res = self.client().post('/actors/new',
                             json=self.actor,
                             headers={'Authorization': PRODUCER}
                             )
    data = json.loads(res.data)
    self.assertEqual(res.status_code, 200)
    self.assertEqual(data['success'], True)
    self.assertTrue(len(data['Actor']))
    self.assertTrue(data['Total Actor'])


def test_error_post_actor(self):
    res = self.client().post('/actors/new',
                             json=self.actor,
                             headers={'Authorization': ASSISTANT}
                             )
    data = json.loads(res.data)
    self.assertEqual(res.status_code, 403)
    self.assertEqual(data['success'], False)


def test_update_actors(self):
    res = self.client().patch('/actors/1',
                              json=self.actor2,
                              headers={'Authorization': PRODUCER}
                              )
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 200)
    self.assertEqual(data['success'], True)
    self.assertTrue(len(data['actor']))
    self.assertTrue(data['total_actor'])


def test_error_update_actor(self):
    res = self.client().patch('/actors/665656',
                              json=self.actore2,
                              headers={'Authorization': PRODUCER}
                              )
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 404)
    self.assertEqual(data['success'], False)
    self.assertEqual(data['message'], 'resource not found')


# -----------------------------------#
# ----------- Movies Test -----------#
# -----------------------------------#

def test_get_movies(self):
    # test GET requests for actors
    # get actors endpoint test function
    res = self.client().get('/movies',
                            headers={'Authorization': ASSISTANT}
                            )
    data = json.loads(res.data)
    # check status code and message
    self.assertEqual(res.status_code, 200)
    self.assertEqual(data['success'], True)
    self.assertTrue(len(data['Movies List']))
    self.assertTrue(data['Total Movies'])


def test_error_get_movies(self):
    # test GET requests for movies
    # get movies endpoint test function
    res = self.client().get('/movies/',
                            headers={'Authorization': ASSISTANT}
                            )
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 404)
    self.assertEqual(data['success'], False)
    self.assertEqual(data['message'], 'resource not found')


def test_delete_movie(self):
    # test delete requests for actors
    res = self.client().delete('/movies/1',
                               json=self.delete_movie,
                               headers={'Authorization': PRODUCER}
                               )
    data = json.loads(res.data)
    self.assertEqual(res.status_code, 200)
    self.assertEqual(data['success'], True)
    self.assertTrue(data['movieId'])
    self.assertTrue(data['Total Movies'])


def test_error_delete_movie(self):
    res = self.client().delete('/movies/1',
                               json=self.delete_movie,
                               headers={'Authorization': ASSISTANT}
                               )
    data = json.loads(res.data)
    self.assertEqual(res.status_code, 403)
    self.assertEqual(data['success'], False)


def test_post_movies(self):
    res = self.client().post('/movies/new',
                             json=self.movie,
                             headers={'Authorization': PRODUCER}
                             )
    data = json.loads(res.data)
    self.assertEqual(res.status_code, 200)
    self.assertEqual(data['success'], True)
    self.assertTrue(len(data['movie']))
    self.assertTrue(data['Total Movies'])


def test_error_post_movies(self):
    res = self.client().post('/movies/new',
                             json=self.actor,
                             headers={'Authorization': DIRECTOR}
                             )
    data = json.loads(res.data)
    self.assertEqual(res.status_code, 403)
    self.assertEqual(data['success'], False)


def test_update_movies(self):
    res = self.client().patch('/movies/1',
                              json=self.movie2,
                              headers={'Authorization': PRODUCER}
                              )
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 200)
    self.assertEqual(data['success'], True)
    self.assertTrue(len(data['movie']))
    self.assertTrue(data['total_movie'])


def test_error_update_movies(self):
    res = self.client().patch('/movies/202019',
                              json=self.movie2,
                              headers={'Authorization': PRODUCER}
                              )
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 404)
    self.assertEqual(data['success'], False)
    self.assertEqual(data['message'], 'resource not found')


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()