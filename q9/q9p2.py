import fileinput
from itertools import combinations, count

data = list(map(int, fileinput.input()))
preamble_length = 25
def valid(data, preamble_length, for_index):
  return set(map(sum, combinations(data[for_index-preamble_length:for_index], 2)))
def seek_rebel(data, preamble_length):
  for (index, n) in list(enumerate(data))[preamble_length:]:
    if n not in valid(data, preamble_length, index):
      return n
  raise RuntimeError("didn't find it")
rebel_value = seek_rebel(data, preamble_length)

def find_rebel_contig():
  for span in count(start=2):
    for index in range(len(data)):
      contig = data[index:index+span]
      if sum(contig) == rebel_value:
        return contig

def sum_minmax(xs):
  return min(xs) + max(xs)

print(sum_minmax(find_rebel_contig()))
