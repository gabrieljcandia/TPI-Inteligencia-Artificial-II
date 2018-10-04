class Cluster:
    def __init__(self, id, x, y, z):
        self.id = id
        self.x = x
        self.y = y
        self.z = z

    def setX (self, x):
        self.x = x

    def getX(self):
        return self.x

    def setY(self, y):
        self.y = y

    def getY(self):
        return self.y

    def setZ(self, z):
        self.z = z

    def getZ(self):
        return self.z

    def getId(self):
        return self.id

    def getCoordenadasR2(self):
        retornar = [self.x, self.y]
        return retornar

    def getCoordenadasR3(self):
        retornar = [self.x, self.y, self.z]
        return retornar
