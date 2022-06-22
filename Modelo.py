class Modelo:
    def __init__(self, qVar, qRest, obj, rest, rest_0, rest_1, z, vals_vars):
        self.qVar = qVar
        self.qRest = qRest
        self.obj = obj
        self.rest = rest
        self.rest_0 = rest_0
        self.rest_1 = rest_1
        self.z = z
        self.vals_vars = vals_vars

    def setqVar(self, qVar):
        set.qVar = qVar

    def setqRest(self, qRest):
        set.qRest = qRest
    
    def setObj(self, obj):
        set.obj = obj

    def setRest(self, rest):
        set.rest = rest

    def setQVar(self, qVar):
        set.qVar = qVar

    def setRest_0(self, rest_0):
        self.rest_0 = rest_0    
   
    def setRest_1(self, rest_1):
        self.rest_1 = rest_1 

    def setZ(self, z):
        set.z = z

    def setZ(self, vals_vars):
        set.vals_vars = vals_vars



    def getqVar(self, qVar):
        return qVar

    def getqRest(self, qRest):
        return qRest
    
    def getObj(self, obj):
        return obj

    def getRest(self, rest):
        return rest

    def getQVar(self, qVar):
        return qVar

    def getRest_0(self):
        return self.rest_0

    def getRest_1(self):
        return self.rest_1

    def getZ(self, z):
        return z

    def getZ(self, vals_vars):
        return vals_vars