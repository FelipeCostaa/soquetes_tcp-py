import socket
HOST = '127.0.0.1'      # Endereco IP do Servidor
PORT = 5000             # Porta que o Servidor está
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as tcp:   # AF_INET e SOCK_STREAM são constantes
    destino = (HOST, PORT)
    tcp.connect(destino)    # Conecta a um socket remoto
    print('Para sair tecle X')
    mensagem = input('--> ')
    while mensagem != 'X':
        tcp.send(mensagem.encode())     # .send Envia a msg e .encode codifica a string
        mensagem = input('--> ')
print('=== Saindo ===')
tcp.close()     # Fecha a conexão com o socket
