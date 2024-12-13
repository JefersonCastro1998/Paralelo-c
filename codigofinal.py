# Función para obtener la opción de un jugador
def obtener_opcion_jugador(jugador):
    opcion = input(f"{jugador}, elige piedra, papel o tijera: ").lower()
    while opcion not in ["piedra", "papel", "tijera"]:
        print("Opción inválida. Intenta nuevamente.")
        opcion = input(f"{jugador}, elige piedra, papel o tijera: ").lower()
    return opcion

# Función para determinar el ganador
def determinar_ganador(opcion_j1, opcion_j2):
    if opcion_j1 == opcion_j2:
        return "Empate"
    elif (opcion_j1 == "piedra" and opcion_j2 == "tijera") or \
         (opcion_j1 == "papel" and opcion_j2 == "piedra") or \
         (opcion_j1 == "tijera" and opcion_j2 == "papel"):
        return "¡Jugador 1 gana!"
    else:
        return "¡Jugador 2 gana!"

# Función principal del juego
def jugar():
    jugando = True
    while jugando:
        # Obtener las opciones de los jugadores
        jugador1 = "Jugador 1"
        jugador2 = "Jugador 2"

        opcion_j1 = obtener_opcion_jugador(jugador1)
        opcion_j2 = obtener_opcion_jugador(jugador2)

        # Mostrar las opciones elegidas
        print(f"{jugador1} eligió: {opcion_j1}")
        print(f"{jugador2} eligió: {opcion_j2}")

        # Determinar y mostrar el resultado
        resultado = determinar_ganador(opcion_j1, opcion_j2)
        print(resultado)

        # Preguntar si quieren jugar otra vez
        jugar_otra_vez = input("¿Quieren jugar otra vez? (si/no): ").lower()
        if jugar_otra_vez != "si":
            jugando = False

# Iniciar el juego
jugar()


'''def describir_persona(nombre = 'amigo' , edad = 0):
    print(f'{nombre} tiene {edad} anos.')

describir_persona( "Ana", 25)'''

'''# crea_una_funcion_saludar
def saludar (nombre = 'amigo'):
    print(f'hola,{nombre}')  

saludar('Jeffo')'''

