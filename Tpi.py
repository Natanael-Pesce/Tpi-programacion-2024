Prueva = open("puntuacion.txt", "a")
Prueva.close

import random

import os

def menu():
    print("#"*45)
    print("Bienvenidos al menu")
    print("Ingrese el juego al que desea jugar")
    print("Se nombran a continuacion")
    print("#"*45)
    print("Juego nro 1: piedra papel tieras\n")

    print("Juego nro 2: Adivina el numero\n")

    print("Juego nro 3: Ahorcado\n")

    print("Juego nor 4: Mas o Menos\n")

    Juego = int(input("Si para salir de la aplicacion use el 0: \n "))

    if Juego == 0:
        print(" ")
    
    if Juego == 1:
        Piedra_papel_tijera()
    
    if Juego == 2:
        adivinaelNum()
    
    if Juego == 3:
        jugar_ahorcado()
    
    if Juego == 4:
        juego_mas_o_menos()

#Codigo de Natanael

def Piedra_papel_tijera():
    print("Bienvenido al piedra, papel y tijeras ʕᵔᴥᵔʔ")
    print("¿Cuantos jugadores tenemos hoy?")
    Players =int(input("1 o 2\n"))

    bot = 0
    bot1 = 0
    jugador1 = 0
    Jugador2 = 0

    if Players == 1:
        Nombre_jugador = str(input("Ingrese su nombre: "))
        print("Jugaras contra la maquina")
        print("Te toca")
        game = True
        while game == True:
            JugadorA = int(input("1 es piedra , 2 papel , 3 tijeras \n "))
            Bot = random.randrange(1,3)

            if JugadorA == 1 and Bot == 3:
                print("El jugador gana")
                bot1 = bot1 + 1

            if JugadorA == 1 and Bot == 2:
                print("El Bot gana")
                bot = bot + 1

            if JugadorA == Bot:
                print("Es un empate")

            if JugadorA == 2 and Bot == 3:
                print("El Bot gana")
                bot = bot + 1

            if JugadorA == 2 and Bot == 1:
                print("El jugador gana")
                bot1 = bot1 + 1
        
            if JugadorA == 3 and Bot == 2:
                print("El jugador gana")
                bot1 = bot1 + 1

            if JugadorA == 3 and Bot == 1:
                print("El Bot gana")
                bot = bot + 1
        
            print("Desea seguir jugando?")
            sigue=str(input("Enter para Y \nN=no \n "))

            if sigue == "n" or sigue == "N":
                game = False
            else:
                game = True

        print("Las victorias obtenidas por el jugador son: ")
        print(bot1)
        print("Las victorias obtenidas por la maquina son: ")
        print(bot)

        Prueva = open("puntuacion.txt", "a")
        Prueva.write(f"Jugador {Nombre_jugador} vs La maquina \n Puntaje = 35 vs 45 \n")
        Prueva.close

        print("Volvemos al menu")
        menu()

    if Players == 2:
        Nombre1 = str(input("Ingrese el nombre primer jugador: "))
        Nombre2 = str(input("Ingrese su nombre segundo jugador: "))
        print("Bien esto sera a turnos asi que va el jugador uno: ")
        game = True
        while game == True:
            JugadorA = int(input("turno del primer jugador: 1  piedra , 2 papel , 3 tijeras \n "))
            os.system('cls')
            JugadorB = int(input("turno del segundo jugador: 1  piedra , 2 papel , 3 tijeras \n "))
            os.system('cls')

            if JugadorA == 1 and JugadorB == 3:
                print("El jugador 1 gana")
                jugador1 = jugador1 + 1

            if JugadorA == 1 and JugadorB == 2:
                print("El jugador 2 gana")
                Jugador2 = Jugador2 + 1

            if JugadorA == JugadorB:
                print("Es un empate")

            if JugadorA == 2 and JugadorB == 3:
                print("El jugador 2 gana")
                Jugador2 = Jugador2 + 1

            if JugadorA == 2 and JugadorB == 1:
                print("El jugador 1 gana")
                jugador1 = jugador1 + 1
        
            if JugadorA == 3 and JugadorB == 2:
                print("El jugador 1 gana")
                jugador1 = jugador1 + 1

            if JugadorA == 3 and JugadorB == 1:
                print("El jugador 2 gana")
                Jugador2 = Jugador2 + 1
        
            print("Desea seguir jugando?")
            sigue=str(input("Enter para Y \nN=no \n "))

            if sigue == "n" or sigue == "N":
                game = False
            else:
                game = True
    
        print("Las victorias obtenidas por el jugador 1 son: ")
        print(jugador1)
        print("Las victorias obtenidas por la jugador 2 son: ")
        print(Jugador2)

        Prueva = open("puntuacion.txt", "a")
        Prueva.write(f"Jugador {Nombre1} vs Jugador {Nombre2} \n puntaje = 44 vs 30 \n")
        Prueva.close

        print("Volvemos al menu")
        menu()
        
