import Image
import numpy
import os

def Getdata(path, start, end):
    #this function help get data from start to end
    filedir = os.listdir(path)
    for i in range(start, end):
        try:
            img = Image.open(path + filedir[i])
            img = img.convert('L')
            gray = numpy.array(img)
            gray = gray.astype(numpy.float32)
            gray /= 255.0
            if i == start:
                ss = gray.shape
                sz = ss[0]*ss[1]
            gray.resize((1, sz))
            if i == start:
                X = gray
            else:
                X = numpy.append(X, gray)
        except IOError:
            print 'Image cannot be found..'
            return numpy.mat([0])
    X = numpy.array([X])
    X = X.reshape((end - start, sz))
    return X

