def fatorial (numero):
    #caso base
 if numero == 0 or numero ==1:
      return 1
 else:
     return numero * fatorial (numero-1)
x = int(input("Digite um numéro para calcular seu fatorial"))
res = fatorial(x)
print(f"O fatorial de {x} é {res}")
