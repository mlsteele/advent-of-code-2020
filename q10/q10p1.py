import fileinput
from collections import Counter

data = list(map(int, fileinput.input()))
def built_in(data):
  return max(data) + 3
data = [0] + sorted(data) + [built_in(data)]
deltas = [b - a for (a, b) in zip(data, data[1:])]
ctr = Counter(deltas)
print(ctr)
print(ctr[1] * ctr[3])
