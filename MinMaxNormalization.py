'''
 Performs min-max normalization on data
 Input: list of values
 Output: Normalized output list
'''
import numpy as np
def MinAndMaxNorm(data):
    data = np.array(data)
    minVal = min(data)
    maxVal = max(data)
    print "min = ",minVal,"      max = ",maxVal
    normData = (data - minVal) / (maxVal - minVal)
    return normData.tolist()

#print MinAndMaxNorm(np.array([10,20,30,40]))