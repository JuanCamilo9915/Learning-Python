"""
Juan Camilo Betancourt Giraldo
Ingenieria de Sistemas
Primer semestre 

Cálculo de los aportes a la cooperativa “El Financiero”

* analisis
    - entradas:
       - codigo de asociado
       - valor del ingreso mensual
       - # de años como asociado
    - salidas:
       - cantidad de aporte a la cooperativa
    -constante:
       - salario minimo mensual
       
*pseudocodigo

    inicio
       SMM = 600000
       codigo = int
       ingresomes = int
       añosdeasociado = int
       seguir = "si"

       mientras seguir == "si" entonces
       
          imprimir (" valor de el salario minimo mensual: 689454")
         
          imprimir ("ingrese por favor su codigo de asociado: ")
          leer codigo
          imprimir ("ingrese por favor el valor de sus ingresos en salarios mensuales ")
          leer ingresomes
          imprimir ("cuantos años lleva de asociado en "LA COOPERATIVA"?")
          leer añosdeasociado

          funcion aportes (totalsalari0, smm) 
              ingresos = totalsalario / smm
              si ingreso <= 2 entonces
                 totalaporte = totalsalario * 0.01
                 retornar totalaporte
              si ingreso > 2 y ingreso <= 6 entonces
                 totalaporte = totalsalario * 0.02
                 retornar totalaporte
              si ingreso > 6:
                 totalaporte = totalsalario * 0.025
                 retornar totalaporte
          fin de funcion

          funcion recreacion (totalsalario, tiempo)
             si tiempo <= 5 entonces 
                totalrecreacion = totalsalario * 0.0025
                retornar totalrecreacion
             si tiempo > 5 entonces 
                totalrecreacion = totalsalario * 0.0030
                retornar totalrecreacion
          fin de funcion

          funcion fondo (totalsalario)
             imprimir ("desea aportar (4%) al fondo de solidaridad? <si-no>  ")
             leer aporte 
             si aporte == "si" entonces 
                descuentofondo = totalsalario * 0.04
                retornar descuentofondo
          fin de funcion

          funcion pension (totalsalario, tiempo, smm)
             numsalario = totalsalario / smm 
             si tiempo >= 10 entonces 
                valorpension = totalsalario * 0.07
                retornar valorpension
             sino entonces 
                si numsalario <= 3 entonces 
                   totalsalario * 0.08
                   retornar totalsalario
                sino entonces 
                   totalsalario * 0.1
                   retornar totalsalario
          fin de funcion

          descuento = aportes (ingresoxmes, SMM) 

          aporterecrea = recreacion (ingresoxmes, años)

          aportefondo = fondo (ingresoxmes)

          aportepension = pension (ingresoxmes, años, SMM)

          neto = descuento + aporterecrea + aportefondo + aportepension

    
          imprimir ("su aporte a la cooperativa es de:", descuento)
          imprimir ("su aporte para el fondo de recreacion es de:", aporterecrea)
          imprimir("su aporte al fondo de solidaridad es de:", aportefondo)
          imprimir ("su aporte para pension es de:", aportepension)
          imprimir("el total de sus aportes a la cooperativa es de:", neto)

          imprimir ("desea hacer una nueva operacion? <si-no>")
          leer seguir
       fin mientras
    fin


* prueba de escritorio

salario minimo mensual = 689454

|  codigo  |  ingreso x mes  |  años de asociado  |  fondo solidaridad  |  aporte cooperativa  |  fondo de recreacion  |  aporte solidaridad  |  pension  |  total  |
|  874022  |    700000       |        10          |         si          |        7000          |         2100          |         28000        |   49000   |  86100  |
|  032328  |   1300000       |        5           |         si          |        32000         |         4000          |         64000        |  128000   | 228000  |
|  685436  |   4900000       |        7           |         no          |       122500         |        14700          |           0          |  490000   | 627200  |

          
Juan Camilo Betancourt Giraldo
Ingenieria de Sistemas
Primer semestre 

             
              
          

          
