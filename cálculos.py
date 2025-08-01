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
    while True:
        print("___________________________________")
        print("| Calculadora de áreas             |")
        print("| 1. Cuadrado                      |")
        print("| 2. Triángulo                     |")
        print("| 3. Círculo                       |")
        print("| 4. Salir                         |")
        print("|__________________________________|")
        opcion = input("Selecciona una opción (1-4): ")

        if opcion == "1":
            try:
                lado = float(input("Ingresa el lado del cuadrado: "))
                area = calcular_area_cuadrado(lado)
                print(f"Área del cuadrado: {area:.2f}")
            except ValueError as e:
                print("Error:", e)
        elif opcion == "2":
            try:
                base = float(input("Ingresa la base del triángulo: "))
                altura = float(input("Ingresa la altura del triángulo: "))
                area = calcular_area_triangulo(base, altura)
                print(f"Área del triángulo: {area:.2f}")
            except ValueError as e:
                print("Error:", e)
        elif opcion == "3":
            try:
                radio = float(input("Ingresa el radio del círculo: "))
                area = calcular_area_circulo(radio)
                print(f"Área del círculo: {area:.2f}")
            except ValueError as e:
                print("Error:", e)
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
