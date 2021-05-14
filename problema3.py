# los numeros consecutivos se sumen 
n = int(input("cabtidad de numeros: "))  #cantidad dr numeros
sumaT = 0 #suma total
while  n > 0 :
    num = int(input("numero:"))
    sumaT = sumaT + sumaDigitos(num)
    n = n - 1