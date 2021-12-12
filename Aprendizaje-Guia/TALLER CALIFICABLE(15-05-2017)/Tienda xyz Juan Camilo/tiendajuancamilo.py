#Tienda xyz - juan camilo  cod. 509932

#ANALISIS DEL PROBLEMA
#VARIABLES
#contador
#cont1
#cont2
#cont3
#cont4
#c1
#c2
#c3
#c4
#cp
#a
#np
#cuv
#b
#vp
#c
#vltl1
#vltl2
#vltl3
#vltl4
#ivag
#ival
#ivaa
#ivac
#valoriva1
#valoriva2
#valoriva3
#valoriva4
#suma1
#suma2
#suma3

#ENTRADAS:
#contador
#cp
#np
#cuv
#vp

#SALIDAS:
#a
#b
#c
#vltl1
#vltl2
#vltl3
#vltl4
#ivag
#ival
#ivaa
#ivac
#valoriva1
#valoriva2
#valoriva3
#valoriva4
#suma1
#suma2
#suma3

#PROCESO
#mientras la variable contador sea diferente a 2:
#        cp=leer("DIGITE (1) SI LA CATEGORIA ES GRANO, (2) SI SON LÁCTEOS,\n(3) SI ES DE ASEO, O (4) SI ES DE CARNE: ")
#        a=operacionesbeatriz.validacioncategorias(cp)#Revisa que el dato ingresado sea un numero.
#        a=operacionesbeatriz.validacioncategorias2(a)
#        np=leer("Digite el nombre del producto: ")
#        cuv=leer("¿Cuantas unidades se vendieron en el dia? : ")
#        b=operacionesbeatriz.validacionunidades(cuv)#Revisa que el dato ingresado sea un numero.
#        vp=leer("Digitar el valor unitario del producto : ")
#       c=operacionesbeatriz.validacionprecio(vp)#Revisa que el dato ingresado sea un numero.
        
#        si la variable a es igual a 1:
#                la variable cont1 es igual a cont1 más la suma de b  
#                la variable c1 es igual a c
#        de lo contrario(a es igual a 2):
#                cont2 es igual a cont2 más la suma de b
#                c2 es igual a c
#        de lo contrario(a es igual a 3):
#                cont3es igual a cont3 más la suma de b
#                c3 es igual a c
#        de lo contrario(a es igual a 4):
#                cont4 es igual a cont4 más la suma de b
#                c4 es igual a c
                
#        contador=entero(leer("Digitar (1) si desea continuar, de lo contrario digite (2): "))
#        contador=operacionesbeatriz.validacionconteo(contador)#Revisa que el dato ingresado este en el rango establecido.

#vltl1 es igual a cont1 multiplicado por c1
#vltl2 es igual a cont2 multiplicado por c2
#vltl3 es igual a cont3 multiplicado por c3
#vltl4 es igual a cont4 multiplicado por c4

#ivag es igual a vltl1 multiplicado por 0.19
#ival es igual a vltl2 multiplicado por 0.19
#ivaa es igual a vltl3 multiplicado por 0.19
#ivac es igual a vltl4 multiplicado por 0.19 

#valoriva1 es igual a vltl1 más la suma de ivag
#valoriva2 es igual a vltl2 más la suma de ival
#valoriva3 es igual a vltl3 más la suma de ivaa
#valoriva4 es igual a vltl4 más la suma de ivac 

#suma1 es igual a vltl1 más la suma de vltl2 más la suma de vltl3 más la suma de vltl4
#suma2 es igual a(vltl1+ivag)más la suma de(vltl2+ival)más la suma de(vltl3+ivaa)más la suma de(vltl4+ivac)
#suma3 es igual ivag más la suma de ival más la suma de ivaa más la suma de ivac

