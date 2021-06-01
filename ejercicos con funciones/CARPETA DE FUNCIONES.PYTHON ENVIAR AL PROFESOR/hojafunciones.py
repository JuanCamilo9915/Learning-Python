#SOLUCION TALLER CALIFICABLE: REALIZADO POR JUAN CAMILO GONZALEZ DUQUE-UCC-ING. EN SISTEMAS
#INICION
#       INICIO
#       nom=LEER("DIGITE EL NOMBRE DEL ASOCIADO: ")
#       cod=LEER("DIGITE EL CODIGO DEL ASOCIADO: ")
#       coda=cod.isdigit()
#       ima=LEER("DIGITE EL INGRESO MENSUAL DEL ASOCIADO, EN PESOS: ")
#       imaa=ima.isdigit()
#IMPRIMIR ("APORTE A LA COOPERATIVA:")
#def aportes (ima):
#    imaa=ima.isdigit()
#    SI(imaa):
#        imaa1=int(ima)
#        imaa12=(imaa1/737717)
#        SI (imaa12<=2):
#           aporte=(round(imaa1*0.01))
#            print("EL APORTE A LA COOPERATIVA DEL ASOCIADO ES DEL 1.0% DEL SMM Y EQUIVALE A: ")
#            return aporte
#        SINO (imaa12>2 and imaa12<=6):
#           aporte=(round(imaa1*0.02))
#            print("EL APORTE A LA COOPERATIVA DEL ASOCIADO ES DEL 2.0% DEL SMM Y EQUIVALE A:")
#            return aporte
#        SINO (imaa12>6):
#            aporte=(round(imaa1*0.025))
#            print("EL APORTE A LA COOPERATIVA DEL ASOCIADO ES DEL 2.5% DEL SMM Y EQUIVALE A:")
#            return aporte
#    DE LO CONTRARIO:
#        SI (ima):
#            print("EL DATO QUE SE DIGITO NO ES UN NUMERO, PORFAVOR DIGITAR UN VALOR NUMERICO PARA ESTE DATO:")
#            return ima 
#
#
#IMPRIMIR ("CUOTA PARA EL FONDO DE RECREACION:")
#def cuota (naac,ima):
#    naaca=naac.isdigit()
#    imaa=ima.isdigit()
#    SI ((naaca) and (imaa)):
#       nuan=int(naac)
#        imaa1=int(ima)
#       SI(nuan<=5):
#            cuota=(round(imaa1*0.25/100))
#            print("LA CUOTA DEL ASOCIADO PARA EL FONDO DE RECREACION ES DEL 0.25% DEL SMM Y EQUIVALE A:")
#            return cuota
#        SINO (nuan>5):
#            cuota=(round(imaa1*0.30/100))
#            print("LA CUOTA DEL ASOCIADO PARA EL FONDO DE RECREACION ES DEL 0.30% DEL SMM Y EQUIVALE A:")
#            return cuota
#    DE LO CONTRARIO:
#       print("EL DATO QUE SE DIGITO NO ES UN NUMERO, PORFAVOR DIGITAR UN VALOR NUMERICO PARA ESTE DATO")
#        return (naac and ima)
#
#IMPRIMIR("APORTE AL FONDO DE SOLIDARIDAD ")
#def fondo (afs,ima):
#    afsa=afs.isdigit()
#    imaa=ima.isdigit()
#    SI ((afsa) and (imaa)):
#        afsa1=int(afs)
#        imaa1=int(ima)
#       SI (afsa1==0):
#            fondosol=(round(imaa1*0.04))
#            print("EL ASOCIADO DECIDE APORTAR EL 4.0% DEL SMM AL FONDO DE SOLIDARIDAD Y EQUIVALE A: ")
#            return fondosol
#        SINO afsa1==1:
#            fondosol=(round(imaa1*0))
#            print("EL ASOCIADO DECIDE NO APORTAR AL FONDO DE SOLIDARIDAD: ")
#            return fondosol
#    DE LO CONTRARIO:
#        print("EL DATO QUE SE DIGITO NO ES UN NUMERO, PORFAVOR DIGITAR UN VALOR NUMERICO PARA ESTE DATO")
#        return (afs and ima)
#
#
#IMPRIMIR("APORTE A PENSION OBLIGATORIO")
#def pension (naac,ima):
#    naaca=naac.isdigit()
#    imaa=ima.isdigit()
#    SI ((naaca) and (imaa)):
#        nuan=int(naac)
#        imaa1=int(ima)
#        imaa12=(imaa1/737717)
#       SI (nuan>=10) and (imaa12<=3):
#            pension=(round(imaa1*0.15))
#            print("EL APORTE A LA PENSION OBLIGATORIA DEL ASOCIADO ES DEL 15% DEL SMM Y EQUIVALE A: ")
#            return pension
#        SINO (nuan>=10) and (imaa12>3):
#            pension=(round(imaa1*0.17))
#            print("EL APORTE A LA PENSION OBLIGATORIA DEL ASOCIADO ES DEL 17% DEL SMM Y EQUIVALE A: ")
#            return pension
#        SINO (imaa12<=3):
#            pension=(round(imaa1*0.08))
#            print("EL APORTE A LA PENSION OBLIGATORIA DEL ASOCIADO ES DEL 8% DEL SMM Y EQUIVALE A: ")
#            return pension
#       SINO (imaa12>3):
#            pension=(round(imaa1*0.1))
#            print("EL APORTE A LA PENSION OBLIGATORIA DEL ASOCIADO ES DEL 10% DEL SMM Y EQUIVALE A: ")
#            return pension
#    DE LO CONTRARIO:
#        print("EL DATO QUE SE DIGITO NO ES UN NUMERO, PORFAVOR DIGITAR UN VALOR NUMERICO PARA ESTE DATO")
#       return (naac and ima)
#
#IMPRIMIR("TOTAL NETO DE APORTES DEL ASOCIADO:" , suma)
def validacion (cod):
    coda=cod.isdigit()
    if (coda):
        coda1=int(cod)
        return coda1
    else:
        print("EL DATO QUE SE DIGITO NO ES UN NUMERO, PORFAVOR DIGITAR UN VALOR NUMERICO PARA ESTE DATO")
        return cod

    
