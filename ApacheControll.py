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
print('list - List sites')
print('exit - Exit from program')
print('================')

cmd = ''
sites_list = parse_blocks(read_apache_file('apache.txt'))
while cmd != 'exit':
    cmd = input('Command: ')

    if cmd == 'add':
        site_name = input('Site name: ')

        if isConfirm():
            pass
        else:
            pass
    elif cmd == 'remove':
        site_index = int(input('Type num site here: ')) - 1

        if isConfirm():
            del sites_list[site_index]

        print(sites_list)
    elif cmd == 'list':
        i = 1
        for site_block in sites_list:
            print('[' + str(i) + ']', parse_server_name(site_block))
            i += 1