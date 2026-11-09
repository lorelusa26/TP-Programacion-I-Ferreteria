# Trabajo Practico Integrador - Programacion I
# Sistema de Control de Inventario para una ferreteria
# Los datos se conservan solo mientras el programa esta abierto.


def cargar_herramientas(inventario):
    print("\n--- CARGA DE HERRAMIENTAS ---")

    # Se vuelve a pedir la cantidad hasta recibir un entero positivo.
    while True:
        
        try:
            cantidad = int(input("¿Cuántas herramientas desea cargar?: "))
            if cantidad <= 0:
                raise ValueError("La cantidad debe ser mayor que cero.")
            break
        except ValueError as error:
            print(f"Error: {error}")

    for numero in range(1, cantidad + 1):
        # El nombre se valida y se vuelve a pedir si es necesario.
        while True:
            try:
                nombre = input(f"Nombre de la herramienta {numero}: ").strip()
                if nombre == "":
                    raise ValueError("El nombre de la herramienta no puede estar vacío.")

                for producto in inventario:
                    if producto["herramienta"].lower() == nombre.lower():
                        raise ValueError("Esa herramienta ya está registrada.")
                break
            except ValueError as error:
                print(f"Error: {error}")

        # Si el stock es inválido, se conserva el nombre válido.
        while True:
            try:
                stock = int(input("Stock inicial: "))
                if stock < 0:
                    raise ValueError("El stock inicial no puede ser negativo.")
                break
            except ValueError as error:
                print(f"Error: {error}")

        # Solo se agrega cuando AMBOS datos son válidos.
        inventario.append({"herramienta": nombre, "cantidad": stock})
        print("Herramienta registrada correctamente.")


def mostrar_inventario(inventario):
    print("\n--- INVENTARIO ACTUAL ---")
    if len(inventario) == 0:
        print("Todavía no hay herramientas cargadas.")
        return

    for producto in inventario:
        print(f"{producto['herramienta']} | Stock: {producto['cantidad']}")


def consultar_stock(inventario):
    print("\n--- CONSULTA DE STOCK ---")
    if len(inventario) == 0:
        print("Todavía no hay herramientas cargadas.")
        return

    nombre = input("Nombre de la herramienta: ").strip()
    if nombre == "":
        raise ValueError("El nombre de la herramienta no puede estar vacío.")

    for producto in inventario:
        if producto["herramienta"].lower() == nombre.lower():
            print(f"Stock disponible de {producto['herramienta']}: {producto['cantidad']}")
            return

    print("La herramienta no se encuentra en el catálogo.")


def reporte_agotados(inventario):
    print("\n--- REPORTE DE AGOTADOS ---")
    if len(inventario) == 0:
        print("Todavía no hay herramientas cargadas.")
        return

    cantidad_agotados = 0
    for producto in inventario:
        if producto["cantidad"] == 0:
            print(f"Herramienta agotada: {producto['herramienta']}")
            cantidad_agotados += 1

    if cantidad_agotados == 0:
        print("No hay herramientas agotadas.")


def alta_producto(inventario):
    print("\n--- ALTA DE NUEVO PRODUCTO ---")
    nombre = input("Nombre de la nueva herramienta: ").strip()
    if nombre == "":
        raise ValueError("El nombre de la herramienta no puede estar vacío.")

    for producto in inventario:
        if producto["herramienta"].lower() == nombre.lower():
            raise ValueError("Esa herramienta ya está registrada.")

    stock = int(input("Stock inicial: "))
    if stock < 0:
        raise ValueError("El stock inicial no puede ser negativo.")

    inventario.append({"herramienta": nombre, "cantidad": stock})
    print("Nuevo producto registrado correctamente.")


def actualizar_stock(inventario):
    print("\n--- ACTUALIZACIÓN DE STOCK ---")
    if len(inventario) == 0:
        print("Todavía no hay herramientas cargadas.")
        return

    nombre = input("Nombre de la herramienta: ").strip()
    if nombre == "":
        raise ValueError("El nombre de la herramienta no puede estar vacío.")

    producto_encontrado = None
    for producto in inventario:
        if producto["herramienta"].lower() == nombre.lower():
            producto_encontrado = producto
            break

    if producto_encontrado is None:
        print("La herramienta no se encuentra en el catálogo.")
        return

    print("1. Venta (restar unidades)")
    print("2. Ingreso (sumar unidades)")
    movimiento = input("Tipo de movimiento (1 o 2): ").strip()
    if movimiento != "1" and movimiento != "2":
        print("Movimiento inválido: debe elegir 1 (venta) o 2 (ingreso).")
        return

    unidades = int(input("Cantidad de unidades: "))
    if unidades <= 0:
        raise ValueError("Las unidades deben ser mayores que cero.")

    if movimiento == "1":
        if unidades > producto_encontrado["cantidad"]:
            raise ValueError("No hay stock suficiente para realizar la venta.")
        producto_encontrado["cantidad"] -= unidades
        print("Venta registrada correctamente.")
    else:
        producto_encontrado["cantidad"] += unidades
        print("Ingreso de mercadería registrado correctamente.")

    print(f"Nuevo stock de {producto_encontrado['herramienta']}: {producto_encontrado['cantidad']}")


def main():
    # Única colección de datos. No se emplean variables globales.
    inventario = []

    while True:
        print("\n===== SISTEMA DE CONTROL DE INVENTARIO =====")
        print("1. Cargar herramientas")
        print("2. Mostrar inventario")
        print("3. Consultar stock")
        print("4. Reporte de agotados")
        print("5. Alta de nuevo producto")
        print("6. Actualizar stock (venta / ingreso)")
        print("7. Salir")

        try:
            opcion = int(input("Seleccione una opción: "))
            if opcion < 1 or opcion > 7:
                raise ValueError("Debe elegir una opción entre 1 y 7.")

            if opcion == 1:
                cargar_herramientas(inventario)
            elif opcion == 2:
                mostrar_inventario(inventario)
            elif opcion == 3:
                consultar_stock(inventario)
            elif opcion == 4:
                reporte_agotados(inventario)
            elif opcion == 5:
                alta_producto(inventario)
            elif opcion == 6:
                actualizar_stock(inventario)
            elif opcion == 7:
                print("Gracias por utilizar el sistema. ¡Hasta pronto!")
                break

        except ValueError as error:
            print(f"Error: {error}")


main()
