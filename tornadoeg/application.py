from datetime import datetime
import tornado.web
import tornado.ioloop
from datastore import DataStore
from mainhandler import MainHandler


def make_app():
    servicesDict={'datastore': DataStore()}
    return tornado.web.Application([
        (r"/", MainHandler, servicesDict)
    ])

if __name__ == '__main__':
    make_app().listen(7888)
    tornado.ioloop.IOLoop.instance().start()
        
