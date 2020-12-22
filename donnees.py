import pickle

words=[]
with open("words.txt","r") as wordsFile:
  for line in wordsFile:
    for word in line.split():
      words.append(word)

nombreChance = 8

scores = {}
try:
  file = open("scores","rb")
except FileNotFoundError:
  file = open("scores","w")
  file.close()

with open("scores","rb") as scoresFile:
  scoresFileUnpickler = pickle.Unpickler(scoresFile)
  try:
    scores = scoresFileUnpickler.load()
  except EOFError: # si rien a load
    pass
def setScores(scores):
  with open("scores","wb") as scoresFile:
    scoresFilePickler = pickle.Pickler(scoresFile)
    scoresFilePickler.dump(scores)

longueurMot = 8

# get vars

def getWordsList():
  return words

def getNombreChance():
  return nombreChance

def getScores():
  return scores

def getLongueurMot():
  return longueurMot
