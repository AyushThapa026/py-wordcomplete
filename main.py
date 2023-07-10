import json

file = open('popular.txt', 'r')

#data = json.load(file)

keyword = 'abs'


list = [s for s in file if s and s.startswith(keyword)]

print(list)