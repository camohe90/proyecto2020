suma,total =0, 0
respuesta,par ,impar,numeros=[],[],[] ,[]

cantidad=int(input("digite la cantidad de número que desea almacenar: "))

for i in range(cantidad):
    print("ingrese el numoero",i+1," que desea almacenar", end=' ')
    numeros.append(int(input()))

print (numeros)
opcion=int(input("Elija una de las 8 opciones definidas: "))

if (opcion == 1):
    for i in numeros:
       suma = suma + i
    print("La suma de los elementos del arreglo es", suma)  
if (opcion == 2):
    for i in range(0,len(numeros),2):
           suma = suma + numeros[i]
    print("La suma de los elementos en las posiciones pares del arreglo es", suma)
if (opcion == 3):
    for i in range(1,len(numeros),2):
           suma = suma + numeros[i]
    print("La suma de los elementos en las posiciones impares del arreglo es", suma)

if (opcion == 4):
    tam=int(len(numeros)/2)
    for i in range(tam):
        respuesta.append(numeros[i]+numeros[-i-1])
    print("El arreglo resultante es ",respuesta)

if (opcion == 5):
    for i in numeros:
        if(i%2==0):
            par.append(i)
    print(par)

if (opcion == 6):
    for i in numeros:
        if(i%2!=0):
            impar.append(i)
    print(impar)

if (opcion == 7):
    for i in range(1,len(numeros)):
        suma=suma+numeros[i]
    print("el resultado es igual: ", numeros[0]-suma)

if(opcion == 8):
    for i in numeros:
        total=total+i
    print("El promedio es igual a ", (total/len(numeros)))






