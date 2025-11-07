personas = [{"id": "1", "name": "Juan", "dni": "31.234.345", "nacionalidad": "Argentina"},
            {"id": "2", "name": "Alberto", "dni": "47.654.990", "nacionalidad": "Bolivia"},
            {"id": "3", "name": "Giuli", "dni": "40.887.094", "nacionalidad": "Bolivia"}]

def mostrar_nombres():
    print ("Lista de nombres")
    for persona in personas:
        print(persona["name"])

def nombres_y_nacionalidades():
    print ("Nombres y paises")
    for persona in personas:
            print(f"{persona['name']} y {persona['nacionalidad']}")

def dni_par_impar():
    print ("DNI par o impar")
    for persona in personas:
        dni_numero = int(persona["dni"].replace(".", ""))
        if persona["dni"] % 2 == 0:
            print (f"{persona}['name'] tiene dni par ({persona["dni"]})")
        else: 
            print (f"{persona}['name'] tiene dni impar ({persona["dni"]})")        

def finalizar_programa():
       print ("Programa finalizado")         
       return False

def menu():
    continuar = True
    while continuar:
        print( """MENU PRINCIPAL
              1- Mostrar nombres
              2- Mostrar nombres y nacionalidades
              3- Mostrar dni par o impar 
              0- Finalizar"""
              )
        opcion = input ("Elegir una opcion:")       
        if opcion == "1":
            mostrar_nombres()
        elif opcion == "2":
            nombres_y_nacionalidades()
        elif opcion == "3":
            dni_par_impar()
        elif opcion == "0":
            continuar = finalizar_programa()
        else:
            print("Opción no válida, intente nuevamente.")

menu()



    



