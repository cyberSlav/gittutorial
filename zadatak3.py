import locale
locale.setlocale(locale.LC_ALL, '')
import glob
import os
from collections import defaultdict

#studentiMapa - kljuc je jmbag, a vrijednost nek bu ime i prez
studentiMapa = {}
sviStudenti = open('studenti', 'r').readlines();
for stud in sviStudenti:
    studInfo = stud.split(' ')
    var = studInfo[1] + " "+studInfo[2]
    studentiMapa[studInfo[0]] = var

currPath = str(os.path.dirname(os.path.abspath(__file__)));
redLabosIBodovi = {} # kljuc je redni broj labosa, a value je bodovi svi
for redniBrojLabosa in os.listdir('.'):
    if redniBrojLabosa != "studenti.txt" and redniBrojLabosa != "ulaz.txt" and redniBrojLabosa.endswith(".txt"):
        bodoviSaLabosa = open(redniBrojLabosa, 'r').read()
        redLab = redniBrojLabosa.split('_')[1]
        redLabosIBodovi[redLab] = bodoviSaLabosa

bodovi1Mapa = {} #kljuc je jmbag a broj bodova je value
bodovi1 = redLabosIBodovi["01"]
listaBodovaIOsoba = bodovi1.split("\n")
for osobaIBodovi in listaBodovaIOsoba :
    jmbag = osobaIBodovi.split(' ')[0]
    bodici = osobaIBodovi.split(' ')[1]
    bodovi1Mapa[jmbag] = bodici

bodovi2Mapa = {} #kljuc je jmbag a broj bodova je value
bodovi2 = redLabosIBodovi["02"]
listaBodovaIOsoba = bodovi2.split("\n")
for osobaIBodovi in listaBodovaIOsoba :
    jmbag = osobaIBodovi.split(' ')[0]
    bodici = osobaIBodovi.split(' ')[1]
    bodovi2Mapa[jmbag] = bodici

print ("%-10s" % 'JMBAG'),
print ("%-10s" % 'Prezime,'),
print ("%-10s" % 'ime'),
print ("%-10s" % 'L1'),
print ("%-10s" % 'L2'),
print ("%-10s" % 'L3'),
print ("%-10s" % 'L4'),
print('\n')

for JMBAG in studentiMapa.keys():

    print(JMBAG + " " + studentiMapa[JMBAG], end='')

    if JMBAG in bodovi1Mapa.keys() :
        print("%-11s" % bodovi1Mapa[JMBAG])
        #print(" "+bodovi1Mapa[JMBAG], end='')
    else :
        print(" -", end='')

    if JMBAG in bodovi2Mapa.keys():
        print("%-11s" % bodovi2Mapa[JMBAG])
        #print(" " + bodovi2Mapa[JMBAG], end='')
    else:
        print(" -", end='')

    print()

        # if JMBAG in redLabosIBodovi[kojiLabos]:

