# Sistema de Envio de Arquivo
Sistema simples de envio de arquivo utilizando um socket tcp com arquitetura cliente-servidor.

## Como usar:
- Em um terminal inicializar o servidor ```python3 Servidor.py```
- Colocar o arquivo que deseja enviar dentro do diretorio **Cliente**
- Em um terminal separado, rodar o comando ```python3 Cliente.py <ip-do-servidor> <arquivo>``` onde  **ip-do-servidor** é o ip da maquina rodando a instancia do servidor, caso este esteje rodando na mesma maquina que o cliente, pode utilizar ```localhost``` , **arquivo** é o nome do arquivo que deseja enviar, como por exemplo Arquivo.txt
