print("-"*30)
print("CADENAS FORMATEADAS")
print("-"*30)
nombre="Gabriel"
edad=28
mensaje="Mi nombre es {} y tengo {} años.".format(nombre,edad)
print(mensaje)
mitote="""Para enterarlos que 
el dia de ayer me encontré con {}
que no veía desde que se graduó con {}.
y ahora resulta que ya no vive con {}
el que eras amigo de {}
porque se juntó con {}"""
mitote_completo=mitote.format(*nombres.split(","))
print(mitote_completo)