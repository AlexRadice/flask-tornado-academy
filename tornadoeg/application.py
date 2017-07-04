from datetime import datetime
import tornado.web
import tornado.ioloop
from mainhandler import MainHandler


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler)
    ])

if __name__ == '__main__':
    make_app().listen(7888)
    tornado.ioloop.IOLoop.instance().start()
        
