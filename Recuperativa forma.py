import random
multa_minima = 1500
multa_maxima = 3500

def multa_r():
    
    valor_multa = random.randint(multa_minima, multa_maxima)
    print("Valor de la multa:", valor_multa)

def validar_patente(numero_patente):
    if len (numero_patente) < 6:
        return False
    
    for caracter in numero_patente:
        if not caracter.isalnum() and caracter != '*':
            return False
        
    return True

def validar_marca(nombre_marca):
    if len (nombre_marca) < 15:
        return False
    
    for caracter in nombre_marca:
        if not caracter.isalnum():
            return False

autos = []

def grabar_auto():

    while True:
        
        numero_patente = input("Ingrese el número de patente del vehiculo: ")
        if validar_patente(numero_patente):
            break
        else:
            print("El número de patente ingresado es inválido.")

    nombre_dueño = input("Ingrese el nombre del dueño del vehiculo: ")
             
    nombre_auto = input("Ingrese el tipo de vehiculo: ")
    while len (nombre_auto) < 6:
        print("El nombre del vehiculo debe tener al menos 6 caracteres.")

        nombre_auto = input("Ingrese el tipo de vehiculo: ")    

    nombre_marca = input("Ingrese la marca del vehiculo: ")
    while len (nombre_marca) < 2 < 15:
           print("El nombre de la marca debe tener al menos 15 caracteres.")

           nombre_marca = input("Ingrese la marca del vehiculo: ")

    precio = int(input("Ingrese el precio del vehiculo: "))
    while precio < 5000000:
        print('El precio debe ser mayor a 5.000.000')
        precio = int(input("Ingrese el precio del vehiculo: "))

    valor_multa = multa_r()
    print(valor_multa)

    auto = {	

        "nombre_dueño": nombre_dueño,
        "numero_patente": numero_patente,
        "nombre_auto": nombre_auto,
        "nombre_marca": nombre_marca,
        "precio": precio,
        "multa": valor_multa
    }

    autos.append(auto)
    print("Vehiculo guardado correctamente")

def buscar_auto():

    numero_patente = input("Ingrese el número de patente del auto que desea buscar: ")
    encontrado = False
    for auto in autos:
        if auto['numero_patente']== numero_patente:
            encontrado = True
        if auto['precio'] >= 5000000:
            print('Mostrar informacio del vehiculo ')
            print('Nombre del dueño: ', auto['nombre_dueño'])
            print('Numero de patente: ',auto['numero_patente'])
            print('Marca del vehiculo', auto['nombre_marca'])
            print('Tipo de vehiculo: ',auto['nombre_auto'])
            print('Precio del vehiculo: ','$',auto['precio'])
        
    if not encontrado:
        print('Vehiculo no encontrado')
 

def imprimir_certificado_vigente():
    print("------ Reporte de vehiculos -----")
    for auto in autos:
        print('Nombre del dueño', auto['nombre_dueño'])
        print('Numero de patente: ',auto['numero_patente'])
        print('Marca del vehiculo: ',auto['nombre_marca'])
        print('Tipo de vehiculo: ',auto['nombre_auto'])
        print('Precio del vehiculo: ','$',auto['precio'])
        print('---------------------------------')

def imprimir_multa_vehiculo():
    print("------ Reporte de vehiculos -----")
    for auto in autos:
        print('Nombre del dueño', auto['nombre_dueño'])
        print('Numero de patente: ',auto['numero_patente'])
        print('Marca del vehiculo: ',auto['nombre_marca'])
        print('Tipo de vehiculo: ',auto['nombre_auto'])
        print('Precio del vehiculo: ','$',auto['precio'])
        print('Multa de vehiculo: ','$',auto['multa'])
        print('---------------------------------')

#Intente que al imprimir la multa se muestre pero no se muestra la multa random pero los demas datos si se muestran

while True:
    print("----- Menú de Auto Seguro -----")
    print("1. Grabar auto")
    print("2. Buscar auto")
    print("3. Imprimir reporte vigente")
    print("4. Imprimir Multa de vehiculo")
    print("5. Salir")
    opcion = int(input("Ingrese una opcion: "))

    if opcion == 1:
        grabar_auto()
    elif opcion ==2:
        buscar_auto()
    elif opcion == 3:
        imprimir_certificado_vigente()    
    elif opcion ==4:
        imprimir_multa_vehiculo()
    elif opcion ==5:
        print("Muchas Gracias por usar el programa, Hasta la proxima")
        print("Manuel Espinoza")
        print("Python v2023.10.1")
        break
    else:
        print("Opción no valida, Ingrese otra opcion")

