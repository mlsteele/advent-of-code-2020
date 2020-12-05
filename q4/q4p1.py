import sys

required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
passports = [[kv.split(':')
  for kv in passport.split()]
  for passport in sys.stdin.read().strip().split('\n\n')]
def validate(passport):
  return set(kv[0] for kv in passport) >= set(required_fields)
list(map(print, passports))
print(list(map(validate, passports)))
print(sum(1 if validate(p) else 0 for p in passports))
