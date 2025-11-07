productos = [{"id": "1", "nombre": "papel higienico", "precio": "500", "categoria": "higiene"},
             {"id": "2", "nombre": "pan", "precio": "250", "categoria": "alimento"},
             {"id": "3", "nombre": "lavandina", "precio": "730", "categoria": "higiene"},
             {"id": "4", "nombre": "alfajor", "precio": "100", "categoria": "alimento"}]

def mostrar_nombre():
    print("LOS PRODUCTOS DISPONIBLES SON: ")
    for producto in productos:
        print(producto["nombre"])

def nombres_y_categorias():
    print("PRODUCTOS Y SUS CATEGORIAS: ")
    for producto in productos:
        print(f"El {producto['nombre']} pertenece a la categoria de {producto['categoria']}")     

def par_impar():
    print("PRECIO DEL PRODUCTO PAR o IMPAR: ")
    for producto in productos:
        n = int(producto["precio"])
        if n % 2 == 0:
            print(f"El {producto['nombre']}, de la categoria {producto['categoria']} tiene precio PAR")
        else:
            print(f"El {producto['nombre']}, de la categoria {producto['categoria']} tiene precio IMPAR")    

def valor_promedio():
    print("VALOR PROMEDIO DE TODOS LOS PRODUCTOS: ")
    suma_de_precios = sum(int(producto["precio"]) for producto in productos)
    promedio_de_precios = suma_de_precios / len(productos)
    print("El precio promedios del total de los productos es", [promedio_de_precios])

def finalizar_programa():
    print("PROGRAMA FINALIZADO")
    return False

def menu():
    continuar = True
    while continuar:
            print(""" MENU DE PRINCIPAL
                  1- Mostar el nombre de los productos
                  2- Mostar nombre y categorias
                  3- Precio par o impar
                  4- Valor promedio total
                  5- Finalizar programa """)     
               
            opcion = input("Elige una opcion")
            if opcion == "1":
                mostrar_nombre()
            elif opcion == "2":
                nombres_y_categorias()
            elif opcion == "3":
                par_impar()
            elif opcion == "4":
                valor_promedio()
            elif opcion == "5":
                finalizar_programa()
                break
            else: print("Opcion no valida, intente nuevamente")

menu()            

