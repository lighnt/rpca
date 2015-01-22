import Image
import numpy
import os
from getdata import Getdata
from coreset import Coreset
from scipy.linalg import orth
import scipy
import math
from rpca import ORPCA
from projectsample import  ProjectSample

'''
path = 'C:/cmu/rpca/data/Campus/'

X = Getdata(path, 0, 10)
y = numpy.array(X[0,:])*255
z = y.astype(numpy.uint8)

#q = numpy.zeros(512*512, dtype=numpy.int).reshape(512, 512)
#z.reshape((128, 160))
z.resize((128, 160))

img = Image.fromarray(z, 'L')
tt = numpy.array(img)
print tt - z
img.show()

#imshow(z.resize(160, 128))

# im.show()

#mtr = numpy.array(im)



#siz = mtr.shape

#print type(siz[0])

a = float(2)
'''
'''
X = numpy.random.random((7,10))
[C,c] = Coreset(X, 3, 0.1)
D = orth(numpy.random.random((10,4)))

costA = pow(numpy.linalg.norm(numpy.dot(X,D), ord = 'fro'),2)
costC = pow(numpy.linalg.norm(numpy.dot(C,D), ord = 'fro'),2)+c

print costA/costC - 1
'''
'''
from rpca import ORPCA

pcasolver = ORPCA(10,10)


L = numpy.random.random((10,10))
X = numpy.random.random((20,10))*3

lambda1 = lambda2 = 1/math.sqrt(20)
for i in range(0,20):
    xt = numpy.array([X[i,:]])
    xt = xt.T
    L = pcasolver.optimization(xt, L, 0*lambda1, 0*lambda2)

R = pcasolver.R.reshape((20,10))
E = pcasolver.E.reshape((20,10))

print X
print X - numpy.dot(R,L.T) - E
'''

path = 'C:/cmu/rpca/data/Campus/'
filedir = os.listdir(path)
total = len(filedir)
n = 100 # the number of frames in a coreset
k = 3 # the number of coreset base
kp = 200 # the number of pca base
epsilon = 0.1
divd = k + math.ceil(k / epsilon) - 1
lambda1 = lambda2 = 1.0/(divd*total/n)
pcasolver = ORPCA()
result = []
for i in  range(1, 3):#total/n):
    X = Getdata(path, i*n, i*n+n)
    [U,C,c] = Coreset(X, k, epsilon)

    if i == 1:
        pcasolver.init(C.shape[1], kp)
        L = numpy.random.random((C.shape[1], kp))
        for t in range(0, kp):
            L[:,t] /= max(1, numpy.linalg.norm(L[:,t]))

    for j in range(0, C.shape[0]):
        xt = numpy.array([C[j,:]])
        xt = xt.T
        L = pcasolver.optimization(xt, L, 0.01, 0.1)

repath = 'C:/cmu/rpca/result/coresetCampus/'
count = 0
for i in range(1,3):
    X = Getdata(path, i*n, i*n+n)
    for j in range(0, X.shape[0]):
        xt = numpy.array([X[j, :]])
        xt = xt.T
        [rn, en] = ProjectSample(xt, L, 0.01, 0.1, 1e-6, 1000)
        xx = numpy.array(en)
        xx = xx.reshape((128, 160))
        xx = xx*255
        xx = xx.astype(numpy.uint8)
        img = Image.fromarray(xx, 'L')
        img.save(repath + str(count) +'.bmp')
        count += 1

'''
for i in range(0, C.shape[0]):
    xx = numpy.array([C[i, :]])
    xx = xx.reshape((128, 160))
    xx = xx*255
    xx = xx.astype(numpy.uint8)
    img = Image.fromarray(xx, 'L')
    img.save()
'''
