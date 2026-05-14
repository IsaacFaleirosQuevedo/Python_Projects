def conversorBinario (n):
    
    restos = []
    
    while n > 0:
        restos.append(n % 2)
        n //= 2

    binarios = int("".join(map(str, restos[::-1])))

    return binarios

def conversorDecimal (n):

    binario_list = list(str(n))[::-1]

    decimal = []

    for i, x in enumerate(binario_list):
        res = int(x) * (2 ** i)
        decimal.append(res)

    return sum(decimal)
    

q = input("Você quer converter decimal para binario (B) ou binario para decimal (D): ")

if q == "B":
    numero = int(input("Digite um numero: "))
    print(conversorBinario(numero))
else:
    numero = int(input("Digite um numero: "))
    print(conversorDecimal(numero))
