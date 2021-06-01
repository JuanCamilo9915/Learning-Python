Nombre=input("Digite el nombre completo")
Cedula=input("Digite numero de cedula")
AñoNac=int(input("Digite el año de nacimiento"))
Edad=int(input("Digite la Edad"))
Alt=int(input("Digite la Altura"))
Est=int(input("Digite el Estrato Social"))
Hijos=int(input("Digite el numero de hijos"))
Pdep=int(input("Digite el numero de personas dependientes"))
 
if(AñoNac>=1990):
    print("cumple")
else:
    print("no cumple")
 
if(Edad>=18):
    print("cumple")
else:
    print("no cumple")
 
if(Alt>=160):
    print("cumple")
else:
    print("no cumple")
 
if(Est<=3):
    print("cumple")
else:
    print("no cumple")
 
if(Hijos>=1):
    print("cumple")
else:
    print("no cumple")
 
if(Pdep>=2):
    print("cumple")
else:
    print("no cumple")
 
if(AñoNac>=1990):
    if(Edad>=18):
        if(Alt>=160):
            if(Est<=3):
                if(Hijos>=1):
                    if(Pdep>=2):
                        print("aceptado")
else:
    print("no aceptado")
         
