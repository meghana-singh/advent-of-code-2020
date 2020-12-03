import csv
with open('input.csv') as f:
    reader = csv.reader(f, delimiter=' ')
    pwd_policy = {}
    count = 0
    for row in reader:
        l = int(row[0].split('-')[0])
        u = int(row[0].split('-')[1])
        letter = row[1].split(':')[0]
        indexes = [i+1 for i, char in enumerate(row[2]) if char == letter]
        pwd_policy[letter] = False
        if indexes:
            if (l in indexes) ^ (u in indexes):
                pwd_policy[letter] = True
                count = count + 1
    print(pwd_policy)
    print(count)