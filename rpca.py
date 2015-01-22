import numpy
import os
from projectsample import ProjectSample

class ORPCA:
    def init(self, d, k):
        self.A = numpy.zeros((k, k))
        self.B = numpy.zeros((d, k))
        self.reset = True

    def basisupdate(self, L, lambda1):
        k = L.shape[1]
        d = L.shape[0]
        Al = self.A + numpy.identity(k)*lambda1
        for i in range(0, k):
            Ll = L[:,i] + (self.B[:,i] - numpy.dot(L, Al[:,i]))/Al[i,i]
            L[:,i] = Ll / max(numpy.linalg.norm(Ll), 1)
        return L

    def optimization(self, X, L, lambda1, lambda2):
        [r, e] = ProjectSample(X, L, lambda1, lambda2, 1e-6, 1000)
        rt = r.T
        self.A += numpy.dot(r, rt)
        self.B += numpy.dot(X - e, rt)
        Ll = self.basisupdate(L, lambda1)
        #print Ll
        if self.reset == False:
            self.R = numpy.append(self.R,r)
            self.E = numpy.append(self.E,e)
        else:
            self.R = r
            self.E = e
            self.reset = False

        return Ll
