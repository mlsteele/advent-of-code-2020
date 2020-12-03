import fileinput
from itertools import combinations

entries = list(map(int, fileinput.input()))
pairs = combinations(entries, 3)
print([x*y*z for x,y,z in pairs if x+y+z == 2020])
