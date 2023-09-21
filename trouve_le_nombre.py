import random

print("🔮 Dans ce jeu, tu dois deviner à quel chiffre ou nombre je pense.🔮"+"\n"+"Tu peux choisir ta difficulté en choisisant toi-même le nombre maximal. Par exemple, si tu choisi 25, tu devras trouver le chiffre ou le nombre compris entre 0 et 25.")
nombre = input("Que le jeu commence ! 🥳 Choisi un nombre (ou un chiffre) : ")

if nombre.isdigit():
  nombre = int(nombre)

  if nombre <= 0:
    print("Tu n'aimes pas le challenge 😂 ! Il faut que ton chiffre ou ton nombre soit plus grand que 0 sinon c'est trop simple.")
    quit()
else:
  print("Soit tu as tenté de mettre une valeur négative, soit ce n'est ni un chiffre, ni un nombre. Essaye de suivre la consigne la prochaine fois 😂")
  quit()

if nombre <= 10:
  print("Ah oui, tu as choisi le mode bébé ! 😅")
elif nombre > 10 and nombre <= 25:
  print("Ok, tu as choisi la difficulté : facile")
elif nombre > 25 and nombre <= 50:
  print("Ok, tu as choisi la difficulté : moyen")
elif nombre > 50 and nombre <= 75:
  print("Ok, tu as choisi la difficulté : difficile")
elif nombre > 75 and nombre <= 100:
  print("Ok, tu as choisi la difficulté : très difficile")
elif nombre > 100:
  print("OULA ! Toi tu veux jouer en mode hardcore ! Bon courage, prend ce trèfle pour te porter chance : ☘")

print(f"Le chiffre ou le nombre que tu dois deviner est compris entre 0 et {nombre}")

nombre_aleatoire = random.randint(0, nombre)
essai = 0

while True:
  essai += 1
  essai_joueur = input("Propose un chiffre ou un nombre : ")
  if essai_joueur.isdigit():
    essai_joueur = int(essai_joueur)

  else:
    print("Roh, tu n'a toujours pas compris la consigne ? 😩 Tu dois écrire un chiffre ou un nombre.")
    continue

  if essai_joueur == nombre_aleatoire:
    print("Oui, c'est ça ! ")
    break
  elif essai_joueur > nombre_aleatoire:
    print("Et non, c'est plus petit !")
  else:
    print("Mince, c'est plus grand !")

print(f"Félicitations, tu as trouvé en {essai} coups ! 🎉")