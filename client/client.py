import socket
HOST = '127.0.0.1'      # Endereco IP do Servidor
PORT = 5000             # Porta que o Servidor está
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as tcp:
    destino = (HOST, PORT)
    tcp.connect(destino)
    print('Para sair tecle X')
    mensagem = input('--> ')
    while mensagem != 'X':
        tcp.send(mensagem.encode())
        mensagem = input('--> ')
print('=== Saindo ===')
tcp.close()