def menu_contabilidad():
    print("\n--- CONTABILIDAD ---")
    ingresos = float(input("Ingrese los ingresos: "))
    gastos = float(input("Ingrese los gastos: "))
    balance = ingresos - gastos
    print(f"Balance final: {balance:.2f}")
