def contar_cuento():
    print("\n--- CUENTA CUENTOS ---")
    cuento = input("Escriba un cuento corto: ")
    palabras = cuento.split()
    print(f"Cantidad de palabras: {len(palabras)}")
