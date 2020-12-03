import fileinput

rows = [line.strip() for line in fileinput.input()]
print(sum(row[(y * 3) % len(row)] == '#' for y, row in enumerate(rows)))
