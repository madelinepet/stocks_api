# import unittest
# import transaction

# from pyramid import testing


# # controllres require us to pass in req object. When we're unit testing, we
# # don't have a req object, so pyramid mocks one up for us for testing purposes
# def dummy_request(dbsession):
#     return testing.DummyRequest(dbsession=dbsession)

# # base test class sets up and tears down, the test runner
# # expects us to define how to set up and tear down the test run
# # usually has to do with connecting to a db
# # always test in an isolated environment
# # set up a special test db
# # each test should be completely isolated and not dependent


# class BaseTest(unittest.TestCase):
#     def setUp(self):
#         """ configure connection to db, like what we do in development.ini
#         """
#         self.config = testing.setUp(settings={
#             'sqlalchemy.url': 'sqlite:///:memory:'
#         })
#         self.config.include('.models')
#         settings = self.config.get_settings()

#         from .models import (
#             get_engine,
#             get_session_factory,
#             get_tm_session,
#             )

#         self.engine = get_engine(settings)
#         session_factory = get_session_factory(self.engine)

#         self.session = get_tm_session(session_factory, transaction.manager)

#     def init_database(self):
#         """ Sets up all of the tables in the db
#         """
#         from .models.meta import Base
#         Base.metadata.create_all(self.engine)

#     def tearDown(self):
#         """ Dump an destroy all of the tables in the db
#         """
#         from .models.meta import Base

#         testing.tearDown()
#         transaction.abort()
#         Base.metadata.drop_all(self.engine)


# class TestMyViewSuccessCondition(BaseTest):

#     def setUp(self):
#         """ Sets up db based on super class, adds new model
#         """
#         super().setUp()
#         self.init_database()

#         from .models import MyModel

#         model = MyModel(name='one', value=55)
#         self.session.add(model)

#     def test_passing_view(self):
#         """ Creates new view, asserts data is as expected
#         """
#         from .views.default import my_view
#         info = my_view(dummy_request(self.session))
#         self.assertEqual(info['one'].name, 'one')
#         self.assertEqual(info['project'], 'stocks_api')


# class TestMyViewFailureCondition(BaseTest):

#     def test_failing_view(self):
#         from .views.default import my_view
#         info = my_view(dummy_request(self.session))
#         self.assertEqual(info.status_int, 500)
