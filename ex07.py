name = {1:'zhang', 3:'nai', 'a': 'tao', 3: 'neil', 4: 'tao', 1: 'Neil'}
print (name)

print (name.values())
print (name.keys())

b = set(name.values())
print (b)

c = set(name.keys())
print (c)

d = b&c
print (d)

diff = b^c
print (diff)
