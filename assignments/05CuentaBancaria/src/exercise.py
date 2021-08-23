def main():
    #escribe tu código abajo de esta línea
    pass

saldoant = float(input("Dame el saldo del mes anterior: "))
    ingresos = float(input("Dame los ingresos: "))
    egresos = float(input("Dame los egresos: "))
    cheques = int(input("Dame el número de cheques: "))
    saldomes = (saldoant + ingresos - egresos) - (cheques*13)
    saldototal = saldomes - (saldomes * .075)
    print("El saldo final de la cuenta es: " + str(saldototal))



if __name__ == '__main__':
    main()
