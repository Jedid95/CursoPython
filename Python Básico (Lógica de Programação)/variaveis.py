"""
Iniciar com letra, pode conter números, separar _, letras minúsculas
"""

nome = 'Jedid'
print(nome, type(nome))

idade = 27
altura =1.74
e_maior = idade>18
peso = 72

print('Nome:', nome)
print('Idade:', idade)
print('Altura:', altura)
print('É maior:', e_maior)

imc = peso / (altura * altura)
print(nome, 'tem', idade, 'anos de idade e seu IMC é', imc)
