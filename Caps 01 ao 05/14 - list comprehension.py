# list comprehensions pode substituir map e filter.
# também são mais velozes para grandes volumes de dados que map e filter.

lista = [1, 3, 5, 6, 7, 8, 9,6,46, 3,534, 43,5 ,6, 57,87,8,68]

print([caracter for caracter in "Maycon R Campos"])

print([numero for numero in lista if numero % 2 == 0])

print([numero ** 2 for numero in lista])

print([numero * 2 for numero in range(1, 50)])

celsius = [0, 10, 20, 30, 40]

fah = [((float(9) / 5) * temp + 32) for temp in celsius]
print(fah)


# list comprehension aninhado
print([numero ** 2 for numero in [num ** 2 for num in range(11)]])