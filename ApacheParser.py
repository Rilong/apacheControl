import re


def parse_blocks(conf_str):
    parsed = re.findall(r'(<VirtualHost .+:\d+>(\n+|.+)+?</VirtualHost>)', conf_str, re.MULTILINE)
    hosts = []
    for host in parsed:
        hosts.append(host[0])

    return hosts

# add comment
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