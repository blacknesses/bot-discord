# importando biblioteca de conexões
import socket
import os
# varivel = objeto.metodo(familia,tipo)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

os.system("clear")
#tratando input do usuario
try:
    host = input('')
    porta = input()
    port = int(porta)
except:
    print("sintaxe: python3 client_tcp.py\nIP\nPORT\nMSG\n")
    
# variavel.metodo(tupla) --> conexão
client.connect((host, port))

try:
    while True:
        
        # envio de dados
        # client.send("conectado !!!".encode())
        msg = input("localhost: ") + f'\n'
        client.send(bytes(msg, "utf-8"))
        
        # recepção de dados
        data = client.recv(1024)
        print(f"remote host: {data}")
        
        
        #verificação de encerramento do chat
        if data.decode() == 'sair\n' or msg == 'sair\n':
            break
    client.close()
except Exception as error:
    print("Erro: ", error)
    client.close()
