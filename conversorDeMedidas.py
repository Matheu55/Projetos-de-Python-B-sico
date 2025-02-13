medida = float(input("Distância em metros: "))
cm = medida * 100
mn = medida * 1000
km = medida / 1000
print("A médida de {}m corresponde a {}cm e {}mm e {}Km".format(medida,cm,mn,km))