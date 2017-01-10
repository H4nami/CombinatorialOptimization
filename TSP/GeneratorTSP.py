from sys import argv
import random
from math import ceil


def generator(x,i,wmin,wmax,vmin,vmax):
	for num in xrange(1,x+1):
		nombre="instancia"+str(num)+'_'+str(i)+".txt"
		file=open(nombre,'w')
		w=0
		for item in xrange(1,i+1):
			peso=random.randint(wmin,wmax+1)
			w+=peso
			file.write(str(item)+" "+str(peso)+" "+str(random.randint(vmin,vmax+1))+"\n")
		wtotal=int(ceil(((w*2)/i)*.99))
		file.write(str(wtotal))
		file.close()

generator(int(argv[1]), int(argv[2]), int(argv[3]), int(argv[4]), int(argv[5]), int(argv[6]))


