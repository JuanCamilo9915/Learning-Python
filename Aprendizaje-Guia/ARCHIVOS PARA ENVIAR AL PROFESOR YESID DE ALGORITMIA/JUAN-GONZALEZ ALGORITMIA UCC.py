#PRIMER TALLER PARA CODIFICAR UN ALGORITMO: ELABORADO POR:(JUAN CAMILO GONZALEZ DUQUE) FACULTAD DE ING. EN SISTEMAS DE LA UCC
#SOLUCION DEL TALLER:
#
#ANALISIS DEL PROBLEMA:
#
#VARIABLES:
#-ESTRATO (1,2,3,4,5,6) 
#-NUMERO DE HIJOS
#-NOMBRE COMPLETO                                                    -NUMERO DE PERSONAS DEPENDIENTES ECONOMICAMENTE DEL CIUDADAN@ 
#-C.C.                                                               -MOSTRAR QUE CONDICIONES NO CUMPLE 
#-AÑO DE NACIMIENTO                                                  -SI ES O NO ES ACEPTAD@ COMO CONCLUSION
#-EDAD
#-ESTATURA
#
#
#SALIDAS:                                                                                               IDENTIFICADORES:                                                                                                               
#-MOSTRAR QUE CONDICIONES NO CUMPLE                                                                         MCNC                           
#-SI ES O NO ES ACEPTAD@ COMO CONCLUSION                                                                    SENEACC                        
#
#
#ENTRADAS:                       
#-NOMBRE COMPLETO                                                                                           NC                       
#-C.C.                                                                                                      CC                       
#-FECHA DE NACIMIENTO                                                                                       FN                        
#-EDAD                                                                                                      ED                       
#-ESTATURA                                                                                                  ETRA                        
#-ESTRATO (1,2,3,4,5,6)                                                                                     ESTO                        
#-NUMERO DE HIJOS                                                                                           NH                        
#-NUMERO DE PERSONAS DEPENDIENTES ECONOMICAMENTE DEL CIUDADAN@                                              NPDEC                       
#
#
#PROCESO:
#1-SI LOS CIUDADAN@S NACIERON ANTES DE 1990
#          MOSTRAR EL MENSAJE "NO ES APT@"
#SI NO
#          MOSTRAR EL MENSAJE "SI ES APT@"
#
#2-SI LOS CIUDADAN@S SON MENORES DE 18 AÑOS
#          MOSTRAR EL MENSAJE "NO ES APT@"
#SI NO
#          MOSTRAR EL MENSAJE "SI ES APT@"
#
#3-SI LOS CIUDADAN@S TIENEN UNA ESTATURA MENOR QUE 1.60MTS
#          MOSTRAR EL MENSAJE "DESCARTAD@ DEL PROCESO"
#SI NO
#          MOSTRAR EL MENSAJE "SI ES APT@ PARA CONTINUAR CON EL PROCESO"
#
#4-SI LOS CIUDADAN@S VIVEN EN UN ESTRATO 4 O 5
#          MOSTRAR EL MENSAJE "DESCARTAD@ EN ESTA CONVOCATORIA"
#SI NO
#          MOSTRAR EL MENSAJE "SI ES APT@ PARA CONTINUAR EN LA CONVOCATORIA"
#
#5-SI LOS CIUDADAN@S TIENEN UN HIJO Y COMO MINIMO DOS PERSONAS DEPENDIENTES ECONOMICAMENTE
#          MOSTRAR EL MENSAJE "ACEPTAD@"
#SI NO
#          MOSTRAR EL MENSAJE "RECHAZAD@"
#
#
#
#INICIO
#       NC=LEER("DIGITE SU NC")
#       CC=LEER("DIGITE SU NUMERO DE CC")
#       AN=LEER("DIGITE SU AN")
#       ED=LEER("DIGITE SU ED")
#       ETRA=LEER("DIGITE SU ETRA")
#       ESTO=LEER("DIGITE SU ESTO")
#       NH=LEER("DIGITE EL NH")
#       NPDEC=LEER("DIGITE CUAL ES NPDEC")
#       
#       SI(LOS CIUDADAN@S QUE NACIERON ANTES DE 1990) 
#               IMPRIMIR("NO ES APT@") 
#       SI NO
#               IMPRIMIR("ES APT@")
#       
#       SI(LOS CIUDADAN@S < 18 AÑOS)
#               IMPRIMIR ("NO ES APT@")
#       SI NO
#               IMPRIMIR("SI ES APT@")
#
#       SI(LOS CIUDADAN@S TIENEN UNA ESTATURA < 1.60MTS)
#               IMPRIMIR ("DESCARTAD@ DEL PROCESO")
#       SI NO
#               IMPRIMIR ("SI ES APT@ PARA CONTINUAR EL PROCESO")
#
#       SI(LOS CIUDADAN@S VIVEN EN UN ESTRATO 4 O 5)
#               IMPRIMIR ("DESCARTAD@ EN ESTA COMVOCATORIA")
#       SI NO
#               IMPRIMIR ("SI ES APT@ PARA CONTINUAR EN LA CONVOCATORIA")
#
#       SI(LOS CIUDADAN@S QUE TIENEN UN HIJO Y COMO MINIMO DOS PERSONAS DEPENDIENTES ECONOMICAMENTE) 
#               IMPRIMIR ("ADMITID@")
#       SI NO
#               IMPRIMIR ("RECHAZAD@")  
#       FIN 
#
#
#       ADMISION DE CIUDADAN@S POSTULADOS A LAS VACANTES DISPONIBLES	PERFIL PROFESIONAL DEL CIUDADAN@	NOMBRE COMPLETO	                       C.C.	        AÑO DE NACIMIENTO	EDAD 	   ESTATURA	ESTRATO (1,2,3,4,5,6)	NUMERO DE HIJOS	     NUMERO DE PERSONAS DEPENDIENTES ECONOMICAMENTE DEL CIUDADAN@	      CONDICIONES CON LAS CUALES NO CUMPLE EL CIUDADAN@	     SI ES O NO ES ACEPTAD@ COMO CONCLUSION
#
#                                                                       NO ESPECIFICADO	                        PEDRO ANTONIO BELALCAZAR TORRES        25.289.156	  07/07/1989	       28 AÑOS	   1,78MTS	       4	                4	                                  2	                                        FECHA DE NACIMIENTO, NUMERO DE HIJOS Y ESTRATO	                  RECHAZADO
#	                                                                NO ESPECIFICADO	                        PAOLA ANDRE SUAREZ LOPEZ	       1.002.589	  12/01/1995	       22 AÑOS	   1,65MTS	       2	                1	                                  2	                                                                X	                                  ADMITIDA
#	                                                                NO ESPECIFICADO	                        ANDREA PEREZ GONZALEZ	               1.213.000	  05/09/1997	       20 AÑOS	   1,70MTS	       3	                0	                                  0	                                                                X	                                  ADMITIDA
#	                        6                                       NO ESPECIFICADO	                        CATALINA GOMEZ SANCHEZ	               1.466.207.000	  24/12/1999	       17 AÑOS	   1,59MTS	       5	                0	                                  0	                                                 EDAD, ESTATURA Y ESTRATO	                          RECHAZADA
#	                                                                NO ESPECIFICADO	                        JUAN PABLO GAVIRIA ROJAS	       22.156.203	  07/02/1961	       66 AÑOS	   1,64MTS	       6	                6	                                  1	                                            FECHA DE NACIMIENTO Y NUMERO DE HIJOS	                  RECHAZADO
#	                                                                NO ESPECIFICADO	                        JOSE DANIEL DUQUE RODRIGUEZ 	       1.574.213	  12/08/1994	       23 AÑOS	   1,86MTS	       1	                0	                                  2	                                                                X	                                  ADMITIDO
#inicio:
#
nombre="nc"
print("digite su nombre completo:")                       
nc=input()
cedula="cc"
print("digite su cedula de ciudadania")
cc=input()
cc1=int(cc)
fecha="año"
print("digite su fecha de nacimiento")
año=input()
fn1=int(año)
edad="e"
print("digite su edad")
e=input()
edad1=int(e)
estatura="esmts"
print("digite su estatura en mts")
esmts=input()
estatura1=int(esmts)
estrato="et"
print("digite su estrato")
et=input()
estratob=int(et)
numerodehijos="nh"
print("digite el numero de hijos")
nh=input()
numerodehijos1=int(nh)
personasquedependendeusted="pdu"
print("digite el numero personas que dependen de usted")
pdu=input()
personasquedependendeusted=int(pdu)

if (fn1<1990):
    print("no es apto")
elif edad1<18:
    print("no es apto")
elif estatura1<160:
    print("no es apto")
elif (estratob==4) or (estratob==5):
    print("descartado")
elif ((numerodehijos1<1) and (personasquedependendeusted<2)): 
    print("descartado")
else:
    print("si es apto")

#fin.   

    

