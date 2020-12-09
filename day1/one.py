target = {}
with open("input.txt") as f:
    nums = list(map(int, f.readlines()))
for n in nums:
    s = 2020 - n
    if target.get(s):
        print('one: {}'.format(n))
        print('two: {}'.format(s))
        print('result: {}'.format(n * s))
        exit('--------End------')
    target[n] = True
# Time complexity O(n)