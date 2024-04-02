import socket
import sys

def enviar_arquivo(ip_servidor, nome_arquivo):
    # Criar um socket TCP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Conectar ao servidor
        client_socket.connect((ip_servidor, 12345))

        # Abrir o arquivo e ler o conteúdo
        with open(nome_arquivo, 'rb') as file:
            conteudo_arquivo = file.read()

        # Enviar nome do arquivo e conteúdo ao servidor
        client_socket.send(nome_arquivo.encode() + b'\n' + conteudo_arquivo)

        print("Arquivo enviado com sucesso!")
    except Exception as e:
        print("Erro:", e)
    finally:
        client_socket.close()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python3 cliente.py <ip-do-servidor> <arquivo>")
        sys.exit(1)

    ip_servidor = sys.argv[1]
    nome_arquivo = sys.argv[2]

    enviar_arquivo(ip_servidor, nome_arquivo)
