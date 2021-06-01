#SOLUCION DEL TALLER DE LA TIENDA:REALIZADO POR JUAN CAMILO GONZALEZ DUQUE--DUBIER TRUJILLO
#ANALISIS DEL PROBLEMA:
#
#VARIABLES:
#NOMRE DEL PRODUCTO                         TOTAL DE VENTAS
#CATEGORIA DEL PRODUCTO                     NUMERO DE VENTAS REFERENTES A CADA CATEGORIA
#VALOR DEL PRODUCTO                         IMPUESTO IVA DEL 19%
#CANTIDAD EN VENTAS DEL PRODUCTO            CATEGORIA MAS RENTABLE
#
#ENTRADAS:
#
#NOMRE DEL PRODUCTO
#CATEGORIA DEL PRODUCTO
#VALOR DEL PRODUCTO
#CANTIDAD EN VENTAS DEL PRODUCTO
#
#
#SALIDAS:
#
#TOTAL DE VENTAS
#NUMERO DE VENTAS REFERENTES A CADA CATEGORIA
#IMPUESTO IVA DEL 19%
#CATEGORIA MAS RENTABLE
#
#
#PROSESOS:
#
#solicitud nombre del producto
#solicitar la categoria del producto
#solicitar el costo del producto del producto
#solicitartar la cantidad de unidades vendidas del producto
#mostrar el total de las ventas
#sumar ventas por cada categoria arrojar, un valor total por cada categoria
#sumar el valor de ventas entre todas las categorias, dar un monto total.
#sacar el respectivo Valor de IVA  cada venta, sumarla y dar un monto total.
#arrojar la categoria que mas ventas obtuvo
#
#
#PSEUDOCODIGO:
#import hojafunciller2
#
#print()
#print("TIENDA XYZ")
#print()
#print("XYZ TE DE LA BIENVENIDA :)")
#print()
#cotin = 0
#while (cotin>-1):
#    cate=input("DIGITE (1) SI LA CATEGORIA ES GRANO, (2) SI SON LÁCTEOS,(3) SI ES DE ASEO, O (4) SI ES DE CARNE:")
#    vali=hojafunciller2.validacioncategorias(cate)
#    uni1=0;
#    valr1=0;
#    uni2=0;
#    valr2=0;
#    uni3=0;
#    valr3=0;
#    uni4=0;
#    valr4=0;
#    while (vali>4 or vali<=0):
#        print("HAS DIGITADO UN DATO QUE NO ESTA COMTEMPLADO EN LOS PARAMETROS PREVISTOS:" , vali)
#        cate=input("DIGITE (1) SI LA CATEGORIA ES GRANO, (2) SI SON LÁCTEOS,(3) SI ES DE ASEO, O (4) SI ES DE CARNE:")
#        vali=int(cate)
#    if (vali==1):
#        prod=input("DIGITE EL NOMBRE DEL PRODUCTO:")
#        uni1=input("DIGITE LA CANTIDAD DE UNIDADES VENDIDAS DEL PRODUCTO EN EL DIA:")
#        unin1=hojafunciller2.categoproduc(uni1)
#        valr1=input("DIGITE EL VALOR DEL PRODUCTO:")
#        vlor1=hojafunciller2.costoproducto(valr1)
#    elif (vali==2):
#        prod=input("DIGITE EL NOMBRE DEL PRODUCTO:")
#        uni2=input("DIGITE LA CANTIDAD DE UNIDADES VENDIDAS DEL PRODUCTO EN EL DIA:")
#        unin2=hojafunciller2.categoproduc(uni2)
#        valr2=input("DIGITE EL VALOR DEL PRODUCTO:")
#        vlor2=hojafunciller2.costoproducto(valr2)
#    elif (vali==3):
#        prod=input("DIGITE EL NOMBRE DEL PRODUCTO:")
#        uni3=input("DIGITE LA CANTIDAD DE UNIDADES VENDIDAS DEL PRODUCTO EN EL DIA:")
#        unin3=hojafunciller2.categoproduc(uni3)
#       valr3=input("DIGITE EL VALOR DEL PRODUCTO:")
#        vlor3=hojafunciller2.costoproducto(valr3)
#    elif (vali==4):
#        prod=input("DIGITE EL NOMBRE DEL PRODUCTO:")
#        uni4=input("DIGITE LA CANTIDAD DE UNIDADES VENDIDAS DEL PRODUCTO EN EL DIA:")
#        unin4=hojafunciller2.categoproduc(uni4)
#        valr4=input("DIGITE EL VALOR DEL PRODUCTO:")
#        vlor4=hojafunciller2.costoproducto(valr4)
#    cotin=int(input("SI DESEA CONTINUAR DIGITE (0) DE LO CONTRARIO DIGITE UN NUMERO NEGATIVO:"))
#
#
import hojafunciller2

