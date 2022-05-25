from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from app import app    
http_server = HTTPServer(WSGIContainer(app))

# 单进程模式，5000为端口，
http_server.listen(5000)   

# 3为进程数，不开的话就是单进程，0和负数是开cpu能开的进程数
# http_server.start(num_processes=3)
IOLoop.instance().start()


# 多进程还是比较建议下面这种方式

from tornado.netutil import bind_sockets
from tornado.process import fork_processes

# sockets = bind_sockets(5000)
# fork_processes(3)
# server = HTTPServer(WSGIContainer(app))
# server.add_sockets(sockets)
# IOLoop.instance().start()