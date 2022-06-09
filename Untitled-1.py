Individu1 ={"prénom":"John","nom":"DEUF","Age":30}
Individu2 ={"prénom":"Aline","nom":"HEA","Age":22}
Individu3 ={"prénom":"Tom","nom":"EIGERY","Age":18}
uneEntreprise = [Individu1,Individu2,Individu3]

def estPresent(uneEntreprise,unTel):
    print (unTel)
    liste_prenom,liste_nom,liste_age = extractiondesdeonnées(uneEntreprise)
    print("Veuillez Indiquer le prénom ou nom de la personne")
    for b in range (len(uneEntreprise)):
        print(liste_prenom[b],liste_nom[b],liste_age[b])

    if (unTel in liste_prenom):
        result = True
        a = liste_prenom.index(unTel)
    elif(unTel in liste_nom):
        result = True
        a = liste_nom.index(unTel)
    else:
        result= False
    return result,a

def ajouterUnePersonne(uneEntreprise):
    print("Prénom de la personne à ajouter")
    prénom = input()
    valeur,valeur2 = estPresent(uneEntreprise,prénom)
    nom = input()
    valeur = estPresent(uneEntreprise,nom)
    if (valeur == None):
        print("Prénom de la personne à ajouter")
        prénom = input()
        print("Nom de la personne à ajouter")
        nom = input()
        print("Age de la personne à ajouter")
        Age = input()
        ajouterutilisateur = {"prénom":prénom, "nom":nom,"age":Age}
        liste_prenom,liste_nom,liste_age = extractiondesdeonnées(uneEntreprise)
        liste_prenom.append(ajouterutilisateur["prénom"])
        liste_nom.append(ajouterutilisateur["nom"])
        liste_age.append(ajouterutilisateur["age"])  
    else:
        print("La Valeur existe Déja")
    return extractiondesdeonnées(uneEntreprise)

def extractiondesdeonnées(uneEntreprise):
    liste_prenom = []
    liste_nom = []
    liste_age = []
    for i in range (len(uneEntreprise)):
        liste_prenom.append(uneEntreprise[i]["prénom"])
        liste_nom.append(uneEntreprise[i]["nom"])
        liste_age.append(uneEntreprise[i]["Age"])
    return(liste_prenom,liste_nom,liste_age)

menu = "**** Menu de la Gestion d’entreprise **** \n 1 : Lister les personnes \n 2 : Ajouter une personne \n 3 : Enlever une personne \n 4 : Vérifier une personne \n f : pour quitter le programme"
print (menu)
choix = int(input())
if (choix == 1):
    print(extractiondesdeonnées(uneEntreprise))
elif (choix == 2):
    ajouterUnePersonne(uneEntreprise)
elif (choix == 4):
    print(estPresent(uneEntreprise))