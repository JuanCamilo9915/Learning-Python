#TALLER 1 ALGORITMIA
#SAIRA ALEJANDRA CORREDOR SANABRIA
#CAMILA ESCOBAR MUÑOZ
#INGENIERIA INDUSTRIAL
#
#Una importante empresa del estado le ha solicitado desarrollar un sistema que permita automatizar el proceso de admisión de los diferentes ciudadanos que se postulan a las vacantes disponibles. El ciudadano suministrará un gran listado de datos y con base en las condiciones establecidas por la entidad, el sistema le notificará si cumple o no con el perfil. De igual manera el sistema entregará indicaciones para que el ciudadano tenga la oportunidad de ajustarse a las condiciones y en una próxima oportunidad aprobar todo el proceso.
#La entidad requiere conocer del ciudadano su nombre completo, cedula, año de nacimiento, edad, estrato social de su vivienda (1, 2, 3, 4 ,5 ,6), número de hijos, altura, número de personas dependientes.
#La entidad es muy estricta en su proceso de selección por lo que el postulado debe cumplir con lo siguiente:
#•  Participantes nacidos antes de 1990 no serán aptos.
#•  Participantes menores de 18 años no serán aptos.
#•  Participantes con una altura menor a 1.60 mts son descartados del proceso.
#•  Para esta convocatoria los participantes de estrato 4 y 5 serán descartados.
#•  Los participantes deben tener por lo menos 1 hijo y como mínimo 2 personas dependientes económicamente para ser aceptados.
 
#Nombre                   Cedula         Edad     Año de nacimiento    Altura    N. de hijos   N.de personas dependientes    Estrato social
#Paula Monroy             32632793        35           1982             1.62          3                     3                       3
#Mauricio Velez           62583754        42           1975             1.80          1                     4                       4
#Jose Gutierrez           52854321        47           1970             1.70          2                     3                       3
#Maria Jose Gaviria       85235302        32           1985             1.61          6                     6                       6
#Sara Lopez               166242581       22           1995             1.55          0                     0                       0
 
#optencion de informacion
nombre = str(input("Digite su nombre completo: ")) #Aqui nos pide digitar el nombre completo y lo declaramos como un objeto -str-(utilizado para letras)
cedula = int(input("Digite su cedula: ")) #Este nos pide la cedula la cual lo declaramos como un entero -int-
anodenacimiento = int(input("Digite año de nacimiento: "))
edad = int(input("Digite su edad: "))
estrato = int(input("Digite el estrato social de su vivienda: "))
numhijos = int(input("Digite el numero de hijos: "))
altura = float(input("Digite su altura: ")) #nos pide la altura la cual la valoramos en metros entonce el usuario digita la altura en numero no entero ejemplo 1.60m por eso lo declaramos float
numpdep = int(input("Digite el numero de personas dependientes: "))
 
#condicionales
 
if(anodenacimiento < 1990): #con este if comparamos  si el año de nacimiento es menor a 1990 nos va a generar un comentario el cual nos dice que no eres apto
     num = str("--Tu año de nacimiento es menor a 1990 por lo tanto no es apto")
     aprobo = str("Lo sentimos no a cumple con los requerimientos establecidos por la empresa")
if(anodenacimiento >= 1990): #de lo contrario nos generara un comentario vacio si no se procede a realizar este if nos saldra error
         num = str("")
  
      
if (edad<18):
    ed = str("--Tu edad es menor a 18 por lo tanto no es apto")
    aprobo = str("Lo sentimos no a cumple con los requerimientos establecidos por la empresa")
if (edad>=18):
     ed = str("")
  
     
if ((estrato==4) or (estrato==5)):
    estr = str("--Tu estrato estra entre 4 y 5 por lo tanto seran descartados")
    aprobo = str("Lo sentimos no a cumple con los requerimientos establecidos por la empresa")
if ((estrato==1) or (estrato==2) or (estrato==3) or (estrato==6)):
        estr = str("")
  
     
if (numhijos < 1):
    numh = str("--numero de hijos inferior a lo permitido")
    aprobo = str("Lo sentimos no  cumple con los requerimientos establecidos por la empresa")
if (numhijos >= 1):
        numh = str("")
  
     
if (numpdep<2):
    ndp = str("--Numero de personas dependientes menor a lo permitido")
    aprobo = str("Lo sentimos no  cumple con los requerimientos establecidos por la empresa")
if (numpdep >= 2):
        ndp = str("")
  
     
if (altura < 1.60):
    alt = str("--Tu altura es menor de 1.60m por lo tanto quedas descartado del proceso")
    aprobo = str("Lo sentimos no cumple con los requerimientos establecidos por la empresa")
if (altura >= 1.60):
        alt = str("")
  
 
if((anodenacimiento >= 1990) and (edad>=18) and ((estrato==1) or (estrato==2) or (estrato==3) or (estrato==6)) and (numhijos >= 1) and (numpdep >= 2) and (altura >= 1.60)):
    aprobo = str("Felicitaciones a sido aceptado")
    
 #resultado final   
print("Nombre: " , nombre )
print("Cedula: " , cedula)
print("Año de nacimiento: " , anodenacimiento , num)
print("Edad: " , edad , ed)
print("Estrato: " , estrato , estr)
print("Numero de Hijos: " , numhijos , numh)
print("Altura: " , altura , alt)
print("Numero de personas dependientes" , numpdep , ndp)
print(aprobo)
 
    
 
 
# Evaluación
# Analisis (2.0): 1.7 Se debe mejorar el pseudocodigo. 
# Escenario 1 (1.0):1.0
# Escenario 2 (1.0):1.0
# Escenario 3 (1.0):1.0
# Nota:4.7
# Obseraciones:
