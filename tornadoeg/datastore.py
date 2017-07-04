import tornado.httpclient
import tornado.gen

class DataStore(object):
    "Data store class"

    @tornado.gen.engine
    def get_google(self, callback=None):
        "Get data from www.google.com"
        http_client = tornado.httpclient.AsyncHTTPClient()
        print("START Backend fetch from www.google.com  ....")
        response  = yield http_client.fetch('http://www.google.com')
        print("FINISH Backend fetch from www.google.com response status={}".format(response.code))
        callback(response)

    @tornado.gen.coroutine
    def get_yahoo(self):
        "Get data from search.yahoo.com"
        http_client = tornado.httpclient.AsyncHTTPClient()
        print("START Backend fetch from search.yahoo.com  ....")
        response  = yield http_client.fetch('http://search.yahoo.com')
        print("FINISH Backend fetch from search.yahoo.com response status={}".format(response.code))
        raise tornado.gen.Return(response)
