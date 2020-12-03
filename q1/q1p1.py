import fileinput
from itertools import combinations

entries = list(map(int, fileinput.input()))
pairs = combinations(entries, 2)
print([x*y for x, y in pairs if x+y == 2020])
