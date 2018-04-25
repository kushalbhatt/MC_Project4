#/usr/bin/python
#!/usr/bin/python

import sys
import csv
import numpy as np
import math
from scipy.spatial.distance import euclidean
from fastdtw import fastdtw

#global variables
datasubject=[]
datareference=[]
DTW_feature=[]

def main():
	dataPath = "D:/ASL/feature/ScaleSpace_CSV/";
	savePath = "D:/ASL/feature/DTW/";
	Subject = "CSE572_G02";
	Reference = "CSE572_G04";

def run_DTW_Generation(subjectinputfile, referenceinputfile):
	numSensors=1
	global datasubject
	global datareference
	global DTW_feature
	
	datasubject = CSV2Memory(subjectinputfile)
	datareference = CSV2Memory(referenceinputfile)
	DTW_feature = [[None]*numSensors*27]*len(datareference)*len(datasubject)
	#what I want to do: there are 486 columns, where it is 27*18, where each 27 from subject and reference are compared
	col=0
	for iSensor in range(0,((len(datasubject)*(len(datareference)%numSensors+1)))):#iterate through all subjects and references for compare
			for iOctave in range(0,3):#3 octaves per sensor
				for iScale in range(0,9):#9 values=4Dogs+5scale-space for each octave
					#produce float array from each string SS or DoG saved in 3D data array
					#subject SS/DoG
					num=0
					x=0
					subject_one=[]
					item=datasubject[iSensor%(len(datasubject))][iOctave][iScale]
					if ',' in item:
						x = np.fromstring(item, dtype=int, sep=',')
						subject_one = x.astype(np.float)
					else:
						x = np.array(item)
						x = np.reshape(x, (1,))
						subject_one = x.astype(np.float)
					#reference SS/DoG
					num=0
					x=0
					reference_one=[]
					item=datasubject[(iSensor%numSensors)+(int(iSensor/len(datasubject))*numSensors)][iOctave][iScale]
					if ',' in item:
						x = np.fromstring(item, dtype=int, sep=',')
						reference_one = x.astype(np.float)
					else:
						x = np.array(item)
						x = np.reshape(x, (1,))
						reference_one = x.astype(np.float)
					
					norm_subject_one = MinAndMaxNorm(subject_one)
					norm_reference_one = MinAndMaxNorm(reference_one)
						#one segment to another segment is one row
						#row is segments
						#column is SS or DoG
					#print("row:"+str(int(iSensor/numSensors))+" col:"+str(col))
					distance, path = fastdtw(norm_subject_one, norm_reference_one, dist=euclidean)
					DTW_feature[int(iSensor/numSensors)][col]=distance
					if(col==(numSensors*27-1)):
						col=0
					else:
						col=col+1

	with open("new_file.csv","w+") as my_csv:
		csvWriter = csv.writer(my_csv,delimiter=',')
		csvWriter.writerows(DTW_feature)

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

def MinAndMaxNorm(input):
	output=[]
	del output[:]
	max_value = np.amax(input)
	min_value = np.amin(input)
	for i in range(0,input.size):
		if(max_value==min_value):
			output.append(0)
		elif(math.isnan((input[i] - min_value) / (max_value - min_value))):
			output.append(0)
		else:
			output.append((input[i] - min_value) / (max_value - min_value))
	return output

def dtw_c(s, t):
	d = 0
	D = []
	i=0
	j=0
	j1=0
	j2=0
	cost=0.0
	temp=0.0
	ns=len(s)
	nt=len(t)

	# initialization
	D = [[-1 for x in range(nt+1)] for y in range(ns+1)]
	
	D[0][0] = 0;
	
	# dynamic programming
	for i in range(1,ns+1):
		j1 = 1
		j2 = nt
		for j in range(j1,j2+1):
			cost = math.sqrt((s[i - 1] - t[j - 1])*(s[i - 1] - t[j - 1]))
			print(cost)
			temp = D[i - 1][j]
			if (D[i][j - 1] != -1):
				if (temp == -1 or D[i][j - 1]<temp):
					temp = D[i][j - 1]
			if (D[i - 1][j - 1] != -1):
				if (temp == -1 or D[i - 1][j - 1]<temp):
					temp = D[i - 1][j - 1]
			
			D[i][j] = cost + temp

	d = D
	return d;
	'''
	d = []
	D=[]
	i=0
	j=0
	j1=0
	j2=0
	cost=0.0
	temp=0.0
	
	#initialization
	D = [[0 for x in range(len(t)+1)] for y in range(len(s)+1)]
	D[0][0] = 0;
	
	# dynamic programming
	for i in range(1,(len(s)+1)):#<=
		j1 = 1
		j2 = (len(t))
		
		for j in range (j1,j2+1):#<=
			cost = math.sqrt((s[i - 1] - t[j - 1])*(s[i - 1] - t[j - 1]))
			temp = D[i - 1][j]
			if (D[i][j - 1] != -1):
				if (temp == -1 or D[i][j - 1]<temp):
					temp = D[i][j - 1]
			if (D[i - 1][j - 1] != -1):
				if (temp == -1 or D[i - 1][j - 1]<temp):
					temp = D[i - 1][j - 1]
			D[i][j] = cost + temp
			print(D[i][j])

	d = D
	return d
	'''
run_DTW_Generation("test.csv","text1.csv")
#run_DTW_Generation("1491432155750.csv","1491433099844.csv")
print (len(DTW_feature))
'''
if __name__ == "__main__":
	main()'''
