import math

#Realiza el cálculo de la distancia, utilizando Pitágoras, en 2 dimensiones
def distanciaR2(p1, p2):
    retorno = math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
    return retorno

#Realiza el cálculo de la distancia, utilizando Pitágoras, en 3 dimensiones
def distanciaR3(p1, p2):
    retorno = math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2)
    return retorno

def metodoSingle():

    return 1

def metodoComplete():
    return 2

def metodoAverage():
    return 3


x = [0, 0]
y = [3, 4]

d = math.sqrt(((x[0]-y[0])**2+(x[1]-y[1])**2)) #Fórmula del cálculo de la distancia
print(d)

d2 = distanciaR2(x, y)
print(d2)
