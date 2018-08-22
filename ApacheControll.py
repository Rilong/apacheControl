from ApacheParser import *
from functions import *
from pathlib import Path

HOME = str(Path.home())
WWW = HOME + 'www'
VHOSTS = '/opt/lampp/etc/extra/httpd-vhosts.conf'

print('Welcome!')
print('====Commands====')
print('add - Add site')
print('remove - Add site')
print('exit - Exit from program')
print('================')

cmd = ''
while cmd != 'exit':
    cmd = input('Command: ')

    if cmd == 'add':
        site_name = input('Site name: ')

        yn = input('Are you sure want do it? (y/n) ')

        while True:
            if yn.lower() == 'y' or yn.lower() == 'n':
                break
            yn = input('Are you sure want do it? (y/n) ')

        if yn == 'y':
            pass
        else:
            pass