#si(valoriva1 es mayor que valoriva2 y valoriva1 mayor que valoriva3 y valoriva1 mayor que valoriva4):
#        imprimir("La categoria Granos fue la mas rentable, su valor - IVA de venta fue: ",vltl1)
#de lo contrario (valoriva2 mayor que valoriva1 y valoriva2 mayor que valoriva3 y valoriva2 mayor que valoriva4):
#        imprimir("La categoria Lacteos fue la mas rentable, su valor - IVA de venta fue: ",vltl2)
#de lo contrario (valoriva3 mayor que valoriva1 y valoriva3 mayor que valoriva2 y valoriva3 mayor que valoriva4):
#        imprimir("La categoria Aseo fue la mas rentable, su valor - IVA de venta fue: ",vltl3)
#de lo contrario (valoriva4 mayor que valoriva1 y valoriva4 mayor que valoriva2 y valoriva4 mayor que valoriva3):
#        imprimir("La categoria Carnes fue la mas rentable, su valor - IVA de venta fue: ",vltl4)

#si (valoriva1 menor que valoriva2 y valoriva1 menor que valoriva3 y valoriva1 menor que valoriva4):
#        imprimir("La categoria Granos fue la menos rentable, su valor - IVA de venta fue: ",vltl1)
#de lo contrario (valoriva2 menor que valoriva1 y valoriva2 menor que valoriva3 y valoriva2 menor que valoriva4):
#        imprimir("La categoria Lacteos fue la menos rentable, su valor - IVA de venta fue: ",vltl2)
#de lo contrario (valoriva3 menor que valoriva1 y valoriva3 menor que valoriva2 y valoriva3 menor que valoriva4):
#        imprimir("La categoria Aseo fue la menos rentable, su valor - IVA de venta fue: ",vltl3)
#de lo contrario (valoriva4 menor que valoriva1 y valoriva4 menor que valoriva2 y valoriva4 menor que valoriva3):
#        imprimir("La categoria Carnes fue la memos rentable, su valor - IVA de venta fue: ",vltl4)

#si (valoriva1 es igual valoriva2 y valoriva1 es igual valoriva3 y valoriva1 es igual valoriva4):
#        imprimir("Las categorias (Granos: ",valoriva1,", Lacteos: ",valoriva2,", Aseo: ",valoriva3," y Carnes: ",valoriva4,") tuvieron el mismo valor + IVA de venta y fue: ",valoriva1)
#de lo contrario:
#        imprimir()

#importar operacionesbeatriz

#imprimir()
#imprimir("TIENDA BETY")
#imprimir()

#contador=0#Almacena la decicion del administrador de volver o no a repetir el proceso.
#cont1=0
#cont2=0
#cont3=0
#cont4=0#Los cont1, 2, etc almacenan las unidades de cada producto.

#c1=0
#c2=0
#c3=0
#c4=0#Los c1,2, etc almacenan el costo unitario de cada producto. 

#mientras(contador!=2):
#        cp=leer("DIGITE (1) SI LA CATEGORIA ES GRANO, (2) SI SON LÁCTEOS,\n(3) SI ES DE ASEO, O (4) SI ES DE CARNE: ")
#        a=operacionesbeatriz.validacioncategorias(cp)#Revisa que el dato ingresado sea un numero.
#        a=operacionesbeatriz.validacioncategorias2(a)
#        np=leer("Digite el nombre del producto: ")
#        cuv=leer("¿Cuantas unidades se vendieron en el dia? : ")
#        b=operacionesbeatriz.validacionunidades(cuv)#Revisa que el dato ingresado sea un numero.
#        vp=leer("Digitar el valor unitario del producto : ")
#       c=operacionesbeatriz.validacionprecio(vp)#Revisa que el dato ingresado sea un numero.
        
#        si (a==1):
#                cont1=cont1+b#cont1 almacena y suma la cantidad de productos de Grano vendidos en el dia. 
#                c1=c#c1 almacena el valor unitario del producto Grano.
#        de lo contrario(a==2):
#                cont2=cont2+b#cont2 almacena y suma la cantidad de productos de Lacteos vendidos en el dia.
#                c2=c#c2 almacena el valor unitario del producto Lacteos.
#        de lo contrario(a==3):
#                cont3=cont3+b#cont3 almacena y suma la cantidad de productos de Aseo vendidos en el dia.
#                c3=c#c3 almacena el valor unitario del producto Aseo.
#        de lo contrario(a==4):
#                cont4=cont4+b#cont4 almacena y suma la cantidad de productos de Carne vendidos en el dia.
#                c4=c#c4 almacena el valor unitario del producto carnes.
                
