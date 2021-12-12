#Beatriz Elena Tabares García codigo 505919
#
#ANALISIS DE PROBLEMA
#VARIBLES
#cp
#cp2
#a
#cuv
#cuv2
#vp
#vp2
#contador

#ENTRADAS:
#cp
#a
#cuv
#vp
#contador

#SALIDAS:
#cp
#cuv
#vp
#a
#contador

#PROCESO
#mientras la variable cp2 sea igual a FALSE
#   imprimir ("NO HAS DIGITADO UN NUMERO PARA ESTE DATO:" , cp)
#   cp es igual a leer ("DIGITE (1) SI LA CATEGORIA ES GRANO, (2) SI SON LÁCTEOS,\n(3) SI ES DE ASEO, O (4) SI ES DE CARNE:")
#retornar la variable entero cp

#mientras la variable a sea mayor que 4 o menor que 1
#   imprimir ("Numero digitado no esta en el rango de seleccion:" , a)
#   imprimir ("Digitar un numero entre 1 y 4")
#   la variable entero a es igual a leer ("DIGITE (1) SI LA CATEGORIA ES GRANO, (2) SI SON LÁCTEOS,\n(3) SI ES DE ASEO, O (4) SI ES DE CARNE:"))
#retornar la variable a

#mientras la variable cuv2 sea igual a FALSE
#   imprimir ("NO HAS DIGITADO UN NUMERO PARA ESTE DATO:" , cuv)
#   la variable cuv lee ("¿Cuantas unidades se vendieron en el dia? :")
#retornar la variable cuv

#mientras la variable vp2 sea igual a FALSE
#   imprimir("NO HAS DIGITADO UN NUMERO PARA ESTE DATO:" , vp)
#   la variable vp lee("Digitar el valor unitario del producto : ")
#retorna vp

#mientras la variable contador sea mayor que 2 o menor que 1
#   imprimir ("Numero digitado no esta en el rango de seleccion" , contador)
#   la variable vp lee ("Digitar (1) si desea continuar, de lo contrario digite (2): ")
#retorna contador

#Inicio
#def validacioncategorias(cp):
#    cp2=cp.isdigit()
#    mientras (cp2==False):
#            imprimir("NO HAS DIGITADO UN NUMERO PARA ESTE DATO:" , cp)
#           cp=leer("DIGITE (1) SI LA CATEGORIA ES GRANO, (2) SI SON LÁCTEOS,\n(3) SI ES DE ASEO, O (4) SI ES DE CARNE:")
#            cp2=cp.isdigit()
#    retornar entero (cp)

#def validacioncategorias2(a):
#    mientras (a>4 or a<1):
#            imprimir("Numero digitado no esta en el rango de seleccion:" , a)
#            imprimir("Digitar un numero entre 1 y 4")
#            a=entero(leer("DIGITE (1) SI LA CATEGORIA ES GRANO, (2) SI SON LÁCTEOS,\n(3) SI ES DE ASEO, O (4) SI ES DE CARNE:"))
#    retornar a

#def validacionunidades(cuv):
#    cuv2=cuv.isdigit()
#    mientras (cuv2==False):
#            imprimir("NO HAS DIGITADO UN NUMERO PARA ESTE DATO:" , cuv)
#            cuv=leer("¿Cuantas unidades se vendieron en el dia? :")
#            cuv2=cuv.isdigit()
#    retornar entero (cuv)

#def validacionprecio(vp):
#    vp2=vp.isdigit()
#    mientras (vp2==False):
#            imprimir("NO HAS DIGITADO UN NUMERO PARA ESTE DATO:" , vp)
#            vp=leer("Digitar el valor unitario del producto : ")
#            vp2=vp.isdigit()
#    retornar entero (vp)

#def validacionconteo(contador):
#    mientras (contador>2 or contador<1):
#        imprimir("Numero digitado no esta en el rango de seleccion" , contador)
#        contador=entero(leer("Digitar (1) si desea continuar, de lo contrario digite (2): "))
#    retornar contador

def validacioncategorias(cp):
    cp2=cp.isdigit()
    while (cp2==False):
            print("NO HAS DIGITADO UN NUMERO PARA ESTE DATO:" , cp)
            cp=input("DIGITE (1) SI LA CATEGORIA ES GRANO, (2) SI SON LÁCTEOS,\n(3) SI ES DE ASEO, O (4) SI ES DE CARNE:")
            cp2=cp.isdigit()
    return int (cp)

def validacioncategorias2(a):
    while (a>4 or a<1):
            print("Numero digitado no esta en el rango de seleccion:" , a)
            print("Digitar un numero entre 1 y 4")
            a=int(input("DIGITE (1) SI LA CATEGORIA ES GRANO, (2) SI SON LÁCTEOS,\n(3) SI ES DE ASEO, O (4) SI ES DE CARNE:"))
    return a

def validacionnombre(np):
    np2=np.isdigit()
    while (np2==True):
            print("HAS DIGITADO UN NUMERO PARA ESTE DATO:" , np)
            np=input("Digitar el nombre del producto en letras :")
            np2=np.isdigit()
    return np

def validacionunidades(cuv):
    cuv2=cuv.isdigit()
    while (cuv2==False):
            print("NO HAS DIGITADO UN NUMERO PARA ESTE DATO:" , cuv)
            cuv=input("¿Cuantas unidades se vendieron en el dia? :")
            cuv2=cuv.isdigit()
    return int (cuv)

def validacionprecio(vp):
    vp2=vp.isdigit()
    while (vp2==False):
            print("NO HAS DIGITADO UN NUMERO PARA ESTE DATO:" , vp)
            vp=input("Digitar el valor unitario del producto : ")
            vp2=vp.isdigit()
    return int (vp)

def validacionconteo(contador):
    while (contador>2 or contador<1):
        print("Numero digitado no esta en el rango de seleccion" , contador)
        contador=int(input("Digitar (1) si desea continuar, de lo contrario digite (2): "))
    return contador
