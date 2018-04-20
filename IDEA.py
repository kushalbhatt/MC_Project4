from run_scale_space_dataV3 import *
import os
import csv

def main():
    # open all user sensor data files
    EMG_Files = []
    IMU_files = []
    for file in os.listdir("K:/ASU/MC/project_data/"):
        if file.endswith("EMG.txt"):
            #print(file)
            EMG_Files.append(file)
        if file.endswith("IMU.txt"):
            #print(file)
            IMU_files.append(file)

    """
        read all the files one by one
        For every file.... extract the sensor values and store it in a separate array (each sensor value wise)
        
        IMU file has time stamp and 10 sensor values (Orientation W,X,Y,Z, Accelerometer X,Y,Z, and Gyroscope X,Y,Z). 
	    
	    EMG sensor has time stamp and 8 EMG pods value.
    """
    #for i in range(len(EMG_Files)):
    sensor1=[]
    sensor2 = []
    sensor3 = []
    sensor4 = []
    sensor5 = []
    sensor6 = []
    sensor7= []
    sensor8 = []
    sensor9 = []
    sensor10 = []
    sensor11 = []
    sensor12 = []
    sensor13 = []
    sensor14 = []
    sensor15 = []
    sensor16 = []
    sensor17 = []
    sensor18 = []



    f = open("K:/ASU/MC/project_data/"+EMG_Files[0], 'r')
    s = f.readline()
    while(s):
        s = s.strip('\n')
        s = s.replace(" ", "")

        values = s.split(",")
        values = [float(v) for v in values]

        sensor1.append(values[1])
        sensor2.append(values[2])
        sensor3.append(values[3])
        sensor4.append(values[4])
        sensor5.append(values[5])
        sensor6.append(values[6])
        sensor7.append(values[7])
        sensor8.append(values[8])

        s = f.readline()

    f = open("K:/ASU/MC/project_data/" + IMU_files[0], 'r')
    s = f.readline()
    while (s):
        s = s.strip('\n')
        s = s.replace(" ", "")

        values = s.split(",")
        values = [float(v) for v in values]

        sensor9.append(values[1])
        sensor10.append(values[2])
        sensor11.append(values[3])
        sensor12.append(values[4])
        sensor13.append(values[5])
        sensor14.append(values[6])
        sensor15.append(values[7])
        sensor16.append(values[8])
        sensor17.append(values[9])
        sensor18.append(values[10])

        s = f.readline()

    '''Run scale-space data on this sensor values...'''



    print "Calculating scale space"
    #x = [-5]
    scale_space = run_scale_space_dataV3(sensor1)
    print "DoG Data = ",scale_space[0]
    print "Scale Space = ", scale_space[1]
    print "Total values=",(np.shape(scale_space[0])),np.shape(scale_space[1])

    '''Write the scale_space data to a csv file  
       Keep Name of the file same as input file name excluding EMG IMU
       But I still I cna't understand the output of scale-space computation
       It's not              27 values--  3 octave: each octave 5 scale, 4 DoG
       It is super weird.'''

    #Code for writing data to a csv file
    #in our case write octave wise  (But then it is not even 27 values)
    testData = [["first_name", "second_name", "Grade"],
              ['Alex', 'Brian', 'A'],
              ['Tom', 'Smith', 'B']]

    myFile = open('test.csv', 'w')
    with myFile:
        writer = csv.writer(myFile)
        writer.writerows(testData)

    print("Writing complete")
if __name__ == "__main__":
    main()