#        contador=entero(leer("Digitar (1) si desea continuar, de lo contrario digite (2): "))
#        contador=operacionesbeatriz.validacionconteo(contador)#Revisa que el dato ingresado este en el rango establecido.

#vltl1=cont1*c1
#vltl2=cont2*c2
#vltl3=cont3*c3
#vltl4=cont4*c4#vltl1, 2, etc almacena el valor total sin IVA de cada categoria.

#ivag=vltl1*0.19
#ival=vltl2*0.19
#ivaa=vltl3*0.19
#ivac=vltl4*0.19#ivag, ival, etc almacena el valor del IVA calculado del total de cada categoria.

#valoriva1=vltl1+ivag
#valoriva2=vltl2+ival
#valoriva3=vltl3+ivaa
#valoriva4=vltl4+ivac#valoriva1, 2, etc almacena el valor total a pagar + el IVA da cada categoria.

#suma1=vltl1+vltl2+vltl3+vltl4#suma1 almacena el valor total global a pagar de todas las categorias sin el IVA.
#suma2=(vltl1+ivag)+(vltl2+ival)+(vltl3+ivaa)+(vltl4+ivac)#suma2 almacena el valor total global a pagar de todas las categorias con el IVA.
#suma3=ivag+ival+ivaa+ivac#suma3 almacena el valor del IVA global de cada categoria.

#imprimir()
#imprimir("VALORES DEL IVA: ")
#imprimir("1-IVA de Grano",ivag,"; IVA de Lacteos",ival,"; IVA de Aseo",ivaa,"; IVA de Carnes",ivac)
#imprimir("2-Valor global cobrado por concepto del IVA de las categorias es: ",suma3)
#imprimir()
#imprimir("VALORES TOTALES DE LAS VENTAS POR CATEGORIAS: ")
#imprimir("1-El total de la categoria Granos sin IVA es de: ",  vltl1 , "con Iva: ", valoriva1)
#imprimir("2-El total de la categoria Lacteos sin IVA es de: ", vltl2 , "con Iva: ", valoriva2)
#imprimir("3-El total de la categoria Aseo sin IVA es de: ",    vltl3 , "con Iva: ", valoriva3)
#imprimir("4-El total de la categoria Carnes sin IVA es de: ",  vltl4 , "con Iva: ", valoriva4)
#imprimir()
#imprimir("VALOR TOTAL A PAGAR RESPECTO A TODAS LAS COMPRAS ANTERIORES: ")
#imprimir("Total a pagar sumando todas las categorias sin IVA: ",suma1,"con Iva: ",suma2)
#imprimir()

#imprimir("RENTABILIDAD DE LAS CATEGORIAS: ")
#imprimir()

#si(valoriva1>valoriva2 and valoriva1>valoriva3 and valoriva1>valoriva4):
#        imprimir("La categoria Granos fue la mas rentable, su valor - IVA de venta fue: ",vltl1)
#de lo contrario (valoriva2>valoriva1 and valoriva2>valoriva3 and valoriva2>valoriva4):
#        imprimir("La categoria Lacteos fue la mas rentable, su valor - IVA de venta fue: ",vltl2)
#de lo contrario (valoriva3>valoriva1 and valoriva3>valoriva2 and valoriva3>valoriva4):
#        imprimir("La categoria Aseo fue la mas rentable, su valor - IVA de venta fue: ",vltl3)
#de lo contrario (valoriva4>valoriva1 and valoriva4>valoriva2 and valoriva4>valoriva3):
#        imprimir("La categoria Carnes fue la mas rentable, su valor - IVA de venta fue: ",vltl4)#Sentencia iterativa de mayor ganancia o rentabilidad.

