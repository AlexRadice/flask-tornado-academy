from datetime import datetime
import tornado.web
import tornado.ioloop

class MainHandler(tornado.web.RequestHandler):
    "Handler for the root page"

    def get(self):
        "Respond to a GET request"
        print("START {} handling {}".format(self.__class__.__name__, self._request_summary()))
        self.write("<html><body><h1>This is the Home Page!</h1>" + 
            "<footer>Served at {}</footer>".format(datetime.now()) +
            "</body></html>")
        print("FINISH {} handling {}".format(self.__class__.__name__, self._request_summary()))
