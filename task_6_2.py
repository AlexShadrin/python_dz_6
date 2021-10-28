with open('nginx_logs.txt') as y:
    data = []
    spam_address = {}
    for line in y:
        splitted = line.split()
        data.append((splitted[0], splitted[5].replace('"', ''), splitted[6]))
        spam_address.setdefault(splitted[0], 0)
        spam_address[splitted[0]] += 1
spam_address = sorted(spam_address.items(), key=lambda x: x[1], reverse=True)
print(spam_address[:5])