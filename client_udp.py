import socket
import sys
import os
# variavel = socket.metodo(familia, tipo)
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

os.system("clear")
try:
    host = input('')
    porta = input()
    port = int(porta)
except:
    print("sintaxe: python3 client_udp.py\nIP\nPORT\nMSG DE TESTE\n")
    sys.exit()

try:
    while True:
        # conexão/enviando dados
        msg = input("Localhost: ") + f'\n'
        client.sendto(msg.encode(), (host, port))

        # recebendo e exibindo dados
        data, sender = client.recvfrom(1024)
        print(sender[0] + ": " + data.decode())

        # verificação de encerramento do chat
        if data.decode() == 'sair\n' or msg == 'sair\n':
            break
    client.close()
except Exception as error:
    print('Erro: ', error)
    client.close()
