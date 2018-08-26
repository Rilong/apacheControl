import re

def read_file(file):
    a_file = open(file, 'r')
    a_content = a_file.read()
    a_file.close()
    return a_content


def write_apache_file(blocks, file):
    a_file = open(file, 'w')
    for block in blocks:
        a_file.write(block)
        a_file.write('\n\n')
    a_file.close()


def create_host(server_name, root, host='*'):
    mackup = '''<VirtualHost ''' + host + ''':80>
    ServerName ''' + server_name + '''
    DocumentRoot "''' + root + '''"
    <Directory "''' + root + '''">
        DirectoryIndex index.php
        AllowOverride All
        Order allow,deny
        Allow from all
    </Directory>
</VirtualHost>'''

    return mackup


def is_confirm(message='Are you sure want do it? (y/n) '):
    yn = input(message)

    while True:
        if yn.lower() == 'y' or yn.lower() == 'n':
            break
        yn = input('Are you sure want do it? (y/n) ')

    if yn == 'y':
        return True
    else:
        return False


def write_host(hosts_dir, hosts):
    file_read = read_file(hosts_dir)
    hoststr = ''
    for host in hosts:
        hoststr += host + '\n'
    file_write = open(hosts_dir, 'w')
    host_content = re.sub('#===\n(.+(\n|.)+)#===', '#===\n' + hoststr + '#===', file_read)
    file_write.write(host_content)
    file_write.close()