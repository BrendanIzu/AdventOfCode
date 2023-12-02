import re

f = open('input.txt')
lines = f.readlines()
res = 0


# clean must account for these scenarios:
# oneight -> 18 ('one' will be replaced first)
# twone -> 21 ('one' will be replaced first)
# eightwo -> 82 ('two' will be replaced first)
# eighthree -> 83 ('three' will be replaced first)
# threeeight -> 38 ('three' will be replaced first)
# fiveight -> 58 ('five' will be replaced first)
# sevenine -> 79 ('seven' will be replaced first)
#
# in each case, the string replaced first must 
# included an extra character in case something
# follows.

def clean(s: str):
  x = s.replace('one', 'o1e')\
    .replace('two', 't2')\
    .replace('three', 't3e')\
    .replace('four', '4')\
    .replace('five', '5e')\
    .replace('six', '6')\
    .replace('seven', '7n')\
    .replace('eight', '8')\
    .replace('nine', '9')
  
  x = nums = re.sub(r'[^\d]', "", x)
  
  return x

for line in lines:
  cleanLine = clean(line)
  res += int(cleanLine[0] + cleanLine[-1])
  
print(res)