import socket
import os

class SimpleHttpServer:
    def __init__(self) -> None:
        self.port = 8000
        self.mysock = socket.socket() 
        
    def connect(self):
        self.mysock.bind(('localhost', self.port))
        self.mysock.listen(5)

        os.system('cls')
        print('Servidor corriendo en el puerto: ', self.port)
        print(f'URL: http://127.0.0.1:{self.port}/')
        
        self.con, addr = self.mysock.accept() 
        
        rquest = self.con.recv(1024).decode('utf-8')
        
        list = rquest.split(' ')    

        self.method = list[0] # metodo
        self.requesting_file = list[1] # nombre
        
    def simpleRuta(self, ruta):
        file = open(f'views/{ruta}', 'rb')
        response = file.read()
        file.close()

        header = 'HTTP/1.1 200 OK\n'
        mimetype='text/html'
        header += 'Content-Type: ' + str(mimetype) + '\n\n'

        final_response = header.encode('utf-8')
        final_response += response
        self.con.send(final_response)


        print('Client request ', self.requesting_file)
        print('Client method ', self.method)

    
        self.con.close()

        return ruta