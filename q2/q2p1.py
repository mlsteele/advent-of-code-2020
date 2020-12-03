import fileinput
import re

p = re.compile('(\d+)-(\d+) (.): (.+)')

def process(entry):
  # entry: "1-3 a: abcde"
  m = p.match(entry)
  lower, upper, letter, password = int(m.group(1)), int(m.group(2)), m.group(3), m.group(4)
  ok = lower <= password.count(letter) <= upper
  return 1 if ok else 0
entries = list(fileinput.input())
print(sum(map(process, entries)))
