#EJEMPLOS PARA VALIDAR ENTRADAS
gl=input("digite su nivel de glucosa: ")
glucos=gl.isdigit()
print(glucos)

if(glucos):
    gluci=int(gl)
    if(gluci<70):
        print("su nivel de glucosa es bajo")
    elif((gluci>=70) and (gluci<140)):
        print("su nivel de glucosa es normal")
    elif((gluci>=140) and (gluci<450)):
        print("su nivel de glucosa es alto")
    elif(gluci>450):
        print("su nivel de glucosa sobrepaso los niveles altos, porfavor dirigirse urgente al doctor porque esta propenso a un derrame cerebral")
else:
    print("no has digitado correctamente el nivel de glucosa, porfavor ingrese las caracteres de forma numerica")
