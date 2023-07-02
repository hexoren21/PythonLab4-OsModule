import subprocess
import os
# cp = subprocess.run(['ls', '-l'], capture_output=True, universal_newlines=True)
cp = subprocess.run(['dir'], capture_output=True, shell=True, universal_newlines=True)
print(cp.stdout)
# cp = subprocess.run(['ls', '/doesnotexist'],
#                     capture_output=True,
#                     universal_newlines=True,
#                     check=True)
directory = '/doesnotexist'

if os.path.isdir(directory):
    cp = subprocess.run(['dir', directory],
                        capture_output=True,
                        shell=True,
                        universal_newlines=True,
                        check=True)
else:
    print(f"Katalog '{directory}' nie istnieje.")

