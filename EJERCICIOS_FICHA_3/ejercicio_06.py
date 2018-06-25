_author_ = 'JORGE NAHUEL AQUINO'

#constantes del programa

INC = 0.080
DES = 0.025
CAMPO1 = 'NOMBRE DEL EMPLEADO: '
CAMPO2 = 'NUEVO SALARIO: '
CAMPO3 = 'ÁREA FUNCIONAL: '
CAMPO4 = 'SALARIO ACTUAL: '

#titulo y carga de datos
print("Ejercicio nro 6 - Calculo de sueldo ")
nom_emp = input("Ingrese el nombre del empleado: ")+'\n'
area = input("Ingrese el area funcional a la cual pertenece: ")+'\n'
sal_act = input("Ingrese su salario acutal: ")+'\n'

#procesos..
nuevo_sal = str(round(int(sal_act)+ int(sal_act) * (INC - DES),2))+'\n'

#visualización de resultados
print(CAMPO1+nom_emp+CAMPO2+nuevo_sal+CAMPO3+area+CAMPO4+sal_act)
