jugadores = []
poemas = []
cantidad = 0

def pedir_jugadores():
    global cantidad, jugadores
    cantidad = int(input("¿Cuántas personas van a jugar? (mínimo 2): "))
    jugadores = []

    for i in range(cantidad):
        nombre = input(f"Nombre del jugador {i+1}: ")
        jugadores.append(nombre)


def escribir_poemas():
    global poemas
    poemas = []
    print("\n--- Empieza el juego ---")
    for nombre in jugadores:
        print(f"\nTurno de {nombre}:")
        poema = input("Escribe tu poema: ")
        poemas.append(poema)


def mostrar_poemas():
    print("\n=== Poemas escritos ===")
    for i in range(cantidad):
        print(f"\nPoema {i+1} - {jugadores[i]}:")
        print(poemas[i])


def elegir_ganador():
    ganador = int(input("\n¿Quién gana? (escribe el número del poema): "))
    ganador -= 1
    print(f"\n¡Felicidades {jugadores[ganador]}! Tu poema fue el mejor.")


def jugar_poemas():
    pedir_jugadores()
    escribir_poemas()
    mostrar_poemas()
    elegir_ganador()


def main():
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Jugar al juego de poemas")
        print("2. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            jugar_poemas()
        elif opcion == "2":
            print("Saliendo... Adiós.")
            break
        else:
            print("Opción inválida.")


main()
