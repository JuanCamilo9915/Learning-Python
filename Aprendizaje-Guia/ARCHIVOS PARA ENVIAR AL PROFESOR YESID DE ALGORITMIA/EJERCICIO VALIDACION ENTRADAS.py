#SOLUCION TALLER NO CALIFICABLE: REALIZADO POR JUAN CAMILO GONZALEZ DUQUE-UCC-ING. EN SISTEMAS
#ANALISIS DEL PROBLEMA:
#
#VARIABLES:
#Nombre del equipo                       PUNTOS OBTENIDOS POR EL EQUIPO
#Cantidad de partidos jugados            DIFERENCIAS DE GOLES
#Cantidad de partidos ganados
#Cantidad de partidos empatados
#Cantidad de partidos perdidos
#Número de goles a favor
#Número de goles en contra.
#
#ENTRADAS:
#Nombre del equipo                       
#Cantidad de partidos jugados            
#Cantidad de partidos ganados
#Cantidad de partidos empatados
#Cantidad de partidos perdidos
#Número de goles a favor
#Número de goles en contra.
#
#
#SALIDAS:
#PUNTOS OBTENIDOS POR EL EQUIPO
#DIFERENCIAS DE GOLES
#
#
#PROCESO:
#1-VALIDAR LAS ENTRADAS
#
#2-SI DEPENDIENDO DEL NUMERO DE PARTIDOS GANADOS
#           MOSTRAR EL MENSAJE "PUNTOS TOTALES DE LOS PARTIDOS GANADOS"   
#
#3-SI DEPENDIENDO DEL NUMERO DE PARTIDOS EMPATADOS
#           MOSTRAR EL MENSAJE "PUNTOS TOTALES DE LOS PARTIDOS EMPATADOS"
#
#4-SI DEPENDIENDO DEL NUMERO DE PARTIDOS PERDIDOS
#           MOSTRAR EL MENSAJE "PUNTOS TOTALES DE LOS PARTIDOS PERDIDOS"
#
#5-SI DEPENDIENDO LA DIFERENCIA DEL NUMERO DE GOLES A FAVOR Y EN CONTRA
#           MOSTRAR EL MENSAJE "DIFERENCIA DE GOLES"
#
#6-SI EL TOTAL DE LOS PUNTOS OBTENIDOS POR EL EQUIPO EN LOS PARTIDOS GANADOS, EMPATADOS Y PERDIDOS 
#           MOSTRAR EL MENSAJE "TOTAL DE PUNTOS OBTENIDOS POR EL EQUIPO DURANTE TODOS LOS PARTIDOS JUGADOS"
#
#
#
#
#
#
#
#INICIO
#       NE=LEER("DIGITE EL NOMBRE DEL EQUIPO DE FUTBOL")
#       PJ=LEER("DIGITE EL TOTAL DE PARTIDOS JUGADOS")
#       PJA=PJ.ISDIGIT()
#       IMPRIMIR (PJA)
#       PG=LEER("DIGITE EL NUMERO DE PARTIDOS GANADOS") 
#       PGA=PG.ISDIGIT()
#       IMPRIMIR (PGA)
#       PE=LEER("DIGITE EL NUMERO DE PARTIDOS EMPATADOS")       
#       PEA=PE.ISDIGIT()
#       IMPRIMIR (PEA)
#       PP=LEER("DIGITE EL NUMERO DE PARTIDOS PERDIDOS")
#       PPA=PP.ISDIGIT()
#       IMPRIMIR (PPA)
#       GF=LEER("DIGITE EL NUMERO DE GOLES A FAVOR")
#       GFA=GF.ISDIGIT()
#       IMPRIMIR (GFA)
#       GC=LEER("DIGITE EL NUMERO DE GOLES EN CONTRA")
#       GCA=GC.ISDIGIT()
#       IMPRIMIR (GCA)
#
#       SI(PGA):
#           PGA1=INT(PG)
#           SI(PGA1*3):
#               IMPRIMIR("PUNTOS TOTALES DE LOS PARTIDOS GANADOS DEL EQUIPO")
#       SI(PEA):
#           PEA1=INT(PE)
#           SI(PEA1*1):
#               IMPRIMIR("PUNTOS TOTALES DE LOS PARTIDOS EMPATADOS DEL EQUIPO")
#       SI(PPA):
#           PPA1=INT(PP)
#           SI(PPA1*0):
#               IMPRIMIR("PUNTOS TOTALES DE LOS PARTIDOS PERDIDOS DEL EQUIPO")
#       SI((GFA) AND (GCA):
#           ((GFA1) AND (GCA1))=INT((GF) AND (GC))
#           SI(GFA1-GCA1):
#               IMPRIMIR("DIFERENCIA DE GOLES QUE TIENE EL EQUIPO")
#       SI(PGA1) + (PEA1) + (PPA1):
#               IMPRIMIR("TOTAL DE PUNTOS OBTENIDOS POR EL EQUIPO DURANTE TODOS LOS PARTIDOS JUGADOS")
#      
# EQUIPO	PUNTOS	PJ	G	E	P	GF	GC	DIF. GS.
#COLOMBIA	 5	3	1	2	0	4	2	  2
#INGLATERRA	 9	3	3	0	0	2	0	  2
#FRANCIA	 1	3	0	1	2	3	5	  2
#E.E.U.U	 2	3	0	2	1	2	7	  5
#HOLANDA	 9	3	3	0	0	5	8	  3
#PORTUGAL	 5	3	1	2	0	7	2	  5
#BRASIL	         4	3	1	1	1	3	1	  2
ne=input("DIGITE EL NOMBRE COMPLETO DEL EQUIPO DE FUTBOL: ")
pj=input("DIGITE EL NUMERO DE PARTIDOS JUGADOS POR EL EQUIPO: ")
pja=pj.isdigit()


