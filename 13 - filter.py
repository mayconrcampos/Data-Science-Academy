lista = [34, 34 , 32, 33, 325, 6,654, 55, 76, 4,64 ,6,46 ,46,4, 6,46, 4, 67, 889, 9867]

def verificaPar(n):
    if n % 2 == 0:
        return True
    else:
        return False

print(verificaPar(35))

# agora usando filter

print(f"Somente os números pares da lista: {list(filter(verificaPar, lista))}")


print(f"Somente os impares com lambda: {list(filter(lambda x: x % 2 != 0, lista))}")