#si (valoriva1<valoriva2 and valoriva1<valoriva3 and valoriva1<valoriva4):
#        imprimir("La categoria Granos fue la menos rentable, su valor - IVA de venta fue: ",vltl1)
#de lo contrario (valoriva2<valoriva1 and valoriva2<valoriva3 and valoriva2<valoriva4):
#        imprimir("La categoria Lacteos fue la menos rentable, su valor - IVA de venta fue: ",vltl2)
#de lo contrario (valoriva3<valoriva1 and valoriva3<valoriva2 and valoriva3<valoriva4):
#        imprimir("La categoria Aseo fue la menos rentable, su valor - IVA de venta fue: ",vltl3)
#de lo contrario (valoriva4<valoriva1 and valoriva4<valoriva2 and valoriva4<valoriva3):
#        imprimir("La categoria Carnes fue la memos rentable, su valor - IVA de venta fue: ",vltl4)#Sentencia iterativa de menor ganancia o rentabilidad

#si (valoriva1==valoriva2 and valoriva1==valoriva3 and valoriva1==valoriva4):
#        imprimir("Las categorias (Granos: ",valoriva1,", Lacteos: ",valoriva2,", Aseo: ",valoriva3," y Carnes: ",valoriva4,") tuvieron el mismo valor + IVA de venta y fue: ",valoriva1)
#de lo contrario:
#        imprimir()


import operacionesjuancamilo #archivo donde reposan los metodos o funciones.

print()
print("TIENDA XYZ")
print()

contador=0#Almacena la decicion del administrador de volver o no a repetir el proceso.
cont1=0
cont2=0
cont3=0
cont4=0#Los cont1, 2, etc almacenan las unidades de cada producto.

c1=0
c2=0
c3=0
c4=0#Los c1,2, etc almacenan el costo unitario de cada producto.

np1="NN"
np2="NN"
np3="NN"
np4="NN"#losnp1, 2, etc almacenan el nombre del producto.

while(contador!=2):
        cp=input("DIGITE (1) SI LA CATEGORIA ES GRANO, (2) SI SON LÁCTEOS,\n(3) SI ES DE ASEO, O (4) SI ES DE CARNE: ")
        a=operacionesjuancamilo.validacioncategorias(cp)#Revisa que el dato ingresado sea un numero.
        a=operacionesjuancamilo.validacioncategorias2(a)
        np=input("Digite el nombre del producto: ")
        d=operacionesjuancamilo.validacionnombre(np)#Revisa que el dato ingresado sea una cadena.
        cuv=input("¿Cuantas unidades se vendieron en el dia? : ")
        b=operacionesjuancamilo.validacionunidades(cuv)#Revisa que el dato ingresado sea un numero.
        vp=input("Digitar el valor unitario del producto : ")
        c=operacionesjuancamilo.validacionprecio(vp)#Revisa que el dato ingresado sea un numero.
        
        if (a==1):
                cont1=cont1+b#cont1 almacena y suma la cantidad de productos de Grano vendidos en el dia. 
                c1=c#c1 almacena el valor unitario del producto Grano.
                np1=d#np1 almacena el nombre del producto.
        elif(a==2):
                cont2=cont2+b#cont2 almacena y suma la cantidad de productos de Lacteos vendidos en el dia.
                c2=c#c2 almacena el valor unitario del producto Lacteos.
                np2=d#np1 almacena el nombre del producto.
        elif(a==3):
                cont3=cont3+b#cont3 almacena y suma la cantidad de productos de Aseo vendidos en el dia.
                c3=c#c3 almacena el valor unitario del producto Aseo.
                np3=d#np1 almacena el nombre del producto.
        elif(a==4):
                cont4=cont4+b#cont4 almacena y suma la cantidad de productos de Carne vendidos en el dia.
                c4=c#c4 almacena el valor unitario del producto carnes.
                np4=d#np1 almacena el nombre del producto.
                
        contador=int(input("Digitar (1) si desea continuar, de lo contrario digite (2): "))
        contador=operacionesjuancamilo.validacionconteo(contador)#Revisa que el dato ingresado este en el rango establecido.

vltl1=cont1*c1
vltl2=cont2*c2
vltl3=cont3*c3
vltl4=cont4*c4#vltl1, 2, etc almacena el valor total sin IVA de cada categoria.

ivag=vltl1*0.19
ival=vltl2*0.19
ivaa=vltl3*0.19
ivac=vltl4*0.19#ivag, ival, etc almacena el valor del IVA calculado del total de cada categoria.

