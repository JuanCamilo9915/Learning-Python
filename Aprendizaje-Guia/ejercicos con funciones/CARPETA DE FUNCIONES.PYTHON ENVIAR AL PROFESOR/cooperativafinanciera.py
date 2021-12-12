#SOLUCION TALLER CALIFICABLE: REALIZADO POR JUAN CAMILO GONZALEZ DUQUE-UCC-ING. EN SISTEMAS
#ANALISIS DEL PROBLEMA:
#
#VARIABLES:
#CODIGO DEL ASOCIADO
#VALOR DEL INGRESO MENSUAL DEL ASOCIADO
#NUMERO DE AÑOS QUE LLEVA EL ASOCIADOAFILIADO A LA COOPERATIVA
#SALARIO MINIMO MENSUAL (SMM)=IMPORTANTE
#EL APORTE A LA COPERATIVA
#LA CUOTA PARA EL FONDO DE RECREACION
#LA CUOTA DE PENSION OBLIGATORIA
#
#ENTRADAS:
#CODIGO DEL ASOCIADO
#VALOR DEL INGRESO MENSUAL DEL ASOCIADO
#NUMERO DE AÑOS QUE LLEVA EL ASOCIADOAFILIADO A LA COOPERATIVA
#SALARIO MINIMO MENSUAL (SMM)=IMPORTANTE= NOTA:NO SE TOMA PROPIAMENTE PORQUE ES UN DATO QUE VAMOS A NECESITAR TODO EL TIEMPO, PERO NO SE LO VAMOS A SOLICITAR AL CLIENTE; ASI QUE NO SE VA A MOSTRAR
#
#SALIDAS:
#EL APORTE A LA COPERATIVA
#LA CUOTA PARA EL FONDO DE RECREACION
#LA CUOTA DE PENSION OBLIGATORIA
#
#PROCESO:
#1-VALIDACION DE ENTRADAS
#
#2-EL INGRESO MENSUAL DIVIDIDO POR EL SMM (PASADO A ENTERO)
#-SI IMA ES MENOR O IGUAL A 2:
#           MOSTRAR EL MENSAJE "EL APORTE A LA COOPERATIVA DEL ASOCIADO ES DEL 1.0% DEL SMM"
#-SINO IMA ES MAYOR A 2 Y MENOR O IGUAL A 6:
#           MOSTRAR EL MENSAJE "EL APORTE A LA COOPERATIVA DEL ASOCIADO ES DEL 2.0% DEL SMM"
#SINO IMA ES MAYOR A 6:
#           MOSTRAR EL MENSAJE "EL APORTE A LA COOPERATIVA DEL ASOCIADO ES DEL 2.5% DEL SMM:" 
#DE LO CONTRARIO 
#           MOSTRAR EL MENSAJE "EL DATO QUE SE DIGITO NO ES UN NUMERO, PORFAVOR DIGITAR UN VALOR NUMERICO PARA ESTE DATO"
#
#3-EL NUMERO DE AÑOS QUE LLEVA ASOCIADO A LA COOPERATIVA (PASADO A ENTERO)
#-SI EL ASOCIADO LLEVA 5 AÑOS O MENOS:
#           MOSTRAR EL MENSAJE "LA CUOTA DEL ASOCIADO PARA EL FONDO DE RECREACION ES DEL 0.25% DEL SMM:"
#-SINO EL ASOCIADO LLEVA MAS DE 5 AÑOS:
#            MOSTRAR EL MENSAJE "LA CUOTA DEL ASOCIADO PARA EL FONDO DE RECREACION ES DEL 0.30% DEL SMM:"
#DE LO CONTRARIO 
#           MOSTRAR EL MENSAJE "EL DATO QUE SE DIGITO NO ES UN NUMERO, PORFAVOR DIGITAR UN VALOR NUMERICO PARA ESTE DATO"
#
#4-APORTAR AL FONDO SOLIDARIO POR VOLUNTAD DEL ASOCIADO (PASADO A ENTERO) 
#-SI EL NUMERO DIGITADO POR EL ASOCIADO ES IGUAL AL CERO (0):
#           MOSTRAR EL MENSAJE "EL ASOCIADO APORTA EL 4.0% DEL SMM AL FONDO DE SOLIDARIDAD: "
#-SINO EL NUMERO DIGITADO POR EL ASOCIADO ES IGUAL A UNO (1):
#            MOSTRAR EL MENSAJE "EL ASOCIADO NO DESEA APORTAR AL FONDO DE SOLIDARIDAD"
#DE LO CONTRARIO 
#           MOSTRAR EL MENSAJE "EL DATO QUE SE DIGITO NO ES UN NUMERO, PORFAVOR DIGITAR UN VALOR NUMERICO PARA ESTE DATO"
#
#5-CUOTA DE LA PENSION OBLIGATORIA (PASADO A ENTERO)
#-SI IMA ES MENOR O IGUAL A 3:
#           MOSTRAR EL MENSAJE "EL APORTE A LA PENSION OBLIGATORIA DEL ASOCIADO ES DEL 8% DEL SMM: "
#-SINO IMA ES MAYOR A 3: 
#           MOSTRAR EL MENSAJE "EL APORTE A LA PENSION OBLIGATORIA DEL ASOCIADO ES DEL 10% DEL SMM: "
#SINO EL NUMERO DE AÑOS ASOCIADO A LA COOPERATIVA ES MAYOR O IGUAL A 10 Y IMA ES MENOR O IGUAL A 3: 
#           MOSTRAR EL MENSAJE "EL APORTE A LA PENSION OBLIGATORIA DEL ASOCIADO ES DEL 15% DEL SMM: "
#SINO EL NUMERO DE AÑOS ASOCIADO A LA COOPERATIVA ES MAYOR O IGUAL A 10 Y IMA ES MAYOR A 3: 
#           MOSTRAR EL MENSAJE "EL APORTE A LA PENSION OBLIGATORIA DEL ASOCIADO ES DEL 17% DEL SMM: "
#
#IMPRIMIR("TOTAL NETO DE APORTES DEL ASOCIADO:" , suma)
#a=resultado
#b=resltdo2
#c=rsultd3
#d=rsltd4
#if ((resultado) and (resltdo2) and (rsultd3) and (rsltd4)):
#    if((resultado) and (resltdo2) and (rsultd3) and (rsltd4)):
#        suma=a+b+c+d
#        print(suma)
#    elif ((resultado) and (resltdo2) and (rsltd4)):
#        suma=a+b+d
#        print(suma)
#else:
#     print("EL DATO QUE SE DIGITO NO ES UN NUMERO, PORFAVOR DIGITAR UN VALOR NUMERICO PARA ESTE DATO" , (resultado) and (resltdo2) and (rsultd3) and (rsltd4))
#
#
#NOMBRE DEL ASOCIADO	        CODIGO DEL ASOCIADO	INGRESO MENSUAL DEL ASOCIADO	NUMERO DE AÑOS QUE LLEVA ASOCIADO A LA COOPERATIVA	APORTA AL FONDO DE SOLIDARIDAD
#JUAN CARLOS PEREZ OROZCO	       2015	                   1500000	                                2	                                        NO=1
#TATIANA MARCELA ESPINOSA 	       2016	                   2360000	                                5	                                        SI=0
#SEBASTIAN ANDRES URQUQUI	       2017	                   4800000	                                8	                                        SI=0
#MANUEL TURIZO SANCHEZ	               2018	                   7900000	                               11 	                                        SI=0
#TANIA ARBELAEZ THOUZ	               2019	                    737717	                               10	                                        NO=1
#ISABELLA VASQUEZ FERNANDEZ	       2020	                   3855000	                                3	                                        NO=1
#EMMANUEL FERNANDEZ SUÑIGA	       2021	                   8050000	                                1	                                        NO=1
#KAROLINA SALAZAR BERMUDEZ	       2022	                   1600000	                                5	                                        SI=0
#KARMEN GOMEZ GIRALDO                  2023                        2313000                                     13                                               SI=0                  
#CARLOS ALBERTO OSPITIA                2024                         874300                                     10                                               NO=1
#JOSE ALBERTO                       VEINTE CINCO                   1543000                                      4                                               NO=1
#LUIS EDUARDO                          2026                     $DOS MILLONES                                 SIETE                                             SI=0
#LUZ MILENA                         VEINTI SEIETE               $DOS MILLONES Y MEDIO                         NUEVE                                             NO=1
#SANDRA MARINA                         2028                        3600000                                       9                                              NO=1 
#NOTA: LA OTRA PARTE DEL SEUDOCODIGO ESTA EN LA HOJA DE FUNCIONES. :)
import hojafunciones

