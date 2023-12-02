import re

f = open('input.txt')
lines = f.readlines()

NUM_RED = 12
NUM_GREEN = 13
NUM_BLUE = 14

def parseRound(round: str):
  for handful in round:
    numCubes = int(re.sub(r'[^\d]', "", handful))

    if 'red' in handful and numCubes > NUM_RED:
      return False
    if 'green' in handful and numCubes > NUM_GREEN:
      return False
    if 'blue' in handful and numCubes > NUM_BLUE:
      return False
  return True

def parseGame(game: str):
  game = game.strip('\n')
  rounds = re.split(': |;', game)
  if '' in rounds:
    rounds.remove('')
  
  for round in rounds:
    if not parseRound(re.split(',', round)):
      return False
  return True
    
res = 0
for i, line in enumerate(lines): 
  if parseGame(line):
    res += i + 1

print(res)
  
  