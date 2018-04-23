#!/usr/bin/python

import sys
import csv
import numpy as np
cimport openmp
from cython.parallel import parallel, prange
from libc.stdlib cimport abort, malloc, free

#read dog then scale space, octave by octave
def main():
    # print command line arguments
	'''
    for arg in sys.argv[1:]:
        print arg
		'''
	dataPath = "D:/ASL/feature/ScaleSpace_CSV/";
	savePath = "D:/ASL/feature/DTW/";
	Subject = "CSE572_G02";
	Reference = "CSE572_G04";

def run_DTW_Generation(dataPath, savePath, Subject, Reference):
	Subject_Data = None#how convert float pointer?
	Subject_N_Data = 0
	Subject_Label = None
	Subject_N_Label = 0
	
	CSV2Memory(dataPath + Subject + "_interpolate_norm.csv", Subject_Data, Subject_N_Data)
	CSV2Memory(dataPath + Subject + "_interpolate_norm_label.csv", Subject_Label, Subject_N_Label)
	
	Reference_Data = None
	Reference_N_Data = 0
	Reference_Label = None
	Reference_N_Label = 0
	
	CSV2Memory(dataPath + Reference + "_interpolate_norm.csv", Reference_Data, Reference_N_Data)
	CSV2Memory(dataPath + Reference + "_interpolate_norm_label.csv", Reference_Label, Reference_N_Label)
	
	SizeSet = [45, 23, 12]#each octave 1/2 each time (downscale)
	DataSizeSet = [0, 405, 612]
	DTW_feature = [][]#(float**)malloc(sizeof(float*) * Subject_N_Label*Reference_N_Label);
	for i in range(0,Subject_N_Label*Reference_N_Label)
		DTW_feature[i] = (float*)malloc(sizeof(float) * 34 * 3 * 9)
	
	iSubject = 0
	iReference = 0
	
	subject_idx, reference_idx, i, j, iCompare
	cdef int num_threads
	openmp.omp_set_dynamic(1)
	#with nogil, parallel(num_threads=8):
	#pragma omp parallel for private(subject_idx,reference_idx, iCompare)
	for iCompare in range(0,Subject_N_Label*Reference_N_Label):#iterate through all subjects and references for compare
			i = iCompare / Reference_N_Label
			j = iCompare % Reference_N_Label
			for iSensor in prange(0,34):#34 sensors
				for iOctave in prange(0,3):#3 octaves per sensor
					for iScale in prange(0,9):#9 values=4Dogs+5scale-space for each octave
						#720*34=24480; 720??? 34???; this iterates through subjects and references
						subject_idx = i * 24480 + iSensor * 720 + DataSizeSet[iOctave] + SizeSet[iOctave] * iScale
						reference_idx = j * 24480 + iSensor * 720 + DataSizeSet[iOctave] + SizeSet[iOctave] * iScale

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
		for n in range(0,34 * 3 * 9):
			#newer_method_string = "{:.9f}".format(numvar)
			Out_File.write("{:.9f}".format(DTW_feature[m][n]))
			#Out_File << fixed << setprecision(5) << DTW_feature[m][n];
			if (n != 34 * 3 * 9 - 1):
				Out_File.write(",")
				#Out_File << ",";
		Out_File.write("\n")
	Out_File.close()

def CSV2Memory(filename, output_data, TotalSize):#this changes for us
	with open(filename, 'r+') as f:
		reader = csv.reader(f)
		vector_Data = list(reader)
	f.close()
	#print (your_list)
	while True:
		if (length(vector_Data.size()) == 0):
			break
		for i in range(0,length(vector_Data)):
			output_data[TotalSize + i] = str(vector_Data[i])
		TotalSize += length(vector_Data)

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
