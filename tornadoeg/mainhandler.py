from datetime import datetime
import tornado.web
import tornado.ioloop
import tornado.httpclient
import tornado.gen

class MainHandler(tornado.web.RequestHandler):
    "Handler for the root page"

    def initialize(self, datastore):
        "Initialise the request handler (called before each request)"
        self._datastore = datastore

    @tornado.gen.coroutine
    def get(self):
        "Respond to a GET request"
        print("START {} handling {}".format(self.__class__.__name__, self._request_summary()))

        response1, response2  = yield [tornado.gen.Task(self._datastore.get_google), self._datastore.get_yahoo()]

        if response1.error:
            response_text = "Error {} from backend".format(response1.error)
        elif response2.error:
            response_text = "Error {} from backend".format(response2.error)
        else:
            response_text = "{} bytes retrieved from backend 1, {} bytes from backend 2".format(response1.headers['Content-Length'], response2.headers['Content-Length'])

        self.finish("<html><body><h1>This is the Home Page!</h1>" + 
            "<p>{}</p>".format(response_text) +
            "<footer>Served at {}</footer>".format(datetime.now()) +
            "</body></html>")
        print("FINISH {} handling {}".format(self.__class__.__name__, self._request_summary()))
