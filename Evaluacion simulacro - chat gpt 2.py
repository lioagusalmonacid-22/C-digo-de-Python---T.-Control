estudiantes = [{"id": "1", "nombre": "Julian", "edad": "20", "nota_final": "6", "carrera": "Arquitectura"},
                {"id": "2", "nombre": "Santiago", "edad": "18", "nota_final": "8", "carrera": "Marketing digital"},
                {"id": "3", "nombre": "Martina", "edad": "32", "nota_final": "4", "carrera": "Filosofia"},
                {"id": "4", "nombre": "Victoria", "edad": "26", "nota_final": "9", "carrera": "Quimica"}]

def mostrar_nombres():
    print("Los estudiantes son: ")
    for estudiante in estudiantes:
        print(estudiante["nombre"])

def nombre_y_carrera():
    print("Estudiantes y la carrera que estan cursando: ")
    for estudiante in estudiantes:
        print(f"{estudiante['nombre']} cursa la carrera de {estudiante['carrera']}")

def aprobado_desaprobado():
    print("Lista de calificaciones finales: ")     
    for estudiante in estudiantes:
        n = int(estudiante["nota_final"])
        if n < 6:
         print(f"{estudiante['nombre']} tiene de nota final {estudiante['nota_final']}, por lo tanto esta DESAPROBADO")  
        else: 
         print(f"{estudiante['nombre']} tiene de nota final {estudiante['nota_final']}, por lo tanto esta APROBADO")

def promedio_notas():
 suma_de_notas = sum(int(estudiante["nota_final"]) for estudiante in estudiantes)
 promedio_de_notas = suma_de_notas / len(estudiantes)
 print(f"El promedio de notas de los estudiantes es: {promedio_de_notas}")

def finalizar_programa():
    print("Programa finalizado")
    return False

def menu():
    continuar = True
    while continuar:
            print(""" MENU DE PRINCIPAL
                  1- Mostar el nombre de los estudiantes
                  2- Mostar nombre y carrera que cursan
                  3- Calificaciones finales 
                  4- Nota promedio total
                  5- Finalizar programa """)     
               
            opcion = input("Elige una opcion")
            if opcion == "1":
                mostrar_nombres()
            elif opcion == "2":
                nombre_y_carrera()
            elif opcion == "3":
                aprobado_desaprobado()
            elif opcion == "4":
                promedio_notas()
            elif opcion == "5":
                finalizar_programa()
                break
            else: print("Opcion no valida, intente nuevamente")

menu()            