from math import sqrt
from operator import attrgetter
class Node:
    x=0
    y=0
    f_score=0
    g_score=0
    walkable=True

listche=[]
f = open("grid")
listche= f.readlines()
grid=[]
y = 0
for line in listche:
    line = line[:-1]
    line = map(lambda x: int(x), line)
    temp = []
    for x in range(len(line)):
        n = Node()
        n.x = x
        n.y = y
        n.walkable = (line[x] == 1)
        temp.append(n)
    grid.append(temp)
    y += 1

f.close()
end = grid[(len(grid))-1][-1]
start = grid[0][0]


def nearest_neshto(a,b):

    c=sqrt(pow((a.x-b.x),2)+(pow((a.y-b.y),2)))
    return c
p=[]
def r_path(dic, point):
    if point in dic:
        if isinstance(r_path(dic,dic[point]), Node):
            p.append(r_path(dic, dic[point]))
        return p.append(point)
    else:
        return point

def notnula(a):
    return a.walkable == True

def neigh_nodes(a, grid):
    nodes=[]
    if a.x+1 < len(grid[0]):
        if notnula(grid[a.y][a.x+1]):

            nodes.append(grid[a.y][a.x+1])
    if a.x-1 > -1:
        if notnula(grid[a.y][a.x-1]):
            nodes.append(grid[a.y][a.x-1])
    if a.y+1 < len(grid):
        if notnula(grid[a.y+1][a.x]):
            nodes.append(grid[a.y+1][a.x])
    if a.y-1 > -1:
        if notnula(grid[a.y-1][a.x]):
            nodes.append(grid[a.y-1][a.x])
    return nodes


def astar(start, end, grid):
    closed_set=set([])
    open_set=set([start])
    dic={}
    start.g_score=0
    start.f_score=start.g_score+nearest_neshto(start,end)

    while len(open_set) > 0:
        current = min(open_set, key=attrgetter("f_score"))
        if current == end:
            return r_path(dic,end)
        open_set.remove(current)
        closed_set.add(current)
        neigs = neigh_nodes(current, grid)
       # print '---------------'
       # for n in neigs:
       #     print n.x, n.y
       # print '---------------'
        for a in neigh_nodes(current, grid):
            if a in closed_set:
                continue
            t_g_score = current.g_score+1

            if a not in open_set or t_g_score < current.g_score:
                dic[a] = current
                a.g_score = t_g_score
                a.f_score = a.g_score+nearest_neshto(a, end)
                if a not in open_set:
                    open_set.add(a)

    return

astar(start, end, grid)
for el in p:
    print (el.x, el.y),

