with open('nginx_logs.txt') as x:
    data = []
    for line in x:
        splitted = line.split()
        data.append((splitted[0], splitted[5].replace('"', ''), splitted[6]))
print(data)