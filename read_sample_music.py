# READ  file TXT
with open('samples/user.txt', 'r') as file:
    lines = file.readlines()
    for n, line in enumerate(lines):
        line = line.split()
        print(line)
# print(contenu.replace(" ", ","))
