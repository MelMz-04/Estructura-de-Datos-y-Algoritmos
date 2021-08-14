'''                 Semáforo COVID   
                    13 - agosto -2021
    Hecho por Matias Zavala, Melissa Maruuati
    Windows 10. Python 3.9.6                                '''
import os
os.system("cls")#limpia la pantalla
print("\n\t\tBienvenido a mi semáforo COVID")#Mensaje de bienvenida
indicadores=[]#arreglo para guardar los indicares
nombres=[]#arreglo para guardar los nombres
edad=[]#arreglo para guardar la edad
ac=0#iniciador para acumulador
inc=0#iniciador de incremento
op='0'#iniciador de opción
a=open("bd.csv",'r')#abre el archivo en modo leer
contenido=a.readlines()#lee cada columna de la base de datos
a.close()#cierra base de 
#Ciclo para separar cada arreglo de la base de datos (nombre, edad , indicador)
for i in contenido:#Ciclo para separar el contenido en distintos arreglos    
    pc=i.find(",")#Busca la primer coma
    ps=i.find(",",pc+1)#Busca la segunda coma
    indicadores.append(i[ps+1:-1])#Guarda en el arreglo indicadores 
    nombres.append(i[:pc])#Guarda en el arreglo nombres 
    edad.append(i[pc+1:ps])#Guarda en el arreglo edad
n=len(indicadores)#longitud del arreglo indicadores
ed=0#inicializa edad
nom=0#inicializa nombres
for i in indicadores:#Ciclo para revisar en el arreglo indicadores 
    if float(i)<0.8:#condición para indicador menos a   
        del edad[ed:ed+1] 
        del nombres[nom:nom+1]
    else:#en caso de mayor a 0.8       
        inc=inc+1#acumula el número de personas con COVID
        ed=ed+1#suma la posición para el siguiente elemento
        nom=nom+1
for i in edad:#Ciclo para calcular suma de edad
    ac=int(i)+ac#Va sumando cada elemento que se encuentre en el arreglo edad
    l=len(edad)#longitud del arreglo edad        
    p=ac/l#Calcula promedio a partir de la suma de edades y longitud del arreglo
while op!='3':#Ciclo para mostrar menú hasta salir
    print("\n1) Color de semáforo\n2) Personas infectadas y promedio de edad infectados\n3) Salir ")#Menú de opciones
    op=input("\tElige la opción deseada: ")#Guarda el número de la opción
    if op=='1':
        #Condicionales para imprimer semáforo acorde a personas contagiadas 
        if inc==0:#
        #al no haber contagios
            print("\nEl semáforo esta em verde, actividad normal con precaución")
        elif 1<=inc<=30:#de un contagio hasta 30
            print("\nEl semáforo esta en amarillo, sal con precaución")
        elif 31<=inc<=70:#31 contagios a 70
            print("\nEl semáforo esta en naranja, quedate en casa de ser posible")
        else:#71 contagios o más 
            print("\nEl semáforo esta en rojo, no salgas a menos que sea necesario")
    elif op=='2':
        acu=0#Iniciador para posición en edad
        print("\nLas personas infectadas son:\nNombre  ,  Edad")#Muestra el mensaje inicial y como se ordenan las columnas
        for i in nombres:
            reg=i+', '+str(edad[acu:acu+1])#Concatena cada nombre con su respectiva edad
            print(reg)#Imprime el arreglo de reg
            acu=acu+1#Va aumentando la posición
        print("\nEl promedio de personas infectadas es: "+str(p))#Muestra el promedio de edad de personas con COVID
    elif op=='3':#Salir del programa
        print("\n\t\tGracias por usar mi programa")#Mensaje de despedida
    else:
        print("\nOpción inválida")#Para opciones que no sean 1, 2 o 3