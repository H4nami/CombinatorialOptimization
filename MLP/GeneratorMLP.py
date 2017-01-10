from sys import argv
import random
from math import ceil


def generator(x,i,vmin,vmax):
	for num in xrange(1,x+1):
		nombre="instancia"+str(num)+'_'+str(i)+".txt"
		file=open(nombre,'w')
		for item in xrange(1,i+1):
			peso=random.randint(wmin,wmax+1)
			file.write()
		file.close()

generator(int(argv[1]), int(argv[2]), int(argv[3]), int(argv[4]))


