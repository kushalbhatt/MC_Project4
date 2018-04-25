#!/usr/bin/python
import csv
import numpy as np
import math
data1=[]
data2=[]

def CSV2Memory(filename):
	
	string=""
	list=[]
	
	#open the file and determine the number of rows in the csv
	sum=0
	f = open(filename, 'r+')
	for line in f:
		cleanedLine = line.strip()
		cleanedLine = str(cleanedLine).replace(',','')
		cleanedLine = str(cleanedLine).replace(' ','')
		if cleanedLine: # is not empty
			sum=sum+1
	row_count = sum
	f.close()


	#create a 3D list named data[x][y][z] where x is the row (which represents the sensor),
	#y is the octave, and z is either a DoG or SS
	data = [[[0 for k in range(0,9)] for j in range(0,3)] for i in range(0,row_count)]
	
	#open the same file in order to do computation
	f = open(filename, 'r+')
	reader = csv.reader(f,delimiter=',')
	row=0
	for octave in reader:
		#format data
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
		if(len(list)>0):
			#append list of strings to octave list
			for x in range(len(list)):
				if(x<9):
					octave1list.append(list[x])
				elif(x>=9 and x<18):
					octave2list.append(list[x])
				else:
					octave3list.append(list[x])
			#convert octave lists into float lists
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
			#store the octave list values into the corresponding 3D array space
			for y in range(0,3):
				for z in range(0,9):
					if(y==0):
						data[row][y][z]=octave1list[z]#parser[x*26+y*8+z]
					elif(y==1):
						data[row][y][z]=octave2list[z]#parser[]
					else:
						data[row][y][z]=octave3list[z]#parser[x*26+y*8+z]
			#get ready to do computation on the next row of the csv
			row=row+1
			#delete lists so that they can be used as temporaries in next iteration
			del octave1list[:]
			del octave2list[:]
			del octave3list[:]
			del list[:]
		else:
			break;
	f.close()
	return data

def main():
	global data1
	global data2
	data1 = CSV2Memory("test.csv")
	data2 = CSV2Memory("text1.csv")
def MinAndMaxNorm(input):
	output=[]
	del output[:]
	max_value = max(input)
	min_value = min(input)
	for i in range(0,len(input)):
		output.append((input[i] - min_value) / (max_value - min_value))
	return output

main()
num=0
x=0
a=[[1,2],[2,3]]
with open("new_file.csv","w+") as my_csv:
	csvWriter = csv.writer(my_csv,delimiter=',')
	csvWriter.writerows(a)
print (len(data1))
print (data2[0][0][0])
