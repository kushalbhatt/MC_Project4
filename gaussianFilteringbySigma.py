import numpy as np
def gaussianFilteringbySigma(data,sigma,sz):
    x = np.linspace( -sz/2, sz/2,num=sz)
    gaussFilter = np.exp( - np.power(x,2) / (2 * sigma * sigma))
    gaussFilter = gaussFilter / sum(gaussFilter)  #normalize
    filteredData = np.convolve(data,gaussFilter,mode="same")
    return filteredData