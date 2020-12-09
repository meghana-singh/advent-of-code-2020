import re
import unittest

class PassportTest(unittest.TestCase):
   def test_pid(self):
      self.assertEquals(pid_chk('000000001'), True)
      self.assertEquals(pid_chk('0123456789'), False)
      self.assertEquals(pid_chk('abcdefghi'), False)
      self.assertEquals(pid_chk(''), False)
      self.assertEquals(pid_chk(None), False)

   def test_ecl(self):
      self.assertEquals(ecl_chk('brn'), True)
      self.assertEquals(ecl_chk('brnn'), False)
      self.assertEquals(ecl_chk(''), False)
      self.assertEquals(ecl_chk(None), False)

   def test_eyr(self):
      self.assertEquals(eyr_chk('2020'), True)
      self.assertEquals(eyr_chk('2030'), True)
      self.assertEquals(eyr_chk('2018'), False)
      self.assertEquals(eyr_chk(''), False)
      self.assertEquals(eyr_chk(None), False)

   def test_hcl(self):
      self.assertEquals(hcl_chk('#123abc'), True)
      self.assertEquals(hcl_chk('#123abz'), False)
      self.assertEquals(hcl_chk('123abc'), False)
      self.assertEquals(hcl_chk(''), False)
      self.assertEquals(hcl_chk(None), False)

   def test_byr(self):
      self.assertEquals(byr_chk('2002'), True)
      self.assertEquals(byr_chk('2003'), False)
      self.assertEquals(byr_chk('abcd'), False)
      self.assertEquals(byr_chk(''), False)
      self.assertEquals(byr_chk(None), False)

   def test_iyr(self):
      self.assertEquals(iyr_chk('2010'), True)
      self.assertEquals(iyr_chk('2020'), True)
      self.assertEquals(iyr_chk('2000'), False)
      self.assertEquals(iyr_chk(''), False)
      self.assertEquals(iyr_chk(None), False)

   def test_hgt(self):
      self.assertEquals(hgt_chk('60in'), True)
      self.assertEquals(hgt_chk('190cm'), True)
      self.assertEquals(hgt_chk('190in'), False)
      self.assertEquals(hgt_chk('190'), False)
      self.assertEquals(hgt_chk(''), False)
      self.assertEquals(hgt_chk(None), False)

def pid_chk(value):
    if value and (bool(re.match('^\d{9}$', value))):
        return True
    return False

def ecl_chk(value):
    if value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return True
    return False

def eyr_chk(value):
    if value and bool(re.match('^\d{4}$', value)):
        if (int(value) >= 2020 and int(value) <= 2030):
            return True
    return False

def hcl_chk(value):
    if value and bool(re.match('^#[0-9a-f]{6}', value)):
        return True
    return False

def byr_chk(value):
    if value and bool(re.match('^\d{4}$', value)):
        if (int(value) >= 1920 and int(value) <= 2002):
            return True
    return False

def iyr_chk(value):
    if value and bool(re.match('^\d{4}$', value)):
        if (int(value) >= 2010 and int(value) <= 2020):
            return True
    return False

def hgt_chk(value):
    if value:
        match = re.findall('^(\d+)(cm|in)$', value)
        for val, key in match:
            if key == 'in' and int(val) >= 59 and int(val) <= 76:
                return True
            if key == 'cm' and int(val) >= 150 and int(val) <= 193:
                return True
    return False

if __name__ == '__main__':

    # Read the entire file and split on newline+newline
    with open('input.txt') as f:
        rows = f.read().split("\n\n")
    valid_count = 0
    for row in rows:
        passport = {}
        regex = "(hcl|cid|ecl|hgt|byr|pid|iyr|eyr):([a-z0-9#]+)"
        match = re.findall(regex, row)
        for key, val in match:
            passport[key] = val
        if (ecl_chk(passport.get('ecl')) and pid_chk(passport.get('pid')) and
            eyr_chk(passport.get('eyr')) and hcl_chk(passport.get('hcl')) and
            byr_chk(passport.get('byr')) and iyr_chk(passport.get('iyr')) and
            hgt_chk(passport.get('hgt'))):
            valid_count += 1

    print(valid_count)