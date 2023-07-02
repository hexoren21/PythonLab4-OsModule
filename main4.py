import os

print(os.getcwd())
os.makedirs('C:\\temp', exist_ok=True)
os.chdir('C:\\temp')

print(os.getcwd())

print(os.environ.get('LOGLEVEL'))
os.environ['LOGLEVEL'] = 'DEBUG'
print(os.environ.get('LOGLEVEL'))

print(os.getlogin())