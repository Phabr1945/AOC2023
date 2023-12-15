def d1p1():
    lst = open('day1.txt').read().split()
    alf = []
    for ltr in 'abcdefghijklmnopqrstuvwxyz':
        alf.append(ltr)
    for x in range(len(lst)):
        for char in alf:
            lst[x] = lst[x].replace(char, '')
    numls = []
    for x in range(len(lst)):
        numls.append(int(lst[x][0] + lst[x][-1]))
        print(sum(numls))
print(d1p1())