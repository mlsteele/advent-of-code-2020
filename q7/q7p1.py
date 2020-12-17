import fileinput
import re
from collections import defaultdict

p1 = re.compile('^(.*) bags$')
p2 = re.compile('^(\d+) (.*) bags?$')

# bagtype -> bagtype
contained_by = defaultdict(list)
for line in fileinput.input():
  if "no other bags" in line:
    continue
  parts = line.replace('contain', ',').split(',')
  parts = [part.strip().strip('.') for part in parts]
  m = p1.match(parts[0])
  container = m.group(1)
  for part in parts[1:]:
    m = p2.match(part)
    n, contained = int(m.group(1)), m.group(2)
    contained_by[contained].append(container)
# print(contained_by)

def set_union(*args):
  if not args:
    return set()
  return set.union(*args)
def containers_recursive(contained, inner=False):
  parents = contained_by[contained]
  parents_recursive = set_union(*(containers_recursive(p, inner=True) for p in parents))
  if inner:
    return set.union(parents_recursive, {contained})
  return parents_recursive

probe = "shiny gold"
print(len(containers_recursive(probe)))
