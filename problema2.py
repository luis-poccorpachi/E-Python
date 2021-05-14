#halla el volumen de un cilindro
from math import pi

def  volumen(r,h):
    v= pi * r**2 * h
    return v

radio= float(input("radio:"))
altura= float(input( "altura:"))

vol = volumen(radio,altura)

print("v =",vol)

        