print("Encuesta Servicios de Bienestar")
print()
nper=int(input("Digite el numero de personas a encuestar: "))
x=0
doc=0
doc2=0
doc3=0
acu=0
while(nper != x):
    ocup=int(input("Digite (1) si es estudiante; (2) Docente o (3) Personal Adm.: "))
    serv=int(input("Digite (1) si el servicio que prefiere es Piscina; (2) Servicio Medico; (3) Cancha de Futbol o (4) Gimnasio: "))
    ed=int(input("Digite la edad de la persona"))
    if(ocup==2 and serv==2):
        doc=doc+1
    elif(ocup==2 and serv==3):
        doc2=doc2+1
    elif(ocup==1 and serv==4):
        doc3=doc3+1
    acu=acu+ed
    x=x+1
acu=acu/nper
print("medico= ",doc,"cancha= ",doc2,"gimnasio= ",doc3,"edad promedio= ",acu)
print("Ha finalizado la encuesta")
