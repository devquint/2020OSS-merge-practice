f = open("teams.txt", 'r')

names = []
ids = []

for line in f:
 args = line.split(' ')
 names.append(args[1])
 ids.append(args[0])


f.close()
