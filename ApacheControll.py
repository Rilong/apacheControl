import os
from ApacheParser import *
from functions import *
from pathlib import Path
from shutil import rmtree

HOME = str(Path.home())
WWW = HOME + '/www'
VHOSTS = '/opt/lampp/etc/extra/httpd-vhosts.conf'
HOSTS = '/etc/hosts'

print('Welcome!')
print('====Commands====')
print('add - Add site')
print('remove - Add site')
print('list - List sites')
print('exit - Exit from program')
print('================')

cmd = ''
hosts_content = read_file(HOSTS)
sys_hosts = parse_hosts(hosts_content)
sites_blocks = parse_blocks(read_file(VHOSTS))
while cmd != 'exit':
    cmd = input('Command: ')

    if cmd == 'add':
        server_name = input('Server name: ')
        server_root = WWW + '/' + server_name + '/public_html'
        if isConfirm():
            sites_blocks.append(create_host(server_name, server_root))
            if not os.path.exists(server_root):
                if isConfirm('Are you want to create directory ' + server_root + '? (y/n) '):
                    os.makedirs(server_root)
                    print('Directory ' + server_root + ' is created')
            print('Virtual host is created')

            file = open('apache.txt', 'w')

            print('Write in file httpd_vhosts...')
            write_apache_file(sites_blocks, VHOSTS)
            sys_hosts.append('127.0.0.1\t' + server_name)
            print('Write in file hosts...')
            write_host(HOSTS, sys_hosts)
            print('Write in file httpd_vhosts is done')
            print('Write in file hosts is done')
            print('Done!')
        else:
            pass
    elif cmd == 'remove':
        site_index = int(input('Type num site here: ')) - 1

        if isConfirm():
            site_dir = WWW + '/' + parse_server_name(sites_blocks[site_index])
            del sites_blocks[site_index]
            if os.path.exists(site_dir):
                rmtree(site_dir)
                print('Site directory is deleted')
            write_apache_file(sites_blocks, VHOSTS)
            print('Site is removed')
            print('Write in file is done')
            print('Done!')

    elif cmd == 'list':
        i = 1
        for site_block in sites_blocks:
            print('[' + str(i) + ']', parse_server_name(site_block))
            i += 1