# fibonacci
def fibonacci(num):
    fib1 = 1
    fib2 = 1
    fib3 = 0
    count = num
    while count > 0:
        print(fib1, end=" ")
        fib3 = fib1 + fib2
        fib1 = fib2
        fib2 = fib3
        count -= 1
    print()

numero = int(input("Digite um número: "))
fibonacci(numero)
