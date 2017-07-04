from datetime import datetime
import tornado.web
import tornado.ioloop
import tornado.httpclient

class MainHandler(tornado.web.RequestHandler):
    "Handler for the root page"

    @tornado.web.asynchronous
    def get(self):
        "Respond to a GET request"
        print("START {} handling {}".format(self.__class__.__name__, self._request_summary()))
        http_client = tornado.httpclient.AsyncHTTPClient()
        print("START Backend fetch....")
        http_client.fetch('http://www.google.com', callback=self.on_respond)

    def on_respond(self, response):
        "Handle response to fetch from backend store"
        print("FINISH Backend fetch response status={}".format(response.code))
        if response.error:
            response_text = "Error {} from backend".format(response.error)
        else:
            response_text = "{} bytes retrieved from backend".format(response.headers['Content-Length'])

        self.finish("<html><body><h1>This is the Home Page!</h1>" + 
            "<p>{}</p>".format(response_text) +
            "<footer>Served at {}</footer>".format(datetime.now()) +
            "</body></html>")
        print("FINISH {} handling {}".format(self.__class__.__name__, self._request_summary()))
