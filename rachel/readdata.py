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
item="0.6378908409044253,0.37455910133030135,-0.4873087374045415,-1.4231004682629815,-2.0970507742699023,-2.033841235459955,-0.9399202127320145,0.4471532111221097,1.179009282488599,1.0273711537224035,-0.19250074722458896,-2.1002985954816893,-3.3421415417449363,-3.1425112940107107,-2.2023349679167366,-1.3092406198340318,-0.710478036511754,-0.5431840815153104,-0.8533309461353675,-1.2468049957186516,-1.6575428071518568,-2.5665146310507003,-4.279623913524215,-6.710292017459322,-8.65991143898319,-6.512843292248712,1.742201711138001,12.113057805770216,16.53727367427968,10.904161175943024,2.209925282915128,0.004851607602709418,3.147326578239381,5.888643445467257,6.11888983635042,5.919209332753674,6.506399385360474,5.834026653638929,4.021907101262892,3.224029553941062,3.205391350485148,2.997645111530962,2.4243861058859495,1.3942138086338733,-0.6902909099737325,-2.6178473510414166,-1.7173901553582658,1.5601568845008416,4.3369163173847065,4.694605668194241,3.0905474006413245,1.5627697701045564,0.9702636173757826,0.7986464168362557,-0.22275046515730845,-1.916153067632957,-1.845183015521886,0.3461095177799568,1.491031220831298,0.30105915274998746,-0.34835447582489976,1.2711748738998978,4.214402923784807,6.592258859194857,7.287149249234482,5.186644523385308,-0.47263189788966686,-7.760300633529653,-13.0314830046016,-15.226252143450703,-14.252627223148563,-10.064381165212092,-3.7880712770132057,2.4856597496261243,6.0630635204017596,7.103760996337803,7.481764311435686,8.057802414405273,9.319526658717487,9.070071229209926,6.010000189832639,2.591838723161652"
if ',' in item:
	x = np.fromstring(item, dtype=float, sep=',')
	subject_one = x.astype(np.float)
else:
	x = np.array(item)
	x = np.reshape(x, (1,))
	subject_one = x.astype(np.float)
print (subject_one)
print (len(data1))
print (data2[0][0][0])
