import fileinput
from operator import mul
from functools import reduce

rows = [line.strip() for line in fileinput.input()]
def slope(right=3, down=1):
  return sum(row[(y * right // down) % len(row)] == '#'
    for y, row in enumerate(rows)
    if y % down == 0)
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
product = lambda xs: reduce(mul, xs, 1)
print(product(slope(*xs) for xs in slopes))
