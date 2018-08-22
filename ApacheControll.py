from ApacheParser import *
file = open('apache.txt', 'r')
data = file.read()
file.close()

print(create_host('test.local', '/home/rilong/www/test.local/public_html'))