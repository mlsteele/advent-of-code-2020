import fileinput
import re
from collections import defaultdict

p1 = re.compile('^(.*) bags$')
p2 = re.compile('^(\d+) (.*) bags?$')

# bagtype contains -> (n, bagtype)
rules = defaultdict(list)
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
    rules[container].append((n, contained))
# print(rules)

def set_union(*args):
  if not args:
    return set()
  return set.union(*args)
def containment_count(container, inner=False):
  under = sum(n * containment_count(contained, inner=True)
    for (n, contained) in rules[container])
  if inner:
    return 1 + under
  return under

probe = "shiny gold"
print(containment_count(probe))
