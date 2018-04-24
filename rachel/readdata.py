#!/usr/bin/python
import csv
import pandas as pd
import numpy as np
import sys
import re
import pprint

parser=[]#instantiate list

string=""
list=[]
f = open("test.csv", 'r+')
row_count = sum(1 for row in csv.reader(f))
#print (row_count)
f.close()
f = open("test.csv", 'r+')
reader = csv.reader(f,delimiter=',')
i=0
for octave in reader:
	octave = str(octave).replace('[','')
	octave = str(octave).replace(']','')
	#print (octave)
	for x in range(1,len(octave)):
		if(octave[x-1]=="'" and octave[x]==","):
			print
		elif(octave[x]==" "):
			print
		elif(octave[x]=="'"):
			list.append(string)
			string=""
		else:
			string+=octave[x]
octave1list = []
octave2list = []
octave3list = []
x=0
while x<len(list):
	if(list[x]==''):
		del list[x]
	else:
		x=x+1
for x in range(len(list)):
	if(x<9):
		#print(list[x])
		octave1list.append(list[x])
	elif(x>=9 and x<18):
		#print(list[x])
		octave2list.append(list[x])
	else:
		#print(list[x])
		octave3list.append(list[x])
for d in range(0,len(octave1list)):
	[float(i) for i in octave1list[d].split(',')]
for d in range(0,len(octave1list)):
	print (octave1list[d])
octave1list = octave1list.astype(np.float)
octave2list = octave2list.astype(np.float)
octave3list = octave3list.astype(np.float)
print (octave1list+ " " + octave2list + " " +octave3list)
f.close()
with open('tester.csv', 'w') as fo:
	for x in range(0,len(list)):
		fo.write(list[x])
data = [[[0 for k in range(0,9)] for j in range(0,3)] for i in range(0,row_count)]
for x in range(0,row_count):
	for y in range(0,3):
		for z in range(0,9):
			data[x][y][z]=x*27+y*9+z#parser[x*26+y*8+z]
	#print (data[x][y][z])
#parser = np.loadtxt('test.csv', delimiter=',')
#print (parser)
'''
	octave = str(octave).replace("'","")
	with open('tester.csv', 'w') as fo:
	for line in octave:
	fo.write(line)'''
