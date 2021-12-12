#Victor Belalcazar Calero
#Ingenieria idustrial
#Primer semestre
#Ucc

#                               TIENDA
#VARIABLES
#Nombre del producto
#Categoria
#precio del producto
#Cantidad unidades vendidas

#ENTRADAS
#Nombre del producto
#Categoria a la que pertenece
#precio del producto
#Cantidad unidades vendidas

#PROCESO
# 1 - validar entradas
# 2 - ingresar nombre producto
# 3 - selecionar la categoria que pertenece
# 4 - digite valor del producto
# 5 - ingresar cantidad de unidades vendidas
# 6 - Preguntar si desea ingresar otro producto
 
#SALIDA
# indicar la categoria más rentable
# total ventas acumulado por categoria grano
# total ventas acumulado por categoria lacteos
# total ventas acumulado por categoria aseo
# total ventas acumulado por categoria carnes
# total ventas acumulado por dia
# valor globar cobrado iva 19%, para la venta calculada por dia

#PRUEBA ESCRITORIO
#                               CATEGORIA
#               1. GRANO  2. LACTEOS  3. ASEO   4. CARNES
#
#PRODUCTO         CATEGORIA     VALOR PRODUCTO     UNIDADES VENDIDAS    
#ARROZ              GRANO           1500                    3                               
#LECHE              LACTEOS         3000                    2
#LIPIDO             ASEO            1200                    4
#POLLO              CARNES          9000                    4  

def grano(valor,unidades):
    cont1=0
    cont1=cont1+(valor*unidades) 
    return cont1
def ivagrano(valor,unidades):
    cont5=0
    cont5=cont5+(valor*0.19*unidades)
    return cont5
def unidadgrano(unidades):
    cont9=0
    cont9=cont9+unidades 
    return cont9

def lacteos(valor,unidades):
    cont2=0
    cont2=cont2+(valor*unidades) 
    return cont2
def ivalacteos(valor,unidades):
    cont6=0
    cont6=cont6+(valor*0.19*unidades)
    return cont6
def unidadlacteos(unidades):
    cont10=0
    cont10=cont10+unidades
    return cont10

def aseo(valor,unidades):
    cont3=0
    cont3=cont3+(valor*unidades) 
    return cont3
def ivaaseo(valor,unidades):
    cont7=0
    cont7=cont7+(valor*0.19*unidades)
    return cont7
def unidadaseo(unidades):
    cont11=0
    cont11=cont11+unidades 
    return cont11

def carnes(valor,unidades):
    cont4=0
    cont4=cont4+(valor*unidades) 
    return cont4
def ivacarnes(valor,unidades):
    cont8=0
    cont8=cont8+(valor*0.19*unidades)
    return cont8
def unidadcarnes(unidades):
    cont12=0
    cont12=cont12+unidades 
    return cont12

x=0
a=0
b=0
c=0
d=0
e=0
f=0
g=0
h=0
i=0
j=0
k=0
l=0
while(x!=2):
    producto=input("Ingrese el nombre del producto ")
    opcion=int(input("\nINGRESE LA CATEGORIA\n\n1. Grano \n2. Lacteos \n3. Aseo \n4. Carnes \nDigite la opcion "))#cateoria
    valor=int(input("\nIngrese el valor del producto ")) 
    unidades=int(input("\nIngrese el numero de unidades vendidas "))
    if(opcion==1):
        a=grano(valor,unidades)
        e=ivagrano(valor,unidades)
        i=unidadgrano(unidades)
    elif(opcion==2):
        b=lacteos(valor,unidades) 
        f=ivalacteos(valor,unidades)
        j=unidadlacteos(unidades)
    elif(opcion==3):
        c=aseo(valor,unidades)
        g=ivaaseo(valor,unidades)
        k=unidadaseo(unidades)
    elif(opcion==4):   
        d=carnes(valor,unidades)
        h=ivacarnes(valor,unidades)
        l=unidadcarnes(unidades)
    elif(opcion > 4):
        print("\nPor favor ingrese una opcion de 1 a 4\n")
    x=int(input("\ndesea ingresar otro producto\n1.si\n2.no\n"))

totalg=a 
totall=b 
totala=c 
totalc=d 
totalfinal=totalg+totall+totala+totalc 


iva1=e 
iva2=f 
iva3=g 
iva4=h 
ivatotal=iva1+iva2+iva3+iva4 


rentable1=i 
rentable2=j 
rentable3=k 
rentable4=l

if(rentable1>rentable2 and rentable1>rentable3 and rentable1>rentable4):
    print("la categoria mas rentable es Grano")
elif(rentable2>rentable1 and rentable2>rentable3 and rentable2>rentable4):
    print("la categoria mas rentable es Lacteos")
elif(rentable3>rentable1 and rentable3>rentable2 and rentable3>rentable4):
    print("la categoria mas rentable es Aseo")
elif(rentable4>rentable1 and rentable4>rentable2 and rentable4>rentable3):
    print("la categoria mas rentable es Carnes")

print("El total de ventas acumulado por la categoria de grano es $",totalg)
print("El total de ventas acumulado por la categoria de lacteos es $",totall)
print("El total de ventas acumulado por la categoria de aseo es $",totala)
print("El total de ventas acumulado por la categoria de carnes es $",totalc)
print("El total de ventas en el dia es $",totalfinal)
print("El valor global por concepto del iva es $",ivatotal)



      

