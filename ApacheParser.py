import re


def parse_blocks(conf_str):
    parsed = re.findall(r'(<VirtualHost .+:\d+>(\n+|.+)+?</VirtualHost>)', conf_str, re.MULTILINE)
    hosts = []
    for host in parsed:
        hosts.append(host[0])

    return hosts


def parse_server_name(vhost):
    return re.search(r'ServerName[ ]*(.+)', vhost).group(1)
