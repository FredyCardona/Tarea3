import math


def calcular_area_cuadrado(lado):
    if lado <= 0:
        raise ValueError("El lado debe ser mayor que cero.")
    return lado * lado

def calcular_area_triangulo(base, altura):
    if base <= 0 or altura <= 0:
        raise ValueError("La base y la altura deben ser mayores que cero.")
    return (base * altura) / 2

def calcular_area_circulo(radio):
    if radio <= 0:
        raise ValueError("El radio debe ser mayor que cero.")
    return math.pi * radio ** 2

def main():
    print("___________________________________")
    print("| Calculadora de áreas             |")
    print("|1. Cuadrado                       |")
    print("|2. Triángulo                      |")
    print("|3. Círculo                        |")
    print("|__________________________________|")
    opcion = input("Selecciona una opción (1-3): ")
    opcion = int(opcion)

    if opcion == 1:
        lado = input("Ingresa el lado del cuadrado: ")
        lado = float(input)
        print("Área del cuadrado:", calcular_area_cuadrado(lado))
    elif opcion == 2:
        base =input("Ingresa la base del triángulo: ")
        altura=input("Ingresa la altura del triángulo: ")
        base = float(base)
        altura = float(altura)
        print("Área del triángulo:", calcular_area_triangulo(base, altura))
    elif opcion == 3:
        radio = input("Ingresa el radio del círculo: ")
        radio = float(radio)
        print("Área del círculo:", calcular_area_circulo(radio))
    else:
        print("Opción no válida.")

if __name__ == "__main__":
    main()
