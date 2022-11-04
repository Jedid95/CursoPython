"""
Entrada de dados - Input
"""

nome = input("Qual o seu nome? ") #input é sempre em type str
idade = input("Qual a sua idade? ")

ano_nascimento = 2022 - int(idade)

print(f'O usuário digitou {nome} e o tipo da variável é {type(nome)}')

print(f'{nome} tem {idade} anos e nasceu no ano de {ano_nascimento}')