print()
print("TIENDA XYZ")
print()
print("XYZ TE DE LA BIENVENIDA :)")
print()
cotin = 0
while (cotin>-1):
    cate=input("DIGITE (1) SI LA CATEGORIA ES GRANO, (2) SI SON LÁCTEOS,(3) SI ES DE ASEO, O (4) SI ES DE CARNE:")
    vali=hojafunciller2.validacioncategorias(cate)
    uni1=0;
    valr1=0;
    uni2=0;
    valr2=0;
    uni3=0;
    valr3=0;
    uni4=0;
    valr4=0;
    while (vali>4 or vali<=0):
        print("HAS DIGITADO UN DATO QUE NO ESTA COMTEMPLADO EN LOS PARAMETROS PREVISTOS:" , vali)
        cate=input("DIGITE (1) SI LA CATEGORIA ES GRANO, (2) SI SON LÁCTEOS,(3) SI ES DE ASEO, O (4) SI ES DE CARNE:")
        vali=int(cate)
    if (vali==1):
        prod=input("DIGITE EL NOMBRE DEL PRODUCTO:")
        uni1=input("DIGITE LA CANTIDAD DE UNIDADES VENDIDAS DEL PRODUCTO EN EL DIA:")
        unin1=hojafunciller2.categoproduc(uni1)
        valr1=input("DIGITE EL VALOR DEL PRODUCTO:")
        vlor1=hojafunciller2.costoproducto(valr1)
    elif (vali==2):
        prod=input("DIGITE EL NOMBRE DEL PRODUCTO:")
        uni2=input("DIGITE LA CANTIDAD DE UNIDADES VENDIDAS DEL PRODUCTO EN EL DIA:")
        unin2=hojafunciller2.categoproduc(uni2)
        valr2=input("DIGITE EL VALOR DEL PRODUCTO:")
        vlor2=hojafunciller2.costoproducto(valr2)
    elif (vali==3):
        prod=input("DIGITE EL NOMBRE DEL PRODUCTO:")
        uni3=input("DIGITE LA CANTIDAD DE UNIDADES VENDIDAS DEL PRODUCTO EN EL DIA:")
        unin3=hojafunciller2.categoproduc(uni3)
        valr3=input("DIGITE EL VALOR DEL PRODUCTO:")
        vlor3=hojafunciller2.costoproducto(valr3)
    elif (vali==4):
        prod=input("DIGITE EL NOMBRE DEL PRODUCTO:")
        uni4=input("DIGITE LA CANTIDAD DE UNIDADES VENDIDAS DEL PRODUCTO EN EL DIA:")
        unin4=hojafunciller2.categoproduc(uni4)
        valr4=input("DIGITE EL VALOR DEL PRODUCTO:")
        vlor4=hojafunciller2.costoproducto(valr4)
    suma=unin1+unin2+unin3+unin4
    cotin=int(input("SI DESEA CONTINUAR DIGITE (0) DE LO CONTRARIO DIGITE UN NUMERO NEGATIVO:"))
print("A TERMINADO EL PROCEDIMIENTO CORRESPNDIENTE")
