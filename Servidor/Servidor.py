import socket

def receber_arquivo():
    # Criar um socket TCP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Vincular o socket à porta e IP do servidor
    server_socket.bind(('localhost', 12345))

    # Aguardar por conexões
    server_socket.listen(1)

    print("Aguardando conexão do cliente...")

    try:
        # Aceitar conexão do cliente
        conn, addr = server_socket.accept()
        print("Conexão estabelecida com", addr)

        # Receber nome do arquivo e conteúdo
        mensagem = b''
        while True:
            parte = conn.recv(1024)
            if not parte:
                break
            mensagem += parte

        nome_arquivo, conteudo_arquivo = mensagem.split(b'\n', 1)

        # Abrir o arquivo para escrita
        with open(nome_arquivo.decode(), 'wb') as file:
            # Escrever o conteúdo do arquivo
            file.write(conteudo_arquivo)

        print("Arquivo recebido e salvo com sucesso!")
    except Exception as e:
        print("Erro:", e)
    finally:
        conn.close()
        server_socket.close()

if __name__ == "__main__":
    receber_arquivo()
