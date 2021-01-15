import datetime
import math
import os.path, time

def mot_passe():
    date = str(datetime.date.today())
    mot = round(math.sqrt(int(date[0:4]) / int(date[5:7]) * int(date[8:10])))
    return mot


def date_modif():
    derniere = time.ctime(os.path.getmtime("carnet.txt"))
    mois = " "
    if derniere[4:7] == "Jan":
        mois == "01"
    if derniere[4:7] == "Feb":
        mois == "02"
    conversion = derniere[20:25] + "-" + mois + "-" + derniere[8:10]
    return (derniere, conversion)

print(date_modif())

#2021-01-15
def codex():
    date = str(datetime.date.today())
    print(date_modif(), type(date_modif()))
    print(date, type(date))
    #if date_modif() == date:
        #print(date_modif(), date)

#codex()