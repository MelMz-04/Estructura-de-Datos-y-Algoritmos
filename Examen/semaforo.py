'''                 Semáforo COVID   
                    9 - agosto -2021
    Hecho por Matias Zavala, Melissa Maruuati
    Windows 10                                '''
import os
os.system("cls")
print("\n\t\tBienvenido a mi semáforo COVID\n")#Mensaje de bienvenida
indicadores=[]#arreglo para guardar los indicares
nombres=[]#arreglo para guardar los nombres
edad=[]#arreglo para guardar la edad
ac=0#iniciador para acumulador
inc=0
a=open("bd.csv",'r')#abre el archivo en modo leer
contenido=a.readlines()#lee cada columna de la base de datos
a.close()#cierra base de 
#Ciclo para separar cada arreglo de la base de datos (nombre, edad , indicador)
for i in contenido:    
    pc=i.find(",")#Busca la primer coma
    ps=i.find(",",pc+1)#Busca la segunda coma
    indicadores.append(i[ps+1:-1])#Guarda en el arreglo indicadores 
    nombres.append(i[:pc])#Guarda en el arreglo nombres 
    edad.append(i[pc+1:ps])#Guarda en el arreglo edad
ed=0#inicializa edad
for i in indicadores:#Ciclo para revisar en el arreglo indicadores 
    if float(i)<0.8:#condición para indicador menos a   
        del edad[ed:ed+1] 
    else:#en caso de mayor a 0.8       
        inc=inc+1#acumula el número de personas con COVID
        ed=ed+1#suma la posición para el siguiente elemento
for i in edad:#Ciclo para calcular suma de edad
    ac=int(i)+ac#Va sumando cada elemento que se encuentre en el arreglo edad
l=len(edad)#longitud del arreglo edad        
p=ac/l#Calcula promedio a partir de la suma de edades y longitud del earreglo
if inc==0:#Condicionales para imprimer semáforo acorde a personas contagiadas 
    print("El semáforo esta em verde")
elif 1<=inc<=30:
    print("El semáforo esta en amarillo")
elif 31<=inc<=70:
    print("El semáforo esta en naranja")
else:
    print("Semáforo rojo, quedense en casa")
print("El promedio de edad es: "+str(p))#Muestra el promedio de edad de personas con COVID