valoriva1=vltl1+ivag
valoriva2=vltl2+ival
valoriva3=vltl3+ivaa
valoriva4=vltl4+ivac#valoriva1, 2, etc almacena el valor total a pagar + el IVA da cada categoria.

suma1=vltl1+vltl2+vltl3+vltl4#suma1 almacena el valor total global a pagar de todas las categorias sin el IVA.
suma2=(vltl1+ivag)+(vltl2+ival)+(vltl3+ivaa)+(vltl4+ivac)#suma2 almacena el valor total global a pagar de todas las categorias con el IVA.
suma3=ivag+ival+ivaa+ivac#suma3 almacena el valor del IVA global de cada categoria.

print()
print("VALORES DEL IVA: ")
print("1-IVA de Grano",ivag,"; IVA de Lacteos",ival,"; IVA de Aseo",ivaa,"; IVA de Carnes",ivac)
print("2-Valor global cobrado por concepto del IVA de las categorias es: ",suma3)
print()
print("VALORES TOTALES DE LAS VENTAS POR CATEGORIAS: ")
print("1-El total de la categoria Granos (",np1,") sin IVA es de: ",  vltl1 , "con Iva: ", valoriva1)
print("2-El total de la categoria Lacteos (",np2,") sin IVA es de: ", vltl2 , "con Iva: ", valoriva2)
print("3-El total de la categoria Aseo (",np3,") sin IVA es de: ",    vltl3 , "con Iva: ", valoriva3)
print("4-El total de la categoria Carnes (",np4,") sin IVA es de: ",  vltl4 , "con Iva: ", valoriva4)
print()
print("VALOR TOTAL A PAGAR RESPECTO A TODAS LAS COMPRAS ANTERIORES: ")
print("Total a pagar sumando todas las categorias sin IVA: ",suma1,"con Iva: ",suma2)
print()

print("RENTABILIDAD DE LAS CATEGORIAS: ")
print()

if(valoriva1>valoriva2 and valoriva1>valoriva3 and valoriva1>valoriva4):
        print("La categoria Granos (",np1,") fue la mas rentable, su valor - IVA de venta fue: ",vltl1)
elif (valoriva2>valoriva1 and valoriva2>valoriva3 and valoriva2>valoriva4):
        print("La categoria Lacteos (",np2,") fue la mas rentable, su valor - IVA de venta fue: ",vltl2)
elif (valoriva3>valoriva1 and valoriva3>valoriva2 and valoriva3>valoriva4):
        print("La categoria Aseo (",np3,") fue la mas rentable, su valor - IVA de venta fue: ",vltl3)
elif (valoriva4>valoriva1 and valoriva4>valoriva2 and valoriva4>valoriva3):
        print("La categoria Carnes (",np4,") fue la mas rentable, su valor - IVA de venta fue: ",vltl4)#Sentencia iterativa de mayor ganancia o rentabilidad.

if (valoriva1<valoriva2 and valoriva1<valoriva3 and valoriva1<valoriva4):
        print("La categoria Granos (",np1,") fue la menos rentable, su valor - IVA de venta fue: ",vltl1)
elif (valoriva2<valoriva1 and valoriva2<valoriva3 and valoriva2<valoriva4):
        print("La categoria Lacteos (",np2,") fue la menos rentable, su valor - IVA de venta fue: ",vltl2)
elif (valoriva3<valoriva1 and valoriva3<valoriva2 and valoriva3<valoriva4):
        print("La categoria Aseo (",np3,") fue la menos rentable, su valor - IVA de venta fue: ",vltl3)
elif (valoriva4<valoriva1 and valoriva4<valoriva2 and valoriva4<valoriva3):
        print("La categoria Carnes (",np4,") fue la memos rentable, su valor - IVA de venta fue: ",vltl4)#Sentencia iterativa de menor ganancia o rentabilidad

if (valoriva1==valoriva2 and valoriva1==valoriva3 and valoriva1==valoriva4):
        print("Las categorias (Granos : ",valoriva1,", Lacteos: ",valoriva2,", Aseo: ",valoriva3," y Carnes: ",valoriva4,") tuvieron el mismo valor + IVA de venta y fue: ",valoriva1)
else:
        print()
