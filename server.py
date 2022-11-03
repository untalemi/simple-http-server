import socket
import os
port = 8000
mysock = socket.socket() 
mysock.bind(('localhost', port))
mysock.listen(5)


while True:
    os.system('cls')
    print('Servidor corriendo en el puerto: ', port)
    print('URL: http://127.0.0.1:8000/')
    con, addr = mysock.accept() 
    rquest = con.recv(1024).decode('utf-8')
    list = rquest.split(' ')    
 
    method = list[0] # metodo
    requesting_file = list[1] # nombre

    file = open('views/index.html', 'rb')
    
    response = file.read()
    file.close()

    header = 'HTTP/1.1 200 OK\n'
    mimetype='text/html'
    header += 'Content-Type: ' + str(mimetype) + '\n\n'

    final_response = header.encode('utf-8')
    final_response += response
    con.send(final_response)
    print('Client request ', requesting_file)
    print('Client method ', method)

    
    con.close()