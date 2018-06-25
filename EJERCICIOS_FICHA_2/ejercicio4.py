a=int(input("Ingrese el coeficiente a del polinomio: "))
b=int(input("Ingrese el coeficiente b del polinomio: "))
c=int(input("Ingrese el coeficiente c del polinomio: "))
x=int(input("Ingrese el valor x a evaluar en el polinomio: "))
Valor=a*(x*x)+b*x+c
Disc=(b*b)-4*a*c
print("El el valor obtenido del punto x es:",Valor,"\nEl valor del discrimintante para el calculo de raices es: ",Disc)
