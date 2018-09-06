import json
import requests
import unittest
import transaction
from pyramid import testing


def dummy_request(dbsession):
    return testing.DummyRequest(dbsession=dbsession)

# base test class sets up and tears down, the test runner
# expects us to define how to set up and tear down the test run
# usually has to do with connecting to a db
# always test in an isolated environment
# set up a special test db
# each test should be completely isolated and not dependent


class BaseTest(unittest.TestCase):
    def setUp(self):
        """ configure connection to db, like what we do in development.ini
        """
        self.config = testing.setUp(settings={
            'sqlalchemy.url': 'postgres://localhost:5432/stocks_api_test'
        })
        self.config.include('..models')
        settings = self.config.get_settings()

        from ..models import (
            get_engine,
            get_session_factory,
            get_tm_session,
            )

        self.engine = get_engine(settings)
        session_factory = get_session_factory(self.engine)

        self.session = get_tm_session(session_factory, transaction.manager)

    def init_database(self):
        """ Sets up all of the tables in the db
        """
        from ..models.meta import Base
        Base.metadata.create_all(self.engine)

    def tearDown(self):
        """ Dump an destroy all of the tables in the db
        """
        from ..models.meta import Base

        testing.tearDown()
        transaction.abort()
        Base.metadata.drop_all(self.engine)


def test_user_registration(testapp):
    """
    """
    account = {
        'email': 'yoyo@yogo.com',
        'password': '1234'
    }
    res = testapp.post('/api/v1/auth/register', json.dumps(account), status=201)
