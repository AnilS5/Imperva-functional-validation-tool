import os
import shutil
from datetime import date

backup = date.today()
username = os.getenv('username')

def hostEntry(*args):
    shutil.copy('C:\Windows\System32\drivers\etc\hosts', r'C:\Users\{}\Documents\hosts_{}'.format(username, backup))
    with open('C:\Windows\System32\drivers\etc\hosts', 'w') as file:
        if len(args[0]) > 1:
            file.writelines('{0} {1}\n{0} {2}'.format(args[1], args[0][0], args[0][1]))
        else:
            file.writelines('{0} {1}'.format(args[1], args[0][0]))


def call_back():
    shutil.move(r'C:\Users\{}\Documents\hosts_{}'.format(username, backup), r'C:\Windows\System32\drivers\etc\hosts')



