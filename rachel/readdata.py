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
data = [[[0 for k in range(0,9)] for j in range(0,3)] for i in range(0,row_count)]
#print (row_count)
f.close()
f = open("test.csv", 'r+')
reader = csv.reader(f,delimiter=',')
row=0
for octave in reader:
	octave = str(octave).replace('[','')
	octave = str(octave).replace(']','')
	#print (octave)
	print ("done")
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
	for d in range(0,len(octave2list)):
		[float(i) for i in octave2list[d].split(',')]
	for d in range(0,len(octave3list)):
		[float(i) for i in octave3list[d].split(',')]
	#print octave values
	'''
	for d in range(0,len(octave1list)):
		print (octave1list[d])
	for d in range(0,len(octave2list)):
		print (octave2list[d])
	for d in range(0,len(octave3list)):
		print (octave3list[d])
		'''
	for y in range(0,3):
		for z in range(0,9):
			if(y==0):
				data[row][y][z]=octave1list[z]#parser[x*26+y*8+z]
			elif(y==1):
				data[row][y][z]=octave2list[z]#parser[]
			else:
				data[row][y][z]=octave3list[z]#parser[x*26+y*8+z]
	row=row+1
	del octave1list[:]
	del octave2list[:]
	del octave3list[:]
	del list[:]
#print (data[x][y][z])
#TODO: test for multiple rows in csv, create 3D matrix below, where outtermost dimension is column
f.close()

