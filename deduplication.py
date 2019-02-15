f = open("url.txt", 'r')
f1 = open("url1.txt", 'w')
lines = f.readlines()
line = set(lines)
for string in line:
    f1.write(string)
f.close()
f1.close()