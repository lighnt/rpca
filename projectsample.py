import numpy as np
import scipy

def ProjectSample(X, L, lambda1, lambda2, delta, itr):
    dd = L.shape[0]
    dk = L.shape[1]
    e = np.zeros((dd,1))
    en = np.zeros((dd, 1))
    #rn = np.zeros((L.shape[1], 1))
    r = np.zeros((dk, 1))
    LT = L.T
    LTL = np.dot(LT, L)
    A = LTL + np.identity(dk)*lambda1
    #A = np.linalg.inv(A)
    solc = scipy.linalg.cholesky(A)
    LTX = np.dot(LT, X)
    for i in range(0, itr):
        b = LTX - np.dot(LT, e)
        rn = scipy.linalg.cho_solve((solc, False), b)
        en = np.zeros((dd, 1))
       # rn = np.dot(A,b)
       # print np.dot(A,rn)-b
        et = X - np.dot(L, rn)
        for j in range(0, dd):
            en[j] = max(et[j] - lambda2, 0) + min(et[j] + lambda2, 0)
        #print np.linalg.norm(e - en), np.linalg.norm(r - rn)
        if max(np.linalg.norm(e - en), np.linalg.norm(r - rn))/dd < delta:
            break
        r = rn
        e = en
        ritr = i
    print 'Iteration is ', ritr+1
    return [rn, en]
