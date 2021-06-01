def validacion(nes):
    ne=nes.isdigit()
    while (ne==False):
        print("EL DATO QUE SE DIGITO NO ES UN NUMERO, PORFAVOR DIGITAR UN VALOR NUMERICO PARA ESTE DATO" , nes)
        nes=input("DIGITE EL NUMERO DE ESTUDIANTES QUE TIENE SU GRUPO:")
        ne=nes.isdigit()
    ne1=int(nes)
    return ne1

def valornota1(nes):
    ne1=nes
    while (ne1<=nes):
        
        while (ne1<=nes):
            prcil1=input("DIGITE LA NOTA DEL PRIMER PARCIAL DEL ESTUDIANTE:")
            nota1=prcil1.isdigit()



            nota12=int(prcil1)
            print (nota12)
    return nota12






    #
    #while(ne1<=nes):
    #    prcil1=input("DIGITE LA NOTA DEL PRIMER PARCIAL DEL ESTUDIANTE:")
    #    nota1=prcil1.isdigit()
    #    if (nota1==False):
    #        print("EL DATO QUE SE DIGITO NO ES UN NUMERO, PORFAVOR DIGITAR UN VALOR NUMERICO PARA ESTE DATO" , nota1)
    #        prcil1=input("DIGITE LA NOTA DEL PRIMER PARCIAL DEL ESTUDIANTE:")
    #        nota1=prcil1.isdigit()
     #   nta12=int(prcil1)
    #   a=nta12
    #print(a)
        
        
       













            
