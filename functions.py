def read_apache_file(file):
    a_file = open(file, 'r')
    a_content = a_file.read()
    a_file.close()
    return a_content


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


def isConfirm():
    yn = input('Are you sure want do it? (y/n) ')

    while True:
        if yn.lower() == 'y' or yn.lower() == 'n':
            break
        yn = input('Are you sure want do it? (y/n) ')

    if yn == 'y':
        return True
    else:
        return False
