import principal

print('Bienvenido a Calculadora Splinter!!')
while True:
    def calculadora():
        n1 = float(input('Ingresa un numero: '))
        n2 = float(input('ingresa otro numero: '))
        oper = input('Ingresa una operacion: ')

        if oper == '+':
            principal.suma(n1, n2)
        elif oper == '-':
            principal.resta(n1, n2)
        elif oper == '*':
            principal.multi(n1, n2)
        elif oper == '/':
            principal.division(n1, n2)
        elif oper == '**':
            principal.elevar(n1, n2)
        elif oper == '//':
            principal.modulo(n1, n2)
        else:
            print('Ingresa un valor valido, quien sos q te haces la dificil? la gymbro? pelotudo')
            calculadora()

    calculadora()
    op = input('Deseas seguir usando la Calculadora Splinter? (S o N): ')
    if op == 'S' or 's':
        calculadora()
    else:
        print('Hasta la proxima B)')
        break