# << Programme qui filtre une chaîne de caractere. >>
# Importation du module "re" pour utiliser les expressions régulière.
import re
# Definition d'une fonction pour nettoyer une chaîne de caractères.
def nettoyer_chaine(chaine):
    # Utilisation de la fonction "re.sub" pour remplacer les caractères non alphabétiques, non numériquess et en conservant les espaces.
    # r'[^a-zA-Z0-9\s] est la motif à remplacer.
    # '' est la chîne qui remplace les occurences du motif(chaîne vide).
    return re.sub(r"[^a-zA-Z0-9\s]",' ', chaine)
# Demande à l'utilisateur d'entrer une chaîne de caractères.
chaine = input("Entrez une chaine de caracteres :")
# Appel de la foction pour nettoyer la chaîne entrée par l'utilisateur. 
chaine_nettoyee = nettoyer_chaine(chaine)
# Affichage de la chaîne nettoyée.
print("chaine nettoyee :", chaine_nettoyee)