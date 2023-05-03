import paramiko

host = input("")
user = input("")
passwd = input("")

cliente = paramiko.SSHClient()
cliente.set_missing_host_key_policy(paramiko.AutoAddPolicy)
cliente.connect(host, username=user, password=passwd)

while True:
    stdin, stdout, stderr = cliente.exec_command(input("comando: "))
    for line in stdout.readlines():
        print(line.strip())

    erros = stderr.readlines()
    if erros:
        print(erros)