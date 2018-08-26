import re


def parse_blocks(conf_str):
    parsed = re.findall(r'(<VirtualHost .+:\d+>(\n+|.+)+?</VirtualHost>)', conf_str, re.MULTILINE)
    hosts = []
    for host in parsed:
        hosts.append(host[0])

    return hosts


def parse_server_name(vhost):
    return re.search(r'ServerName[ ]*(.+)', vhost).group(1)


def parse_server_root(vhost):
    return re.search(r'DocumentRoot[ ]*"(.+)"', vhost).group(1)


def parse_hosts(hosts):
    localhosts = re.search(r'#===\n(.+(\n|.)+)#===', hosts).group(1)
    parsed_hosts = re.findall(r'([0-9.]+\s+.+)', localhosts)
    return parsed_hosts
