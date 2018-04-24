#/usr/bin/python
#!/usr/bin/python

import sys
import csv
import numpy as np

#global variables
datasubject=[]
datareference=[]

def main():
	dataPath = "D:/ASL/feature/ScaleSpace_CSV/";
	savePath = "D:/ASL/feature/DTW/";
	Subject = "CSE572_G02";
	Reference = "CSE572_G04";

def run_DTW_Generation(dataPath, savePath, subjectinputfile, referenceinputfile):
	
	global datasubject
	global datareference
	datasubject = CSV2Memory(subjectinputfile)
	datareference = CSV2Memory(referenceinputfile)
	
	for iCompare in range(0,(len(datareference))*(len(datasubject))):#iterate through all subjects and references for compare
		i = iCompare / Reference_N_Label
			j = iCompare % Reference_N_Label
			for iSensor in prange(0,18):#18 sensors
				for iOctave in prange(0,3):#3 octaves per sensor
					for iScale in prange(0,9):#9 values=4Dogs+5scale-space for each octave
						#720*34=24480; this iterates through subjects and references
						subject_idx = i * 12960 + iSensor * 720 + DataSizeSet[iOctave] + SizeSet[iOctave] * iScale #9DoG and SS*80=45+23+12 = 720
						reference_idx = j * 12960 + iSensor * 720 + DataSizeSet[iOctave] + SizeSet[iOctave] * iScale
						
						subject_one=[45]
						reference_one=[45]
						
						norm_subject_one=[45]
						norm_reference_one=[45]
						
						for m in range(0,SizeSet[iOctave]):
							subject_one[m] = Subject_Data[subject_idx + m]
							reference_one[m] = Reference_Data[reference_idx + m]
						
						
						MinAndMaxNorm(subject_one, SizeSet[iOctave], norm_subject_one)
						MinAndMaxNorm(reference_one, SizeSet[iOctave], norm_reference_one)
						DTW_feature[i*Reference_N_Label + j][iSensor * 27 + iOctave * 9 + iScale] = dtw_c(norm_subject_one, norm_reference_one, SizeSet[iOctave], SizeSet[iOctave])

save_filename = savePath + Subject+ "_" + Reference + ".csv"
	DTW_filename = save_filename
	Out_File = open(DTW_filename)
	for m in range(0,Subject_N_Label*Reference_N_Label):
		for n in range(0,18 * 3 * 9):
			#newer_method_string = "{:.9f}".format(numvar)
			Out_File.write("{:.9f}".format(DTW_feature[m][n]))
			#Out_File << fixed << setprecision(5) << DTW_feature[m][n];
			if (n != 18 * 3 * 9 - 1):
				Out_File.write(",")
		#Out_File << ",";
	Out_File.write("\n")
Out_File.close()

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

def MinAndMaxNorm(input, inputSize, output):
	max_value = max(input)
	min_value = min(input)
	for i in range from (0,inputSize):
		output[i] = (input[i] - min_value) / (max_value - min_value)

def dtw_c(s, t, ns, nt):
	d = 0
	D=[][]
	i, j
	int j1, j2
	cost, temp
	
	#initialization
	for i in range(0,ns+1):
		for j in range(0,nt+1):
			D[i][j] = -1
	D[0][0] = 0;
	
	# dynamic programming
	for i in range(1,nss+1):#<=
		j1 = 1
		j2 = nt
		
		for j in range (j1,j2+1):#<=
			cost = np.sqrt((s[i - 1] - t[j - 1])*(s[i - 1] - t[j - 1]))
			temp = D[i - 1][j]
			if (D[i][j - 1] != -1):
				if (temp == -1 || D[i][j - 1]<temp):
					temp = D[i][j - 1]
			if (D[i - 1][j - 1] != -1):
				if (temp == -1 || D[i - 1][j - 1]<temp):
					temp = D[i - 1][j - 1]
			D[i][j] = cost + temp

d = D[ns][nt]
return d

if __name__ == "__main__":
	main()
