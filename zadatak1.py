#angus hehehehehehhehehahahahh
import sys
from math import ceil, floor


def pogreska( poruka ):
    print(poruka)
    sys.exit(0)
#never will recover
def ucitati( data ):
    matrica = {}
    for redak in data:
        s = redak.split();
        matrica[' '.join([s[0] ,s[1]])] = float(s[2]);
    return matrica

def fillMatrix(rows):
    dictionary = {}
    for row in rows:
        elementiRetka = row.split()
        try:
            float(elementiRetka[2])
        except ValueError:
            print("kriva vrijednost u matrici")
            return -1
        dictionary[int(elementiRetka[0]) ,int(elementiRetka[1])] = float(elementiRetka[2])
    return dictionary

def getDimensionsRedak(dimenz):
    dimenz = dimenz.split()
    brojRedaka = int(dimenz[0])
    return brojRedaka

def getDimensionStupac(dimenz):
    dimenz = dimenz.split()
    brojStupac = int(dimenz[1])
    return brojStupac

def ucitaj( info ):
    matrix = {}
    for redak in info:
        pom = redak.split();
        matrix[' '.join([pom[0],pom[1]])] = float(pom[2]);
    return matrix




cijelaMatrica1 = {}
cijelaMatrica2 = {}
datoteka = open("matrice.txt", "r")
sadrzajDatoteke = datoteka.read()
matrice = sadrzajDatoteke.split("\n\n")

retciMatrice1 = matrice[0].split("\n")
retciMatrice2 = matrice[1].split("\n")

matrix1 = ucitaj(retciMatrice1[1:])
matrix2 = ucitaj(retciMatrice2[1:])

infoORetcimaIStupcima1 = retciMatrice1[0].split()
infoORetcimaIStupcima2 = retciMatrice2[0].split()
brojRedaka1 = infoORetcimaIStupcima1[0]
brojStupaca1 = infoORetcimaIStupcima1[1]
brojRedaka2 = infoORetcimaIStupcima2[0]
brojStupaca2 = infoORetcimaIStupcima2[1]

if brojStupaca1 != brojRedaka2:
    pogreska("nekonzistentno stanje matrica")



cijelaMatrica1 = fillMatrix(retciMatrice1[1:])
cijelaMatrica2 = fillMatrix(retciMatrice2[1:])

if cijelaMatrica1 == -1:
    pogreska("nekonzistentno stanje matrica")

#timedMatrix = pomnozi(cijelaMatrica1, cijelaMatrica2, retciMatrice1[0], retciMatrice2[0])
rez = {}


for i in range(int(brojRedaka1)):
    for j in range(int(brojStupaca2)):
        ez = '%d' % (i + 1)
        jz = '%d' % (j + 1)
        rez[' '.join([ez, jz])] = 0.0
for el in matrix1:
    z = el.split()
    rowP = z[0]
    colum = z[1]
    num1 = matrix1[el]
    for i in range(int(brojStupaca2)):
        ind = '%d' % (i+1)
        kljuc = ' '.join([colum,ind])
        if kljuc in matrix2:
            num2 = matrix2[kljuc]
            rez[ ' '.join([rowP,ind]) ] += num1*num2
        else:
            pogreska("krive matrice")


rezDatoteka = open("times.txt", "w")
rezDatoteka.write(str(brojRedaka1 ) + " " +str(brojStupaca2 )+ "\n")

for redakMatrice in rez:
    redak = str(redakMatrice)+" "+str(float(rez[redakMatrice]))
    rezDatoteka.write(redak+"\n")

rezDatoteka.close()