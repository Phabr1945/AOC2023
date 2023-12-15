#fs = open("day2.txt", "r")
#fss = open("day2.txt").read().split()
#class gameinfo:
#    id = int
#    red = int
#    green = int
#    blue = int
#    fs.readlines()
#
#solution2 = int(0)
#solution1 = int(0)
#
#def r():
#    if info.red > 12:
#        return True
#def g():
#    if info.green > 13:
#        return True
#def b():
#    if info.blue > 14:
#        return True
#
#for line in fss:
#    info = gameinfo()
#    if r and g and b:
#        solution1 += info.id


from collections import defaultdict
D = open("day2.txt").read().strip()
p1 = 0
p2 = 0
#only 12 red cubes, 13 green cubes, and 14 blue cubes?
for line in D.split('\n'):
  ok = True
  id_, line = line.split(':')
  V = defaultdict(int)
  for event in line.split(';'):
    for balls in event.split(','):
      n,color = balls.split()
      n = int(n)
      V[color] = max(V[color], n)
      if int(n) > {'red': 12, 'green': 13, 'blue': 14}.get(color, 0):
        ok = False
  score = 1
  for v in V.values():
    score *= v
  p2 += score
  if ok:
    p1 += int(id_.split()[-1])
print(p1)
print(p2)

        #def d2p1():
#    r = "r"
#    g = "g"
#    lst = open("day2.txt").read().split()
#    for x in range(len(lst)):
#        for character in lst:
#            if character.isdigit():
#                number = int(character)
#                if number < 14:
#                    print("The input contains an integer less than 14.")
#                    def red():
#                        return True, r in str
#                    def green():
#                        return True, g in str
#                    if red and green:
#                        print(x)
#            else:
#                print("idiot.")
#                break
#
#d2p1()
