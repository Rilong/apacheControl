import re


def parse_blocks(conf_str):
    return re.findall(r'(<VirtualHost .+:\d+>(\n+|.+)+?</VirtualHost>)', conf_str, re.MULTILINE)