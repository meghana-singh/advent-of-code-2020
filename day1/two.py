with open("input.txt") as f:
    s = sorted(list(map(int, f.readlines())))
    len = len(s)
    for i in range(len-3):
        sum = 2020 - s[i]
        j=i+1
        k=len-1
        while(j<k):
            if s[j]+s[k] == sum:
                print('one: {}'.format(s[i]))
                print('two {}'.format(s[j]))
                print('three {}'.format(s[k]))
                print('result: {}'.format(s[i] * s[j] * s[k]))
                exit('--------End------')
            if s[j] + s[k] < sum:
                j=j+1
            if s[j] + s[k] > sum:
                k=k-1
# Time complexity O(n^2)