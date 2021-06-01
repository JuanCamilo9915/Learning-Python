#Juan Camilo Betancourt Giraldo
#Ingenieria de Sistemas
#Primer Semestre 

def aportes (totalsalario, smm):
    ingreso = totalsalario / smm
    if ingreso <= 2:
        totalaporte = totalsalario * 0.01
        return totalaporte
    if ingreso > 2 and ingreso <= 6:
        totalaporte = totalsalario * 0.02
        return totalaporte
    if ingreso > 6:
        totalaporte = totalsalario * 0.025
        return totalaporte


def recreacion (totalsalario, tiempo):
    if tiempo <= 5:
        totalrecreacion = totalsalario * 0.0025
        return totalrecreacion
    if tiempo > 5:
        totalrecreacion = totalsalario * 0.0030
        return totalrecreacion

def fondo (totalsalario):
    print ()
    aporte = input ("desea aportar (4%) al fondo de solidaridad? <si-no>  ")
    if aporte == "si":
        descuentofondo = totalsalario * 0.04
        return descuentofondo
    else:
        return 0 


def pension (totalsalario, tiempo, smm):
    numsalario = totalsalario / smm 
    if tiempo >= 10:
        valorpension = totalsalario * 0.07
        return valorpension
    if numsalario <= 3:
        valorpension = totalsalario * 0.08
        return valorpension
    if numsalario > 3:
        valorpension = totalsalario * 0.1
        return valorpension
        
            
