import numpy
import math


def Coreset(X, k, epsilon):
    #X: data, k: the dim of subspace, epsilon: the error
    m = min(k + math.ceil(k / epsilon) - 1, X.shape[0])
    [U, s, V] = numpy.linalg.svd(X, full_matrices=False)
    U = U[:,0:m]
    s = s[0:m]
    V = V[0:m,:]
    S = numpy.diag(s)
    C = numpy.dot(S,V)
   # C = numpy.dot(U,numpy.dot(S, V))
    c = pow(numpy.linalg.norm(X, ord='fro'),2) - pow(numpy.linalg.norm(S, ord='fro'),2)
    return [U,C,c]

