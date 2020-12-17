import fileinput
import re
from dataclasses import dataclass, field

p = re.compile('^(\w+) ([+-]\d+)$')

instructions = []
for line in fileinput.input():
  m = p.match(line.strip())
  instructions.append((m.group(1), int(m.group(2))))
# print(instructions)

@dataclass
class State:
  acc: int = 0
  pc: int = 0
  visited: set = field(default_factory=frozenset)

def step(state, instructions) -> State:
  op, n = instructions[state.pc]
  visited = state.visited.union({state.pc})
  if op == 'acc':
    return State(state.acc + n, state.pc + 1, visited)
  elif op == 'jmp':
    return State(state.acc, state.pc + n, visited)
  elif op == 'nop':
    return State(state.acc, state.pc + 1, visited)
  else:
    raise RuntimeError("unrecoginzed op: " + op)

def execute(instructions):
  state = State()
  while True:
    next_state = step(state, instructions)
    if next_state.pc in next_state.visited:
      return state.acc
    state = next_state

print(execute(instructions))
