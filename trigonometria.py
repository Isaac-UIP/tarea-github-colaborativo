import math

def menu_trigonometria():
    print("\n--- TRIGONOMETRÍA ---")
    angulo = float(input("Ingrese un ángulo en grados: "))
    radianes = math.radians(angulo)

    print(f"Seno: {math.sin(radianes):.2f}")
    print(f"Coseno: {math.cos(radianes):.2f}")
    print(f"Tangente: {math.tan(radianes):.2f}")
