import socket
HOST = ''               # Endereco IP do Servidor
PORT = 5000             # Porta que o Servidor está
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(2)
print('=== Servidor iniciado ===')
while True:
    con, cliente = tcp.accept()
    print('*** Conectado por', cliente)
    while True:
        mensagem = con.recv(1024)
        if not mensagem:
            break
        print(cliente, mensagem)
    print('*** Finalizando conexao do cliente', cliente)
    con.close()