nom=input("DIGITE EL NOMBRE DEL ASOCIADO: ")
cod=input("DIGITE EL CODIGO DEL ASOCIADO: ")
digite=hojafunciones.validacion(cod)
print()
print("APORTE A LA COOPERATIVA: ")
print()
ima=input("DIGITE EL INGRESO MENSUAL DEL ASOCIADO, EN PESOS: ")
resultado=hojafunciones.aportes(ima)
print(resultado)
print()
print("CUOTA PARA EL FONDO DE RECREACION: ")
print()
naac=input("DIGITE EL NUMERO DE AÑOS QUE LLEVA EL ASOCIADO EN LA COOPERATIVA: ")
resltdo2=hojafunciones.cuota(naac,ima)
print(resltdo2)
print()
print("APORTE AL FONDO DE SOLIDARIDAD ")
print()
afs=input("SEÑOR USUARIO SI DESEA APORTAR AL FONDO DE SOLIDARIDAD\nMARQUE CERO (0) DE LO CONTRARIO MARQUE UNO (1):")
rsultd3=hojafunciones.fondo(afs,ima)
print(rsultd3)
print()
print("APORTE A PENSION OBLIGATORIO")
print()
rsltd4=hojafunciones.pension(naac,ima)
print(rsltd4)
print()
print("TOTAL DE APORTES DEL ASOCIADO")
a=resultado
b=resltdo2
c=rsultd3
d=rsltd4
if ((resultado) and (resltdo2) and (rsltd4)):
    if((resultado) and (resltdo2) and (rsultd3) and (rsltd4)):
        suma=a+b+c+d
        print(suma)
    elif ((resultado) and (resltdo2) and (rsltd4)):
        suma=a+b+d
        print(suma)
else:
     print("EL DATO QUE SE DIGITO NO ES UN NUMERO, PORFAVOR DIGITAR UN VALOR NUMERICO PARA ESTE DATO" , (resultado) and (resltdo2) and (rsltd4))


























