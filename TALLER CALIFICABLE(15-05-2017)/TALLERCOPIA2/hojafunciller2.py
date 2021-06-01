def validacioncategorias(cate):
    cater=cate.isdigit()
    while (cater==False):
        print("NO HAS DIGITADO UN NUMERO PARA ESTE DATO:" , cate)
        cate=input("DIGITE (1) SI LA CATEGORIA ES GRANO, (2) SI SON LÁCTEOS, (3) SI ES DE ASEO, O (4) SI ES DE CARNE:")
        cater=cate.isdigit()
    catr=int(cate)
    return catr

def categoproduc(uni):
    uni1=0;
    uni2=0;
    uni3=0;
    uni4=0;
    uin=uni.isdigit()
    while (uin==False):
        print("NO HAS DIGITADO UN NUMERO PARA ESTE DATO:" , unin1 and unin2 and unin3 and unin4)
        uni=input("DIGITE LA CANTIDAD DE UNIDADES VENDIDAS DEL PRODUCTO EN EL DIA:")
        uin=uni.isdigit()
    unda=int(uni)
    return unda

def costoproducto(valr):
    uin=valr.isdigit()
    while (valr==False):
        print("NO HAS DIGITADO UN NUMERO PARA ESTE DATO:" , valr1 or valr2 or valr3 or valr4)
        valr=input("DIGITE EL VALOR DEL PRODUCTO:")
        uin=valr.isdigit()
    costopro=int(valr)
    return costopro

