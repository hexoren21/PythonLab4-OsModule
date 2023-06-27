import paramiko

# Dane logowania SSH
host = ''
port = 22
username = ''
password = ''

# Inicjalizacja klienta SSH
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Logowanie do hosta
ssh.connect(host, port, username, password)

# Tworzenie folderu
ssh.exec_command('mkdir folder1')

stdin, stdout, stderr = ssh.exec_command('ls')
print(stdout.read().decode())

# Zmiana uprawnień folderu
ssh.exec_command('chmod 755 folder1')

# Tworzenie pliku
ssh.exec_command('echo "to jest jakis tekst" > folder1/file.txt')
stdin, stdout, stderr = ssh.exec_command('cat folder1/file.txt')
print(stdout.read().decode())

# Kopiowanie pliku
ssh.exec_command('mkdir folder2 && cp folder1/file.txt folder2/file2.txt')

#usuniecie pliku
ssh.exec_command('rm -r folder1')

ssh.close