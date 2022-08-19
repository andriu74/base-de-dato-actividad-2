#Crear una lista con los elemntos de los numeros de la Serie de Fibonacci

# Partiendo con los nuemeros inicales [0, 1].

def rec_fib(c):
    if c > 1:
        return rec_fib(c-1) + rec_fib(c-2)
    return c
for i in range(15):
    print(rec_fib(i))
    