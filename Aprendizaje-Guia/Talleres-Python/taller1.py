def aportecooperativa (INGRESOMENSUAL):
    pregunta=INGRESOMENSUAL.isdigit()
    if(pregunta):
        pregunta1=int(INGRESOMENSUAL)
        if (pregunta1<=2):
            gasto=(pregunta1*0.01)
            return gasto
        elif ((pregunta1>2) and (pregunta1<=6)):
            gasto=(pregunta1*0.02)
            return gasto
        elif (pregunta1>6):
            gasto=(pregunta1*0.03)
            return gasto
    else:
        print("no digitaste un numero")
        
