#TALLER PARA PRACTICAR CON LOS CONECTORES LOGICOS
nc=input("digite su nombre completo: ")
print=(nc)
edad="ed"
ed=int(input("digite su edad en años: "))
print=(ed)
estratosocial="es"
es=int(input("digite su estrato social: "))
print=(es)
estadodejubilacion="ej"
ej=int(input("digite su estado de jubilacion, 0 si es jubilado o 1 si no es jubilado: "))
print=(ej)
estadolaboral="el"
el=int(input("digite su estado laboral, 0 si esta laborando o 1 si no esta laborando: "))
print=(el)
valortotaldeactivos="vta"
vta=int(input("digite su valor total de activos en pesos: "))
print=(vta)
valordeudas="vd"
vd=int(input("digite su valor total en deudas en pesos: "))
print=(vd)
tipodeestudio="te"
te=int(input("digite su tipo de estudios, 0 si es bachiller, 1 si es tecnologo o 2 si es profesional: "))
print=(te)
if(ed>=18 or ed<=60):
   print=("cumples con la exigencia de la norma")
else:
    print=("no cumples con la exigencia de la norma")
    
if(ej==0 or ej==1):
    print=("cumples con la exigencia de la norma")
else:
    print=("no cumples con la exigencia de la norma")
    
if(el==0):
    print=("cumples con la exigencia de la norma")
else:
    print=("no cumples con la exigencia de la norma")
    
if(vta>=10000000):
    print=("cumples con la exigencia de la norma")
else:
    print=("no cumples con la exigencia de la norma")
    
if(vd<5000000):
    print=("cumples con la exigencia de la norma")
else:
   print=("no cumples con la exigencia de la norma")
   
if(te==2):
   print=("cumples con la exigencia de la norma")
else:
    print=("no cumples con la exigencia de la norma")





