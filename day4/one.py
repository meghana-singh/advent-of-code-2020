with open('input.txt') as f:
    rows = f.read().splitlines()
passport = {}
valid_count = 0
for row in rows:
    if row != '':
        for r in row.split(' '):
            passport[r.split(':')[0]] = True
    elif row == '':
        if (passport.has_key('ecl') and passport.has_key('pid') and
            passport.has_key('eyr') and passport.has_key('hcl') and
            passport.has_key('byr') and passport.has_key('iyr') and
            passport.has_key('hgt')):
            valid_count = valid_count + 1
        passport = {}
if (passport.has_key('ecl') and passport.has_key('pid') and
    passport.has_key('eyr') and passport.has_key('hcl') and
    passport.has_key('byr') and passport.has_key('iyr') and
    passport.has_key('hgt')):
    valid_count = valid_count + 1

print(valid_count)