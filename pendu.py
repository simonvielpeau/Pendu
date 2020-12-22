from fonctions import *
import donnees

# get word & nombre chances -> données
word = pickWord(donnees.getWordsList(),donnees.getLongueurMot())
nombreChance = donnees.getNombreChance()
scores = donnees.getScores()


print("----------------")
print("Bienvenue dans le jeu du pendu créé par Simon")
print("Les règles sont simples :")
print("    • Un mot de {} lettres maximum est choisi ;".format(donnees.getLongueurMot()))
print("    • À chaque coup, vous tentez de trouver une lettre composant le mot.")
print("    • Si la lettre figure dans le mot, vous ne perdez pas de chance. Par contre, si elle ne l'est pas, vous en perdez une.")
print("    • Vous avez {} chances pour déterminer le mot ;".format(nombreChance))
print("----------------")


name = input("Tout d'abord, j'aurais besoin de votre nom pour enregistrer plus tard votre score : ").lower()
# already a score ?
eventuelScore = getScoreIfExists(name,scores)
if eventuelScore != 0:
  print("Je vois que vous êtes un habitué !")
  print("Vous reprenez bien entendu votre score de {} points.".format(eventuelScore))
else:
  print("Je vois que c'est la première fois que vous jouez.")
  print("Bonne chance !")
print("----------------")


print("C'est parti !")

# set basic vars
foundLetters = []
nombreErreurs = 0

continuerPartie = "o"

while continuerPartie == "o":
  while not isFound(word,foundLetters):

    print("\nIl vous reste {} chances(s).\n".format(nombreChance-nombreErreurs)) # j'affiche les chances

    print(getDisplayedWord(word,foundLetters))  # j'affiche le mot avec les * (ou non s'il a trouvé)

    # demande lettre
    letter = input("Rentrez une lettre : ")
    if(len(letter) != 1):
      print("Vous n'avez le droit qu'à une lettre !")
      continue

    # check if it's right
    if(rightLetter(word,letter)):
      foundLetters.append(letter.upper())
    else:
      nombreErreurs+=1

    # enough chances ?
    if nombreErreurs >= nombreChance:
      break

  # pourquoi a-t-on quitté la boucle ?
  if isFound(word,foundLetters): # parce qu'il a trouvé
    print(getDisplayedWord(word,foundLetters))
    print("\nFélicitations ! Vous gagnez {} point(s).".format(nombreChance-nombreErreurs))

    donnees.setScores(getUpdateScoresHash(name,scores,nombreErreurs,nombreChance))
    score = donnees.getScores()[name]
    print("Cela vous fait donc {} point(s) au compteur !".format(score))
  else:                          # parce qu'il avait plus de chance
    print("PENDU !")
    print("Le mot était {}. Retentez votre chance !".format(word))

  continuerPartie = input("\nOn continue ? O = oui / N = non : ").lower()
  if continuerPartie == "o":
    print("C'est reparti !")
    print("----------------")
    word = pickWord(donnees.getWordsList(),donnees.getLongueurMot())
    foundLetters = []
    nombreErreurs = 0





