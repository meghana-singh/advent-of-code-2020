import csv
with open('input.csv') as f:
    reader = csv.reader(f, delimiter=' ')
    pwd_policy = {}
    count = 0
    for row in reader:
        l = int(row[0].split('-')[0])
        u = int(row[0].split('-')[1])
        letter = row[1].split(':')[0]
        n = row[2].count(letter)
        pwd_policy[letter] = False
        if (n>=l and n<=u):
            pwd_policy[letter] = True
            count = count+1
    print(pwd_policy)
    print(count)