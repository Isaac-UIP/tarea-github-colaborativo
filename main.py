from trigonometria import menu_trigonometria
from contacuentos import contar_cuento
from contabilidad import menu_contabilidad

def main():
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Módulo de Trigonometría")
        print("2. Módulo de Cuenta Cuentos")
        print("3. Módulo de Contabilidad")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_trigonometria()
        elif opcion == "2":
            contar_cuento()
        elif opcion == "3":
            menu_contabilidad()
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
