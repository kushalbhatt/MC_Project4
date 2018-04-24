# %EXTREMA   Gets the global extrema points from a time series.
# %   [XMAX,IMAX,XMIN,IMIN] = EXTREMA(X) returns the global minima and maxima
# %   points of the vector X ignoring NaN's, where
# %    XMAX - maxima points in descending order
# %    IMAX - indexes of the XMAX
# %    XMIN - minima points in descending order
# %    IMIN - indexes of the XMIN
# %
# %   DEFINITION (from http://en.wikipedia.org/wiki/Maxima_and_minima):
# %   In mathematics, maxima and minima, also known as extrema, are points in
# %   the domain of a function at which the function takes a largest value
# %   (maximum) or smallest value (minimum), either within a given
# %   neighbourhood (local extrema) or on the function domain in its entirety
# %   (global extrema).
# %
# %   Example:
# %      x = 2*pi*linspace(-1,1);
# %      y = cos(x) - 0.5 + 0.5*rand(size(x)); y(40:45) = 1.85; y(50:53)=NaN;
# %      [ymax,imax,ymin,imin] = extrema(y);
# %      plot(x,y,x(imax),ymax,'g.',x(imin),ymin,'r.')
# %
# %   See also EXTREMA2, MAX, MIN
#
# %   Written by
# %   Lic. on Physics Carlos Adrian Vargas Aguilera
# %   Physical Oceanography MS candidate
# %   UNIVERSIDAD DE GUADALAJARA
# %   Mexico, 2004
# %
# %   nubeobscura@hotmail.com
#
# % From       : http://www.mathworks.com/matlabcentral/fileexchange
# % File ID    : 12275
# % Submited at: 2006-09-14
# % 2006-11-11 : English translation from spanish.
# % 2006-11-17 : Accept NaN's.
# % 2007-04-09 : Change name to MAXIMA, and definition added.

'''NOTE: THis code might have off by one errors needs to be checked! '''
import numpy as np
import math
def extrema(x):
    xmax = [];
    imax = [];
    xmin = [];
    imin = [];
    Nt = np.size(x)
    '''Check if 2-D array is passed
        Only vector is expected'''
    if Nt != len(x):
        print("Entry Must be a VECTOR!")
        return

    #find indices of NaN in vector
    inan = np.where(np.isnan(x))
    indx = range(Nt)
    x_without_nan = []
    #remove nan indices from indx
    if len(inan[0])!=0:
        for i in range(len(x)):
            if np.isin(i,inan,invert=True):
                x_without_nan.append(x[i])

        #NaNs removed
        x = x_without_nan

    # Difference between subsequent elements:
    dx = np.diff(x)

    #if any horizontal line?
    if not np.any(dx):
        return (xmax,imax,xmin,imin)

    #% Flat peaks? Put the middle element:

    #indexes where diff is non zero
    a = []
    for i in range(len(dx)):
        if dx[i]!=0:
          a.append(i)

    #index where a do not change
    a_diff = np.diff(a)
    lm=[]
    for i in range(len(a_diff)):
        if a_diff[i]!=1:
            lm.append(i+1) #not sure why +1

    #no of elements in the flat peak - d

    for l in lm:
        d = a[l] - a[l-1]
        #save middle elements
        a[l] = int(a[l] - math.floor(d/2))
    #because indexing starts at 0... in matlab code it is 1
    a.append(Nt-1)


    # PEAKS??
    #series without flat peaks
    xa = []
    for i in a:
        xa.append(x[i])

    b = []
    for i in np.diff(xa):
        '''  1 = positive slopes (minima begin)
             0 = negative slopes (maxima begin)'''
        if i > 0:
          b.append(1)
        else:
          b.append(0)

    # % -1 = > maxima indexes(but one)
    # % +1 = > minima indexes(but one)

    xb = np.diff(b)
    for i in range(len(xb)):
        if xb[i] == -1:
            #maxima index

            imax.append(a[i+1]) #not sure why +1

        if xb[i] == 1:
            #minima index
            imin.append(a[i + 1])  # not sure why +1

    nmaxi = len(imax)
    nmini = len(imin)


    """
    NOTE:: Below code could be having "off by 1 errors'  as matlab indexing starts at 1 but python is at 0
    Maximum or minimum on a flat peak at the ends?"""
    if nmaxi==0 and nmini==0:
        if(x[0] > x[Nt-1]):
            xmax = x[0]
            imax = indx[0]
            xmin = x[Nt-1]
            imin = indx[Nt-1]
        elif x[0]<x[Nt-1]:
            xmax = x[Nt-1]
            imax = indx[Nt-1]
            xmin = x[0]
            imin = indx[0]
        return (xmax,imax,xmin,imin)

    """Maximum or minimum at the ends?"""
    if(nmaxi==0):
        imax.insert(0, 1)
        imax.insert(1,Nt-1)
    elif nmini==0:
        imin.insert(0,1)
        imin.insert(1,Nt-1)
    else:
        if imax[0]< imin[0]:
            #insert 1 at front
            imin.insert(0,1)
        else:
            imax.insert(0,1)

        if imax[-1] > imin[-1]:
            imin.append(Nt-1)
        else:
            imax.append(Nt-1)

    for i in imax:
        xmax.append(x[i])

    for i in imin:
        xmin.append(x[i])

    # NaNs
    # imax = []
    # imin = []
    if len(inan[0]) != 0:
        for i in imax:
            imax.append(indx[i])
        for i in imin:
            imin.append(indx[i])

    ###SAME SIZE AS X
    imax = np.reshape(imax,np.shape(xmax))
    imin = np.reshape(imin, np.shape(xmin))

    ## Sort in Descending Order
    # xmax.sort()
    # xmax = np.flip(xmax,axis=1)

    '''But why??????? What's the point'''
    # #return indices of descending order sorting
    # inmax = np.argsort(-np.asarray(xmax))
    # temp_sort = []
    # temp_imax = []
    # for i in inmax:
    #     temp_sort.append(xmax[i])
    #     temp_imax.append(imax[i])
    # xmax = temp_sort
    # imax = temp_imax
    #
    # inmin = np.argsort(np.asarray(xmin))
    # temp_sort = []
    # temp_imin = []
    # for i in inmin:
    #     temp_sort.append(xmin[i])
    #     temp_imin.append(imin[i])
    # xmin = temp_sort
    # imin = temp_imin


    return (xmax,imax,xmin,imin)


#print extrema([10,10,10,20,10,10,20])