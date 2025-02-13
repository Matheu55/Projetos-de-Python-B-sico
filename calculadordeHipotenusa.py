from math import hypot

comcateoposto = float(input("comprimento do cateto oposto: "))
catadjcente = float(input("Comprimento do cateto adjacente: "))
hip = hypot(comcateoposto, catadjcente)
print("A hipotenusa vai medir {:.2f} ".format(hip))