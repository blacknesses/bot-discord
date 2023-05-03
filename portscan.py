import socket
import os
import sys

os.system("clear")

def scan(host, ports):
    try:
        for port in ports:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.settimeout(0.05)
            conexao = client.connect_ex((host, int(port)))
            if conexao == 0:
                print("[+] {} open".format(port))
    except:
        print("Algum erro ocorreu.")
        
if __name__ == "__main__":
    if len(sys.argv) >= 2:
        host = sys.argv[1]
        if len(sys.argv) >=3:
            ports = sys.argv[2].split(",")
        else:
            ports = [21, 22, 23, 25, 80, 443, 445, 8080, 8443, 3306, 139, 135]
        scan(host, ports)
    else:
        print("sintaxe: python3 portscan.py google.com range")
