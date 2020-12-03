import fileinput
import re

p = re.compile('(\d+)-(\d+) (.): (.+)')

def process(entry):
  # entry: "1-3 a: abcde"
  m = p.match(entry)
  p1, p2, letter, password = int(m.group(1)), int(m.group(2)), m.group(3), m.group(4)
  ok = (password[p1-1] == letter) != (password[p2-1] == letter)
  return 1 if ok else 0
entries = list(fileinput.input())
print(sum(map(process, entries)))
