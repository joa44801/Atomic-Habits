import datetime
import math
import os.path, time

def mot_passe():
    date = str(datetime.date.today())
    mot = round(math.sqrt(int(date[0:4]) / int(date[5:7]) * int(date[8:10])))
    return mot


def date_modif():
    derniere = time.ctime(os.path.getmtime("carnet.txt"))
    mois = 0
    if derniere[4:7] == "Jan":
        mois =+ 1
    if derniere[4:7] == "Feb":
        mois =+ 2
    if derniere[4:7] == "Mar":
        mois =+ 3
    if derniere[4:7] == "Apr":
        mois =+ 4
    if derniere[4:7] == "May":
        mois =+ 5
    if derniere[4:7] == "Jun":
        mois =+ 6
    if derniere[4:7] == "Jul":
        mois =+ 7
    if derniere[4:7] == "Aug":
        mois =+ 8
    if derniere[4:7] == "Sep":
        mois =+ 9
    if derniere[4:7] == "Oct":
        mois =+ 10
    if derniere[4:7] == "Nov":
        mois =+ 11
    if derniere[4:7] == "Dec":
        mois =+ 12
    mois = str(mois)
    if len(mois) < 2:
        mois = "0" + mois
    conversion = derniere[20:25] + "-" + str(mois) + "-" + derniere[8:10]
    return conversion


def codex():
    date = str(datetime.date.today())
    modif = date_modif()
    code = mot_passe()
    if date == modif:
        return code
    return "Hahaha! You didn't say the magic word!"


print(codex())