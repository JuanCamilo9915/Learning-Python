#Juan Camilo Betancourt Giraldo
#Ingeniera de Sistemas
#Primer Semestre

import funciones
import os

seguir = "si"
SMM = 689454

while seguir == "si":
    
    os.system ("cls") 
    titulo = ("CALCULO DE LOS APORTES A LA COOPERATIVA EL FINANCIERO")
    print (titulo.center (70, " "))
    print ()
    print ("SALARIO MINIMO MENSUAL(SMM) = $ 689454")
    print ()
    
    while True:
        try:
            codigo = input ("Digite por favor su codigo de asociado:  ") 
            if codigo.isdigit () == True:
                codigoa = int (codigo)
                break
            else:

                print ("Digite solo numeros")
        except ValueError:
            print ("")


    print ()
    
    while True:
        try:
            ingresomes = input ("Digite por favor su salario mensual:  ")  
            if ingresomes.isdigit () == True:
                ingresoxmes = int (ingresomes)
                if ingresoxmes < SMM:
                    print ("Su valor es menor que el salario basico")
                else:
                    break
            else:
                print ("Digite solo numeros")
        except ValueError:
            print ("")
            
    print ()
    
    while True:
        try:
            asoaños = input ("Digite por favor cantidad de años como asociado:  ") 
            if asoaños.isdigit () == True:
                años = int (asoaños)
                break
            else:
                print ("Digite solo numeros")
        except ValueError:
            print ("")


    descuento = funciones.aportes (ingresoxmes, SMM) 

    aporterecrea = funciones.recreacion (ingresoxmes, años)

    aportefondo = funciones.fondo (ingresoxmes)

    aportepension = funciones.pension (ingresoxmes, años, SMM)

    neto = descuento + aporterecrea + aportefondo + aportepension

    print ()
    print ("su aporte a la cooperativa es de: $", "%.0f" % descuento)
    print ("su aporte para el fondo de recreacion es de: $", "%.0f" % aporterecrea)
    print ("su aporte al fondo de solidaridad es de: $", "%.0f" % aportefondo)
    print ("su aporte para pension es de: $", "%.0f" % aportepension)
    print ()
    print ("el total de sus aportes a la cooperativa es de: $", "%.0f" % neto)

    print ()
    seguir = input ("desea hacer una nueva operacion? <si-no>  ")


    
    

 
