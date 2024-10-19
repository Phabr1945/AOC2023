mirrors = open('day16.txt').read().split()

# A beam consists of a location (x,y) and a direction of travel (dx,dy).
# It moves (and sometimes splits).
class beam:
    def __init__(self, x, y, dx, dy):
        self.x, self.y = x,y
        self.dx, self.dy = dx,dy

    def move(self):
        m = mirrors[self.y][self.x]
        if m == '-' and self.dy != 0: # split - return new beams                 
            return [beam(self.x,self.y,-1,0), beam(self.x,self.y,+1,0)]
        elif m == '|' and self.dx != 0: # split - return new beams                
            return [beam(self.x,self.y,0,-1), beam(self.x,self.y,0,+1)]
        elif m == '/':
            t = self.dx
            self.dx = -self.dy
            self.dy = -t
        elif m == '\\': 
            t = self.dx
            self.dx = self.dy
            self.dy = t

        self.x += self.dx
        self.y += self.dy
        return [self] # the old beam is still moving

    # A useful representation of a beam
    def __repr__(self):
        s = '('+str(self.x)+','+str(self.y)+')'+'\''+mirrors[self.y][self.x]+'\''
        match (self.dx,self.dy):
            case (1,0):
                s += '>'
            case (-1,0):
                s += '<'
            case (0,1):
                s += 'v'
            case (0,-1):
                s += '^'
        return s


def get_energized_count(x,y,dx,dy):
    beams = [beam(x,y,dx,dy)]
    energized = {(x,y,dx,dy)} # energized also has the direction, to avoid beam duplication

    while beams != []:
        newbeams = []
        for b in beams:
            energized.add((b.x,b.y,b.dx,b.dy))
            newbeams += b.move()
        beams = [b for b in newbeams
                 if b.x >= 0 and b.x < len(mirrors[0]) and b.y >= 0 and b.y < len(mirrors) # on grid
                 and (b.x,b.y,b.dx,b.dy) not in energized] # this location/direction is new

    return len({(x,y) for (x,y,_,_) in energized}) # only one direction for each (x,y)

print("Part 1 - energized:", get_energized_count(0,0,+1,0))


maxen = 0
for y in range(len(mirrors)):
    mplus = get_energized_count(0,y,+1,0)
    mminus = get_energized_count(len(mirrors[0])-1,y,-1,0)
    maxen = max(maxen,mplus,mminus)
                    
for x in range(len(mirrors[0])):
    mplus = get_energized_count(x,0,0,+1)
    mminus = get_energized_count(x,len(mirrors)-1,0,-1)
    maxen = max(maxen,mplus,mminus)

print("Part 2 - max energized:", maxen)
   
