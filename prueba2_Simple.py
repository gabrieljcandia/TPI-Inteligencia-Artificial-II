from clases.Clases import Cluster
from Controladora import Controladora

con = Controladora()

c1 = Cluster(1, 1, 1)
c2 = Cluster(2.5, 2.5, 2)
c3 = Cluster(3.5, 3.5, 3.5)
c4 = Cluster(4.6, 4.6, 4.6)
c5 = Cluster(5.8, 5.8, 5.8)

#con.setClusters([c1, c2, c3, c4, c5])
#p = 0
#while p<4:
#    con.simple()
#    p = p + 1

#print()
#print()
#print("Resultado:----------------")
#for x in con.getClusters():
#    print("El clúster: ", x.getCoordenadasR2())
#    print("Contiene a: ")
#    for m in x.getClusters():
#        print("1", m.getX(), m.getY())

#   print("--o--o--o--o--o--o--o--o--o--o--o--")

print("FUNCIONAMIENTO DE LOS CLUSTERS CONTENIDOS:")
c1.agregarCluster(c2)
c1.agregarCluster(c4)
#c2.agregarCluster(c3)
#c2.agregarCluster(c5)
#c3.agregarCluster(c4)
#c3.agregarCluster(c5)

print()
print("El cluster: ", c1.getCoordenadasR2()," tiene los siguientes clústers contenidos: ")
print(c1.getClusters())

print()
print("El cluster: ", c3.getCoordenadasR2()," tiene los siguientes clústers contenidos: ")
print(c3.getClusters())

print()
print("El cluster: ", c2.getCoordenadasR2()," tiene los siguientes clústers contenidos: ")
print(c2.getClusters())

print()
print("El cluster: ", c4.getCoordenadasR2()," tiene los siguientes clústers contenidos: ")
print(c4.getClusters())

print()
print("El cluster: ", c5.getCoordenadasR2()," tiene los siguientes clústers contenidos: ")
print(c5.getClusters())


#resultado = c1.getClustersContenidos()
#print ("El resultado final es: ", resultado)
#for x in resultado:
#    print (x)


