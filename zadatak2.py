sveHipoteze = open('ulaz', 'r').readlines()
print('Hyp#Q10#Q20#Q30#Q40#Q50#Q60#Q70#Q80#Q90')
brojac = 1
myList=[i for i in range(10)]
kvantiliSvi = []
for j in range(10):
        kvantiliSvi.append(float(myList[j])/10.0)




brojLinije = 1
for redak in sveHipoteze:
		redak = redak.split(' ')
		redak.sort(key=float)
		if brojLinije < 10 :
			print("00" + str(brojLinije), end='')
		else:
			print("0" + str(brojLinije), end='')

		trenutniIndeksKvant=0
		for kvant in kvantiliSvi:
			indeks = int(len(redak)*kvant)
			vrijednost = redak[indeks]
			trenutniIndeksKvant = trenutniIndeksKvant +1
			if trenutniIndeksKvant == len(kvantiliSvi):
				print("#"+str(float(vrijednost)))
			else :
				print("#"+str(float(vrijednost)), end='')
		brojLinije = brojLinije+1