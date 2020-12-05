import sys
import re

required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
hcl_re = re.compile('^#[0-9a-f]{6}$')
ecl_choices = ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')
pid_re = re.compile('^[0-9]{9}$')
passports = [[kv.split(':')
  for kv in passport.split()]
  for passport in sys.stdin.read().strip().split('\n\n')]
def validate_hgt(v):
  if v[-2:] == 'cm':
    return 150 <= int(v[:-2]) <= 193
  elif v[-2:]:
    return 59 <= int(v[:-2]) <= 76
  else:
    return False
def validate(passport):
  if not set(kv[0] for kv in passport) >= set(required_fields):
    return False
  validators = {
    'byr': lambda v: 1920 <= int(v) <= 2002,
    'iyr': lambda v: 2010 <= int(v) <= 2020,
    'eyr': lambda v: 2020 <= int(v) <= 2030,
    'hgt': validate_hgt,
    'hcl': lambda v: hcl_re.match(v),
    'ecl': lambda v: v in ecl_choices,
    'pid': lambda v: pid_re.match(v),
    'cid': lambda v: True,
  }
  # list(print(k, v, validators[k](v)) for (k, v) in passport)
  return all(validators[k](v) for (k, v) in passport)
list(map(print, passports))
print(list(map(validate, passports)))
print(sum(1 if validate(p) else 0 for p in passports))
