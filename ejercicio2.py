import random 
def añadir_mision (misiones):
    tipo = input("ingrese que tipo de mision: ")
    planeta = input("ingrese el planeta destino: ")
    general = input("ingrese el general que ha solicitado la mision: ")

    mision_nueva =[tipo, planeta, general]
    misiones.append(mision_nueva)

def asignar_recursos(misiones):
    scout_troopers = 0
    speeder_bike = 0
    stormtoopers = 0
    vehiculos = 0 
    for mision in misiones:
        if mision[2] == "Palpatine" or mision[2] == "Darth vader":
            scout_troopers += 15
            speeder_bike += 2
            stormtoopers += 50
            vehiculos += 7
        else:
            if mision[0] == "exporacion":
                scout_troopers += 15
                speeder_bike += 2
            elif mision[0] == "contencion":
                stormtoopers += 30
                vehiculos += random.choice(["AT-AT", "AT-RT", "At-TE", "AT-DP", "AT-SP"])
            elif mision[0] == "ataque":
                stormtoopers += 50
                vehiculos += random.choice(["AT-AT", "AT-RT", "At-TE", "AT-DP", "AT-ST", "AT-M6", "At-MP", "AT-DP"])
    print("Recursos asignados: ")
    print("Scout Troopers: ", scout_troopers)
    print("Speeder Bike: ", speeder_bike)
    print("Stormtroopers: ", stormtoopers)
    print("Vehiculos; ", vehiculos)

def mostrar_misiones(misiones):
    print("MIsiones: ")
    for mision in misiones:
        print("Tipo: ", mision[0])
        print("Planeta destino: ", mision[1])
        print("General que la solicita: ", mision[2])
        print(" ")

def mostrar_menu():
    print("1. Agregar mision")
    print("2. Asignar recursos")
    print("3. Mostrar misiones")
    print("4. Salir")

def ejecutar():
    misiones = []
    opcion = 0
    while opcion != 4:
        mostrar_menu()
        opcion = int(input("Ingrese una opcion: "))
        if opcion == 1:
            añadir_mision(misiones)
        elif opcion ==2 :
            asignar_recursos(misiones)
        elif opcion == 3:
            mostrar_misiones(misiones)