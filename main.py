import paramiko
import re
# Dane do logowania do serwera
host = '10.97.190.4'
username = 'przemyslawk'
password = 'atu7Xoo!'

# Ścieżka do pliku dziennika
log_path = '/var/log/apache2/access.log.1'

# Tworzenie obiektu klienta SSH
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())


try:
    # logowanie do serwera
    client.connect(hostname=host, username=username, password=password)
    
    # Otwieranie połączenia FTP
    ftp = client.open_sftp()

    # Zamykanie połączenia FTP
    ftp.close()

finally:
    # Zamykanie połączenia SSH
    client.close()