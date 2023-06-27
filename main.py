import paramiko
import os
import shutil

print(os.listdir('.'))
# Dane do logowania do serwera
host = ''
username = ''
password = ''
port = 22

# Funkcja wykonująca polecenia na serwerze SSH
def execute_ssh_command(command):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, port, username, password)
    stdin, stdout, stderr = client.exec_command(command)
    output = stdout.read().decode('utf-8')
    client.close()
    return output

# Logowanie przez SSH
command = 'ls -l'
output = execute_ssh_command(command)
print(output)

# Utworzenie folderu
folder_path =  '/home/przemyslawk/test1'
folder_path2 =  '/home/przemyslawk/test2'
if not os.path.exists(folder_path):
    os.makedirs(folder_path)
if not os.path.exists(folder_path2):
    os.makedirs(folder_path2)

# Wyświetlenie zawartości folderów
folder_content = os.listdir('/home/przemyslawk')
print(folder_content)

# Zmiana uprawnień folderu
os.chmod(folder_path, 0o755)

# Utworzenie pliku
file_path = os.path.join(folder_path2, 'file1.txt')
with open(file_path, 'w', encoding='utf-8') as file:
    file.write('To jest zawartość pliku')
    
# Zmiana uprawnień folderu
os.chmod(folder_path2, 0o777)

# Skopiowanie pliku
shutil.copy(file_path, folder_path)

# Usunięcie pliku
os.remove(file_path)


