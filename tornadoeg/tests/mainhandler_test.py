from StringIO import StringIO
import tornado.gen
import tornado.testing
import tornado.web
from tornado.httpclient import HTTPResponse, HTTPRequest
from mainhandler import MainHandler


class MainHandlerTest(tornado.testing.AsyncHTTPTestCase):
    "Test fixture for MainHandler class"

    def __init__(self, *args, **kwargs):
        "Initialise fixture"
        super(MainHandlerTest, self).__init__(*args, **kwargs)
        self._datastore = MockDataStore()
        self._mock_google_response = None
        self._mock_yahoo_response = None

    def get_app(self):
        "Return a Tornado application instance that will be used for the tests"
        servicesDict={'datastore': self._datastore}
        return tornado.web.Application([
            (r"/", MainHandler, servicesDict)
        ])

    def testSimpleGet(self):
        "Test simple GET"
        self._datastore.mock_google_response = HTTPResponse(HTTPRequest('http://www.google.com'), 
                code=200, 
                headers={'Content-Length': 24},
                buffer=StringIO('<html><body>I Am Google</body></html>'))
        self._datastore.mock_yahoo_response = HTTPResponse(HTTPRequest('http://search.yahoo.com'), 
                code=200, 
                headers={'Content-Length': 20},
                buffer=StringIO('<html><body>I Am Groot</body></html>'))

        response = self.fetch('/')
        self.assertEqual(response.code, 200)
        self.assertIn('<h1>This is the Home Page!</h1>', response.body)
        self.assertIn('<p>24 bytes retrieved from backend 1, 20 bytes from backend 2</p>', response.body)
        self.assertNotIn('Error', response.body)



class MockDataStore(object):
    "Mock datastore"

    def __init__(self):
        "Initialise mock store"
        self.mock_google_response = None
        self.mock_yahoo_response = None

    @tornado.gen.coroutine
    def get_google(self):
        "Mock get google content"
        raise tornado.gen.Return(self.mock_google_response)

    @tornado.gen.coroutine
    def get_yahoo(self):
        "Mock get yahoo content"
        raise tornado.gen.Return(self.mock_yahoo_response)


