import datetime

def entree():
    date = str(datetime.date.today())
    nbr_mots = input("Nombre de minutes aujourd'hui ")
    infos = (" " + nbr_mots + "\n")
    fichier = open('carnet.txt', 'a')
    fichier.write(date)
    fichier.write(infos)

entree()