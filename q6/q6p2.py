import sys

groups = [group.split() for group in sys.stdin.read().strip().split('\n\n')]
group_sets = [set.intersection(*(set(person) for person in group)) for group in groups]
x = sum(list(map(len, group_sets)))
print(x)
