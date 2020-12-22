import random

def pickWord(words, longueurMot):
  word = str()
  while len(word) >= longueurMot or len(word) == 0:
    i = random.randint(0,len(words)-1) # inclu
    word = words[i]
  try:
    assert(len(word) > 0)
  except AssertionError:
    print("Erreur dans la détermination du mot...")
    exit()
  return word

def rightLetter(word, letter):
  letters = [char.upper() for char in word]
  if letter.upper() in letters:
    return True
  return False

def getDisplayedWord(word,foundLetters):
  letters = [char.upper() for char in word]
  for i,letter in enumerate(letters):
    if not letter in foundLetters:
      letters[i] = "*"
  return " ".join(letters)

def isFound(word, foundLetters):
  for char in word:
    if not char.upper() in foundLetters:
      return False
  return True

def getUpdateScoresHash(name,scores,nombreErreurs,nombreChance):
  score = nombreChance-nombreErreurs
  if name in scores.keys():
    scores[name] += score
  else:
    scores[name] = score
  return scores

def getScoreIfExists(name,scores):
  if name in scores.keys():
    return scores[name]
  else:
    return 0
