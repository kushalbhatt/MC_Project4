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
        Below written code is functional but not the most elegant
        Kept it seimple for easy of writing and understanding
        Can be improved and zipped to less lines of code
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

    print "Calculating scale space"

    '''Write the scale_space data to a csv file  
       Keep Name of the file same as input file name excluding EMG IMU
    
    csv file name would be same as sensor data file name.... except for EMG and IMU parts...

    '''
    output_filename = EMG_Files[0][:-8]#EMG.txt

    write_scale_space_to_file(output_filename,sensor1)
    write_scale_space_to_file(output_filename, sensor2)
    write_scale_space_to_file(output_filename, sensor3)
    write_scale_space_to_file(output_filename, sensor4)
    write_scale_space_to_file(output_filename, sensor5)
    write_scale_space_to_file(output_filename, sensor6)
    write_scale_space_to_file(output_filename, sensor7)
    write_scale_space_to_file(output_filename, sensor8)
    write_scale_space_to_file(output_filename, sensor9)
    write_scale_space_to_file(output_filename, sensor10)
    write_scale_space_to_file(output_filename, sensor11)
    write_scale_space_to_file(output_filename, sensor12)
    write_scale_space_to_file(output_filename, sensor13)
    write_scale_space_to_file(output_filename, sensor14)
    write_scale_space_to_file(output_filename, sensor15)
    write_scale_space_to_file(output_filename, sensor16)
    write_scale_space_to_file(output_filename, sensor17)
    write_scale_space_to_file(output_filename, sensor18)


def write_scale_space_to_file(filename,sensor_data):
    scale_space = run_scale_space_dataV3(sensor_data)
    myFile = open(filename + '.csv', 'ab+')  # append data for all sensors
    # print "DoG Data = ",scale_space[0]
    # print "Scale Space = ", scale_space[1]
    # print "Total values =",(np.shape(scale_space[0])),np.shape(scale_space[1])

    #Code for writing data to a csv file
    with myFile:
        writer = csv.writer(myFile)
        writer.writerows(scale_space)
    myFile.close()
    #print("Writing complete")


if __name__ == "__main__":
    main()