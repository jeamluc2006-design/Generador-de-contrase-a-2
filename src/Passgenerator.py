import random
import string


# ---------------------------------
# Validar longitud
# ---------------------------------
def obtener_longitud():

    while True:

        dato = input("Ingrese la longitud de la contraseña (4 - 128): ")

        if not dato.isdigit():
            print("Error: solo puede ingresar números.\n")
            continue

        longitud = int(dato)

        if longitud < 4:
            print("La longitud mínima es de 4 caracteres.\n")

        elif longitud > 128:
            print("La longitud máxima es de 128 caracteres.\n")

        else:
            return longitud


# ---------------------------------
# Validar opciones del menú
# ---------------------------------
def obtener_nivel():

    while True:

        print("\nSeleccione el nivel de seguridad")
        print("1. Baja")
        print("2. Media")
        print("3. Alta")

        opcion = input("Opción: ")

        if opcion in ("1", "2", "3"):
            return opcion

        print("Opción inválida.\n")


# ---------------------------------
# Generar contraseña
# ---------------------------------
def generar_password(longitud, nivel):

    minusculas = string.ascii_lowercase
    mayusculas = string.ascii_uppercase
    numeros = string.digits
    simbolos = "@#-"

    password = []

    # -----------------------------
    # Nivel Bajo
    # -----------------------------
    if nivel == "1":

        caracteres = minusculas + numeros

        for _ in range(longitud):
            password.append(random.choice(caracteres))

    # -----------------------------
    # Nivel Medio
    # -----------------------------
    elif nivel == "2":

        caracteres = mayusculas + minusculas + numeros

        password.append(random.choice(mayusculas))
        password.append(random.choice(minusculas))
        password.append(random.choice(numeros))

        while len(password) < longitud:
            password.append(random.choice(caracteres))

        random.shuffle(password)

    # -----------------------------
    # Nivel Alto
    # -----------------------------
    else:

        caracteres = mayusculas + minusculas + numeros + simbolos

        password.append(random.choice(mayusculas))
        password.append(random.choice(minusculas))
        password.append(random.choice(numeros))
        password.append(random.choice(simbolos))

        while len(password) < longitud:
            password.append(random.choice(caracteres))

        random.shuffle(password)

    return "".join(password)


# ---------------------------------
# Mostrar descripción del nivel
# ---------------------------------
def mostrar_nivel(nivel):

    if nivel == "1":
        return "Baja"

    elif nivel == "2":
        return "Media"

    else:
        return "Alta"


# ---------------------------------
# Programa principal
# ---------------------------------
def main():

    print("=" * 40)
    print(" GENERADOR SEGURO DE CONTRASEÑAS")
    print("=" * 40)

    while True:

        longitud = obtener_longitud()

        nivel = obtener_nivel()

        password = generar_password(longitud, nivel)

        print("\nNivel de seguridad:", mostrar_nivel(nivel))
        print("Contraseña generada:")
        print(password)

        while True:

            opcion = input("\n¿Desea generar otra contraseña? (s/n): ").lower()

            if opcion in ("s", "n"):
                break

            print("Ingrese únicamente 's' o 'n'.")

        if opcion == "n":
            break

    print("\nGracias por utilizar el programa.")


main()