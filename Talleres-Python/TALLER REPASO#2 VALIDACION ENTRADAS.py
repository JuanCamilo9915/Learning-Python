#SOLUCION TALLER NO CALIFICABLE: REALIZADO POR JUAN CAMILO GONZALEZ DUQUE-UCC-ING. EN SISTEMAS
#ANALISIS DEL PROBLEMA:
#
#VARIABLES:
#NOMBRE DEL PROFESOR                                    PRECIO UNITARIO + IVA POR CD
#CANTIDAD DE ALMAENAMIENTO DEL DISCO DURO EN GB         
#VALOR UNITARIO DEL CD
#CANTIDAD DE CDS
#
#ENTRADAS:
#NOMBRE DEL PROFESOR
#CANTIDAD DE ALMAENAMIENTO DEL DISCO DURO EN GB
#VALOR UNITARIO DEL CD
#
#
#SALIDAS:
#CANTIDAD DE CDS
#PRECIO UNITARIO + IVA POR CD
#
#
#PROCESO:
#1-VALIDAR LAS ENTRADAS
#
#2-SI CADA DISCO DURO EQUIVALE A GB
#           MOSTRAR EL MENSAJE "CONVERCION DE GB A MB"
#
#3-SI LA CAPACIDAD DEL DISCO DURO ESTA EN MBS 
#           MOSTRAR EL MENSAJE "LA CANTIDAD DE CDS QUE SE NECESITAN PARA ALMACENAR ESA INFORMACION"
#
#4-SI SE SABEN CUANTOS CDS SE VAN A UTILZAR
#           MOSTRAR EL MENSAJE "COSTO DEL TOTAL DE CDS + IVA POR UNIDAD DE CD"
#
#5-SI SE CONOCE EL COSTO TOTAL DE LOS CDS + IVA 
#           MOSTRAR EL MENSAJE "COSTO TOTAL + IVA DE LOS CDS QUE SE NECESITAN PARA GUARDAR ESE TAMAÑO DE INFORMACION"
#
#
#INICIO
#       NP=LEER("DIGITE SU NOMBRE")
#       CADD=LEER("DIGITE EL TOTAL DE ALMACENAMIENTO DE SU DISCO DURO, EN GBS")
#       CADDA=CADD.ISDIGIT()
#       IMPRIMIR (CADDA)
#       VUCD=LEER("DIGITE EL COSTO POR UNIDAD DE UN CD, EN PESOS") 
#       VUCDA=VUCD.ISDIGIT()
#       IMPRIMIR (VUCDA)
#       
#
#       SI(CADDA):
#           CADDA1=INT(CADD)
#           SI(CADDA1*1024/1):
#               IMPRIMIR("TOTAL DE MBS QUE EQUIVALEN A CADDA1")
#           SI CADDA1MBS>=700:
#               IMPRIMIR("TOTAL DE CD QUE SE NECESITAN PARA ALMACENAR ESA INFORMACION")
#       SI (VUCDA):
#           VUCDA1=INT(VUCD)
#           SI(VUCDA1*16/100):
#               IMPRIMIR("COSTO TOTAL + IVA POR UNIDAD ES  ")
#
#
#
#
#
#
#
#
np=input("DIGITE SU NOMBRE COMPLETO: ")
cadd=input("DIGITE LA CAPACIDAD DE ALMACENAMIENTO DE SU DISCO DURO, EN GBS: ")
cadda=cadd.isdigit()
vucd=input("DIGITE EL COSTO POR UNIDAD DE UN CD, EN PESOS: ")
vucda=vucd.isdigit()



if(cadda):
    caddaa=int(cadd)
    print("TOTAL DE MBS: ")
    print(caddaa*1024/1)
    
    
    print("TOTAL DE CDS QUE SE NECESITAN PARA ALMACENAR ESA INFORMACION: ")
    print(caddaa*1024/1/700)

if (vucda):
    vucdab=int(vucd)
    print("EL COSTO TOTAL + IVA DE LA CANTIDAD DE CDS ES DE: ")
    print(vucdab*16/100*caddaa*1024/1/700)
    
        