def aportes (ima):
    imaa=ima.isdigit()
    if(imaa):
        imaa1=int(ima)
        imaa12=(imaa1/737717)
        if (imaa12<=2):
            aporte=(round(imaa1*0.01))
            print("EL APORTE A LA COOPERATIVA DEL ASOCIADO ES DEL 1.0% DEL SMM Y EQUIVALE A: ")
            return aporte
        elif (imaa12>2 and imaa12<=6):
            aporte=(round(imaa1*0.02))
            print("EL APORTE A LA COOPERATIVA DEL ASOCIADO ES DEL 2.0% DEL SMM Y EQUIVALE A:")
            return aporte
        elif (imaa12>6):
            aporte=(round(imaa1*0.025))
            print("EL APORTE A LA COOPERATIVA DEL ASOCIADO ES DEL 2.5% DEL SMM Y EQUIVALE A:")
            return aporte
    else:
        if (ima):
            print("EL DATO QUE SE DIGITO NO ES UN NUMERO, PORFAVOR DIGITAR UN VALOR NUMERICO PARA ESTE DATO:")
            return ima 

def cuota (naac,ima):
    naaca=naac.isdigit()
    imaa=ima.isdigit()
    if ((naaca) and (imaa)):
        nuan=int(naac)
        imaa1=int(ima)
        if(nuan<=5):
            cuota=(round(imaa1*0.25/100))
            print("LA CUOTA DEL ASOCIADO PARA EL FONDO DE RECREACION ES DEL 0.25% DEL SMM Y EQUIVALE A:")
            return cuota
        elif (nuan>5):
            cuota=(round(imaa1*0.30/100))
            print("LA CUOTA DEL ASOCIADO PARA EL FONDO DE RECREACION ES DEL 0.30% DEL SMM Y EQUIVALE A:")
            return cuota
    else:
        print("EL DATO QUE SE DIGITO NO ES UN NUMERO, PORFAVOR DIGITAR UN VALOR NUMERICO PARA ESTE DATO")
        return (naac or ima)

    

def fondo (afs,ima):
    afsa=afs.isdigit()
    imaa=ima.isdigit()
    if ((afsa) and (imaa)):
        afsa1=int(afs)
        imaa1=int(ima)
        if (afsa1==0):
            fondosol=(round(imaa1*0.04))
            print("EL ASOCIADO DECIDE APORTAR EL 4.0% DEL SMM AL FONDO DE SOLIDARIDAD Y EQUIVALE A: ")
            return fondosol
        elif afsa1==1:
            fondosol=(round(imaa1*0))
            print("EL ASOCIADO DECIDE NO APORTAR AL FONDO DE SOLIDARIDAD: ")
            return fondosol
    else:
        print("EL DATO QUE SE DIGITO NO ES UN NUMERO, PORFAVOR DIGITAR UN VALOR NUMERICO PARA ESTE DATO")
        return (afs or ima)

def pension (naac,ima):
    naaca=naac.isdigit()
    imaa=ima.isdigit()
    if ((naaca) and (imaa)):
        nuan=int(naac)
        imaa1=int(ima)
        imaa12=(imaa1/737717)
        if (nuan>=10) and (imaa12<=3):
            pension=(round(imaa1*0.15))
            print("EL APORTE A LA PENSION OBLIGATORIA DEL ASOCIADO ES DEL 15% DEL SMM Y EQUIVALE A: ")
            return pension
        elif (nuan>=10) and (imaa12>3):
            pension=(round(imaa1*0.17))
            print("EL APORTE A LA PENSION OBLIGATORIA DEL ASOCIADO ES DEL 17% DEL SMM Y EQUIVALE A: ")
            return pension
        elif (imaa12<=3):
            pension=(round(imaa1*0.08))
            print("EL APORTE A LA PENSION OBLIGATORIA DEL ASOCIADO ES DEL 8% DEL SMM Y EQUIVALE A: ")
            return pension
        elif (imaa12>3):
            pension=(round(imaa1*0.1))
            print("EL APORTE A LA PENSION OBLIGATORIA DEL ASOCIADO ES DEL 10% DEL SMM Y EQUIVALE A: ")
            return pension
    else:
        print("EL DATO QUE SE DIGITO NO ES UN NUMERO, PORFAVOR DIGITAR UN VALOR NUMERICO PARA ESTE DATO")
        return (naac or ima)
