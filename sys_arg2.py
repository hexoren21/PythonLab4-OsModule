import sys

def say_it(greeting, name):
    message = f'{greeting} {name}'
    print(message)

if __name__ == '__main__':
    greeting = 'Witaj'
    target = 'Janusz'

if '--help' in sys.argv:
    help_message = f"Sposób użycia: {sys.argv[0]} --name <IMIĘ> --greeting <POWITANIE>"
    print(help_message)
    sys.exit()
    
if '--name' in sys.argv:
    name_index = sys.argv.index('--name') + 1
    if name_index < len(sys.argv):
        name = sys.argv[name_index]
    
    if '--greeting' in sys.argv:
        greeting__index = sys.argv.index('--greeting') + 1
    
    if greeting__index < len(sys.argv):
        greeting = sys.argv[greeting__index]
        
say_it(greeting, name)