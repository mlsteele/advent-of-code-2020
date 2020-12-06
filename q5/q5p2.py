import fileinput
from functools import reduce

# BFFFBBFRRR: row 70, column 7, seat ID 567.
# FFFBBBFRRR: row 14, column 7, seat ID 119.
# BBFFBBFRLL: row 102, column 4, seat ID 820.

total_seats = 128 * 8
seats = [line.strip() for line in fileinput.input()]
to_bits = lambda str, zero, one: [{zero: 0, one: 1}[x] for x in str]
bits_to_num = lambda bits: reduce(lambda acc, b: acc*2 + b, bits, 0)
mk_seat_id = lambda row, column: row * 8 + column
def process(seat):
  row = bits_to_num(to_bits(seat[:-3], 'F', 'B'))
  column = bits_to_num(to_bits(seat[-3:], 'L', 'R'))
  return (row, column, mk_seat_id(row, column))
seats2 = list(map(process, seats))
all_seats = set(range(0,total_seats+1))
taken_seats = set(seat_id for (row, column, seat_id) in seats2)
print(sorted(all_seats - taken_seats))
