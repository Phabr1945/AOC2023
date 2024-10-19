import re

class range:
    def __init__(self, base=None):
        if base:
            self.spans = dict(base.spans)
        else:
            self.spans = {
                's':[1,4000],
                'a':[1,4000],
                'm':[1,4000],
                'x':[1,4000],
            }

    def apply(self, rule):
        val = int(rule[2])
        current = self.spans[rule[0]]
        if rule[1] == '<':
            self.spans[rule[0]] = [current[0],min(current[1],val-1)]
        else:
            self.spans[rule[0]] = [max(current[0],val+1),current[1],]

    def exclude(self, rule):
        val = int(rule[2])
        current = self.spans[rule[0]]
        if rule[1] == '>':
            self.spans[rule[0]] = [current[0], min(current[1], val)]
        else:
            self.spans[rule[0]] = [max(current[0], val), current[1], ]

    def combos(self):
        return (1 + self.spans['x'][1] - self.spans['x'][0]) * \
               (1 + self.spans['m'][1] - self.spans['m'][0]) * \
               (1 + self.spans['a'][1] - self.spans['a'][0]) * \
               (1 + self.spans['s'][1] - self.spans['s'][0])

    def check(self, x, m, a, s):
        if x >= self.spans['x'][0] and x <= self.spans['x'][1] and \
            m >= self.spans['m'][0] and m <= self.spans['m'][1] and \
            a >= self.spans['a'][0] and a <= self.spans['a'][1] and \
            s >= self.spans['s'][0] and s <= self.spans['s'][1]:
            return (x+m+a+s)
        else:
            return 0

part_one = True
rules = {}
accepts = []

def process(rules,accepts,base,label):
    start = rules[label]
    default_rule = range(base)
    for rule in start[0]:
        x = range(default_rule)
        x.apply(rule)
        default_rule.exclude(rule)
        if rule[3] == 'A':
            accepts.append(x)
        elif rule[3] != 'R':
            process(rules,accepts,x,rule[3])
    if start[1] == 'A':
        accepts.append(default_rule)
    elif start[1] != 'R':
        process(rules,accepts,default_rule,start[1])

answer = 0
for line in open("day19.txt").readlines():
    if not line.strip():
        part_one = False
        process(rules,accepts,None,"in")
    elif part_one:
        directives = re.findall(r"([a-z]+)([<>])([0-9]+)\:([a-zA-Z]+)",line)
        default = re.search(r",([a-zA-Z]+)}",line).groups()[0]
        label = re.search(r"([a-z]+){",line).groups()[0]
        rules[label] = (directives,default)
    else:
        vals = list(map(int,re.findall(r"([0-9]+)",line)))
        match = 0
        for possible in accepts:
            match = possible.check(*vals)
            answer += possible.check(*vals)
print(answer)

answer = 0
for possible in accepts:
    answer += possible.combos()
print(answer)