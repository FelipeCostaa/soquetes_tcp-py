import socket
HOST = ''               # Endereco IP do Servidor
PORT = 5000             # Porta que o Servidor está
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)     # AF_INET e SOCK_STREAM são constantes
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)           # Habilita o servidor para aceitar conexões
print('=== Servidor iniciado ===')
while True:
    con, cliente = tcp.accept()     # Aceita uma conexão
    print('*** Conectado por', cliente)
    while True:
        mensagem = con.recv(1024).decode()   # Recebe dados do socket
        if not mensagem:
            break
        print(cliente, mensagem)
    print('*** Finalizando conexao do cliente', cliente)
    con.close()                     # Fecha a conexão com o socket