pg=input("DIGITE EL NUMERO DE PARTIDOS GANADOS POR EL EQUIPO: ")
pga=pg.isdigit()


if(pga):
    pga1=int(pg)
    print(pga1*3)
        
pe=input("DIGITE EL NUMERO DE PARTIDOS EMPATADOS POR EL EQUIPO: ")
pea=pe.isdigit()


if(pea):
    pea1=int(pe)
    print(pea1*1)
    
pp=input("DIGITE EL NUMERO DE PARTIDOS PERDIDOS POR EL EQUIPO: ")
ppa=pp.isdigit()


if(ppa):
    ppa1=int(pp)
    print(ppa1*0)

gf=input("DIGITE EL NUMERO DE GOLES A FAVOR DEL EQUIPO: ")
gfa=gf.isdigit()

gc=input("DIGITE EL NUMERO DE GOLES EN CONTRA DEL EQUIPO: ")
gca=gc.isdigit()


if((gfa) and (gca)):
    gfa1=int(gf)
    gca1=int(gc)
    pga=pga1*3
    pea=pea1*1
    ppa=ppa1*0

    print("TOTAL DE PUNTOS OBTENIDOS POR EL EQUIPO DURANTE TODOS LOS PARTIDOS JUGADOS: ")
    suma=pga+pea+ppa
    print(suma)

    print("DIFERENCIA DE GOLES DEL EQUIPO: ")
    print(gfa1-gca1)
else:
    print("NO HAS DIGITADO CORRECTAMENTE LOS DATOS, PORFAVOR INGRESAR CARACTERES NUMERICOS")

print("TABLA DE RESULTADOS DEL EQUIPO: ")

print("PARTIDOS JUGADOS" , pj )
print("PARTIDOS GANADOS POR EL EQUIPO" , pga1 )
print("PARTIDOS EMPATADOS POR EL EQUIPO" , pea1 )
print("PARTIDOS PERDIDOS POR EL EQUIPO" , ppa1 )
print("GOLES A FAVOR DEL EQUIPO" , gfa1 )
print("GOLES EN CONTRA DEL EQUIPO" , gca1)
print("PUNTOS TOTALES DEL EQUIPO" , pga+pea+ppa )
print("DIFERENCIA DE GOLES DEL EQUIPO" , gfa1-gca1)







        
        
    