#Codigo de Daniela

def juego_mas_o_menos():
    oportunidades = 15
    aciertos = 0
    objetivo_aciertos = 10

    print("¡Bienvenido a 'Más o Menos'!")
    print("Adivina si el siguiente número será Mayor o Menor")
    print(f"Necesitas {objetivo_aciertos} aciertos para ganar y tenes {oportunidades} oportunidades.\n")

    # Comienza el Juego, primer número.
    numero_actual = random.randint(1, 100)
    print(f"El número es: {numero_actual}\n ¡ADIVINA!")

    # Conteo de oportunidades y desarrollo del juego.
    while oportunidades > 0:

        eleccion = input(" 乁[⎚_⎚]ㄏ ¿El siguiente será Mayor o Menor? (Escribí '+' o '-'): ").strip().lower()

        # Siguiente número
        siguiente_numero = random.randint(1, 100)
        print(f"El siguiente número es: {siguiente_numero}")

        # ¿Adivinó o no?
        if (eleccion == "+" and siguiente_numero > numero_actual) or \
           (eleccion == "-" and siguiente_numero < numero_actual):
            aciertos += 1

            print("¡Buenisimo! Ganaste un punto. (👍 ͡❛ ͜ʖ ͡❛)👍")
        else:
            oportunidades -= 1
            print("Incorrecto. Perdiste una oportunidad. ( ˘︹˘ )")

        # En qué condiciones está el jugador.
        print(f"Aciertos: {aciertos}/{objetivo_aciertos}, Oportunidades que te quedan: {oportunidades}\n")

        # Condiciones para ganar o perder
        if aciertos >= objetivo_aciertos:
            print("¡Felicidades! El juego terminó, GANASTE!!.")
            print("(♥‿♥)")
            print("Volvemos al menu")
            menu()
            
        elif oportunidades == 0:
            print("Te quedaste sin oportunidades. ¡PERDISTE!")
            print("ಥ‿ಥ")
            print("Volvemos al menu")
            menu()

        # Actualizar el número actual
        numero_actual = siguiente_numero

#Codigo de Tiago

def obtener_palabra_aleatoria(): #funcion para poner las palabras
    palabras=["messi", "monarquia", "astrolgia", "crucero", "raton", "murcielago", "goku", "caballo", "volcan", "superman", "pollo", "vino", "salsa", "cielo", "hola", "ahorcado"]
    #cadena de palabras
    palabra_aleatoria=random.choice(palabras)
    return palabra_aleatoria

def mostrar_tablero(palabras_secreta, letras_adivinas):
    tablero=""
    for letra in palabras_secreta:
        if letra in letras_adivinas:
            tablero+=letra
        else:
            tablero+="_"
    print(tablero)

def jugar_ahorcado():
  palabras_secreta=obtener_palabra_aleatoria()
  letras_adivinadas=[]
  intentos_restantes=10

  while intentos_restantes>0:
    mostrar_tablero(palabras_secreta, letras_adivinadas)
    letra=input("introduce una letra: ").lower()

    if letra in letras_adivinadas:
       print("esa letra ya la has introducido,  prueba otra")
       continue
    
    if letra in palabras_secreta:
       letras_adivinadas.append(letra)
       if set(letras_adivinadas) ==set(palabras_secreta):
        print("flicidades, has hacertado la palabra la cual es") 
        print(palabras_secreta)
        print("Regresando al menu")
        menu()
    else:
      intentos_restantes-=1
      print(f"letra incorrecta, te quedan {intentos_restantes} intentos")
  if intentos_restantes==0:
      print(f"has perdido. la palabra secreta era {palabras_secreta}")
      print("Regresando al menu")
      menu()

#Codigo de Victor

def adivinaelNum():
    randomNum = random.randint(1, 20)
    intents = 0
    print('Intenta adivinar el número entre 1 y 20. Tienes 5 intentos.')

    while intents < 5:
        print(f'Intento {intents + 1}')
    
        try:
            guess = int(input('Ingresa tu número: '))
        except ValueError:
            print("Por favor, ingresa un número válido.")
            continue

        intents += 1

        if guess < randomNum:
            print('Tu intento es demasiado bajo.')
        elif guess > randomNum:
            print('Tu intento es demasiado alto.')
        else:
            print(f'¡Has acertado! El número era {randomNum}.')
            print("Volveremos al menu")
            menu()

    if guess != randomNum:
        print(f'Has perdido, el número era {randomNum}.')
        print("Volveremos al menu")
        menu()

menu()
