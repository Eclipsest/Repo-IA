limite = "Solo respondo dudas sobre los temas del curso. Para notas, fechas u otros temas, consulta a tu TL."

print("+------------------------------------------+")
print("|  ASISTENTE DE REPASO - PYTHON RIWI       |")
print("|                                          |")
print("|  1) Variables                            |")
print("|  2) Condicionales (if / else)            |")
print("|  3) input e int                          |")
print("|  4) Otra cosa (notas, fechas...)         |")
print("|                                          |")
print("|  LIMITE: solo respondo dudas del curso.  |")
print("|  Puedo equivocarme: verifica con tu TL.  |")
print("+------------------------------------------+")

tema = input("[R] Elige una opción (1, 2, 3 o 4): ")

nombre = ""
if tema == "1":
    nombre = "Variables"
    explicacion = "Una variable guarda un valor con un nombre. Ejemplo: edad = 20"
    ejercicio = "Crea una variable con tu nombre y muéstrala con print."
elif tema == "2":
    nombre = "Condicionales"
    explicacion = "if decide qué hacer según una comparación. Ejemplo: if a <= b: print(a, b)"
    ejercicio = "Pide un número y muestra si es mayor o menor que 10."
elif tema == "3":
    nombre = "input e int"
    explicacion = "input lee lo que escribes; int lo convierte en número. Ejemplo: n = int(input())"
    ejercicio = "Pide dos números y muestra su suma."

if nombre == "":
    print("[R]", limite)
else:
    duda = input("[R] Escribe tu duda: ")
    if duda == "":
        print("[R] Escribe una pregunta para poder ayudarte.")
    else:
        print("[M] Tema:", nombre)
        print("[M]", explicacion)

        print("[M] Ejercicio:", ejercicio)

        entendio = input("¿Entendiste? (s/n): ")
        if entendio == "s":
            print("¡Bien! Resuelve el ejercicio y compártelo con tu clan.")
        else:
            print("[H] Tu consulta se envió al TL para que la revise.")
            print("[H] Tema:", nombre, "- Duda:", duda)
