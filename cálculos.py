import math

def calcular_area_cuadrado(lado):
    return lado * lado

def calcular_area_triangulo(base, altura):
    return (base * altura) / 2

def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def main():
    print("___________________________________")
    print("| Calculadora de áreas             |")
    print("|1. Cuadrado                       |")
    print("|2. Triángulo                      |")
    print("|3. Círculo                        |")
    print("|__________________________________|")
    opcion = input("Selecciona una opción (1-3): ")

    if opcion == "1":
        lado = float(input("Ingresa el lado del cuadrado: "))
        print("Área del cuadrado:", calcular_area_cuadrado(lado))
    elif opcion == "2":
        base = float(input("Ingresa la base del triángulo: "))
        altura = float(input("Ingresa la altura del triángulo: "))
        print("Área del triángulo:", calcular_area_triangulo(base, altura))
    elif opcion == "3":
        radio = float(input("Ingresa el radio del círculo: "))
        print("Área del círculo:", calcular_area_circulo(radio))
    else:
        print("Opción no válida.")

if __name__ == "__main__":
    main()
