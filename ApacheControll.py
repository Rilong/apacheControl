from ApacheParser import parse_blocks

file = open('apache.txt', 'r')
data = file.read()
file.close()

print(parse_blocks(data))