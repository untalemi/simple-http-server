from SimpleHttpServer import SimpleHttpServer

server = SimpleHttpServer()
server.connect()

@server.simpleRuta('index.html')
def index():
    pass
