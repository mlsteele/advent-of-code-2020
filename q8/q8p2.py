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

# return (whether it halted, accumulator)
def execute(instructions):
  state = State()
  while True:
    if state.pc >= len(instructions):
      if state.pc == len(instructions):
        return (True, state.acc)
      raise RuntimeError("ran way out of bounds")
    next_state = step(state, instructions)
    if next_state.pc in next_state.visited:
      return (False, state.acc)
    state = next_state

def toggle(instructions, index):
  op, n = instructions[index]
  if op == 'nop':
    op = 'jmp'
  elif op == 'jmp':
    op = 'nop'
  return instructions[:index] + [(op, n)] + instructions[index+1:]

def corruptions(instructions):
  return [toggle(instructions, index) for index in range(len(instructions))]

def fixup(instructions):
  for program in corruptions(instructions):
    halted, acc = execute(program)
    if halted:
      return acc
  raise RuntimeError("could not fix program")

print(fixup(instructions))
