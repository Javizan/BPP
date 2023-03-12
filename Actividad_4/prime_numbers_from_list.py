import pdb
pdb.set_trace()

def es_primo(x=int):
    divisors = 0
    for i in range(2,x-1):
        if x%i == 0:
            divisors += 1
    if divisors == 0:
        return True

numeros = list(range(1,100))
primos = list(filter(es_primo, numeros))
print(primos)