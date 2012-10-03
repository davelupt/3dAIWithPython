import random
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
from matplotlib import cm
import random as rand
import sys
import math

sys.setrecursionlimit(20000)
nx, ny = 5,5

x = range(nx)
y = range(ny)

data = np.random.random_integers(1,100,(nx,ny))
datamap = []

for indexOfi, i in enumerate(data):
	for indexOfj, j in enumerate(i):
		ele = [indexOfj, indexOfi, j]
		datamap.append(ele)
		
#print(data)
#print(datamap)

maxZ = min(datamap, key = lambda x:x[2])
print('the real answers is: ' + str(maxZ))
maxY = datamap[(nx * ny - 1)][1]
maxX = datamap[(nx * ny - 1)][0]
minY = datamap[0][1]
minX = datamap[0][0]

def findLowest():
	attemptsScalar = 1.1
	def checkUp(i, turnNo, currentLowest):
		#print('Starting with: ' + str(i))
		#print('checking up')
		currY = i[1] 								#gets the y value for the random element
		currX = i[0]								#gets the x value for the random element
		newY = currY + 1
		if(newY < maxY):
			indexForY = newY * ny						#increases the y value by 1 and multiplies by the size 
			newIndex = indexForY + currX					#in order to get the right element if possible
			#print(datamap[newIndex])
			if(datamap[newIndex][2] < i[2]):
				#print('The Z value for upper was lower')
				setLowest(datamap[newIndex], turnNo, currentLowest)
			else:
				#print('The Z value for upper was higher')
				checkDown(i, turnNo, currentLowest)
				
		else:
			#print('Going up puts us out of bounds')
			checkDown(i, turnNo, currentLowest)
			
	def checkDown(i, turnNo, currentLowest):
		#print('checking down')
		currY = i[1]
		currX = i[0]
		newY = currY - 1
		if(newY >= minY):
			indexForY = newY * ny
			newIndex = indexForY + currX
			#print(datamap[newIndex])
			if(datamap[newIndex][2] < i[2]):
				#print('the Z value for down was lower')
				setLowest(datamap[newIndex], turnNo, currentLowest)
			else:
				#print('The Z value for down was higher')
				checkLeft(i, turnNo, currentLowest)
		else:
			#print('Going down puts us out of bounds')
			checkLeft(i, turnNo, currentLowest)
			
	def checkLeft(i, turnNo, currentLowest):
		print('checking left')
		currY = i[1]
		currX = i[0]
		newX = currX - 1
		if(newX >= minX):
			newIndex = (currY * ny) + newX
			#print(datamap[newIndex])
			if(datamap[newIndex][2] < i[2]):
				#print('the Z value for left was lower')
				setLowest(datamap[newIndex], turnNo, currentLowest)
			else:
				#print('The Z value for left was higher')
				checkRight(i, turnNo, currentLowest)
		else:
			#print('Going left puts us out of bounds')
			checkRight(i, turnNo, currentLowest)
			
	def checkRight(i, turnNo, currentLowest):
		#print('checking right')
		currY = i[1]
		currX = i[0]
		newX = currX + 1
		if(newX < maxX):
			newIndex = (currY * ny) + newX
			print(datamap[newIndex])
			if(datamap[newIndex][2] < i[2]):
				#print('the Z value for right was lower')
				setLowest(datamap[newIndex], turnNo, currentLowest)
			else:
				#print('The Z value for right was higher')
				generateRandom(turnNo, currentLowest)
		else:
			#print('Going right puts us out of bounds')
			generateRandom(turnNo, currentLowest)
			
	def setLowest(i, turnNo, currentLowest):
		maxTries = math.floor((nx * ny)/attemptsScalar)								
		#print('the currentLowest at the start is: ' + str(currentLowest))
		#print('the current number of tries is:->>>>>>>>>>>>>>>' + str(turnNo))
		if(currentLowest != None):
			if(currentLowest[2]>i[2]):
				currentLowest = i
		else:
			currentLowest = i	
		print('THE Current Lowest is Now:--------------------->' + str(currentLowest))
		if(turnNo <= maxTries):
			checkUp(i, turnNo + 1, currentLowest)
		
	def generateRandom(turnNo = 0, currentLowest = None):
		i = rand.choice(datamap)
		setLowest(i, turnNo, currentLowest)
		
	generateRandom()
	
findLowest()


hf = plt.figure()

ha = hf.add_subplot(111,projection='3d')

X,Y = np.meshgrid(x,y)
ax = ha.plot_surface(X,Y,data, rstride = 1, cstride = 1, cmap = cm.jet)
ha.set_zlabel('z')
ha.set_ylabel('y')
ha.set_xlabel('x')

hf.colorbar(ax, shrink= 0.5, aspect = 5)
plt.show()
