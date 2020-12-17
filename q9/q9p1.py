import fileinput
from itertools import combinations

data = list(map(int, fileinput.input()))
preamble_length = 25
def valid(data, preamble_length, for_index):
  return set(map(sum, combinations(data[for_index-preamble_length:for_index], 2)))
def seek(data, preamble_length):
  for (index, n) in list(enumerate(data))[preamble_length:]:
    if n not in valid(data, preamble_length, index):
      return n
  raise RuntimeError("didn't find it")
print(seek(data, preamble_length))
