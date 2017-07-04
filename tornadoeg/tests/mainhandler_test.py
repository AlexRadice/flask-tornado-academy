import tornado.testing
import tornado.web
from application import make_app
from mainhandler import MainHandler


class MainHandlerTest(tornado.testing.AsyncHTTPTestCase):
    "Test fixture for MainHandler class"

    def get_app(self):
        "Return a Tornado application instance that will be used for the tests"
        return make_app()

    def testSimpleGet(self):
        "Test simple GET"
        response = self.fetch('/')
        self.assertEqual(response.code, 200)
        self.assertIn('<h1>This is the Home Page!</h1>', response.body)

