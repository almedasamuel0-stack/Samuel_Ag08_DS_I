import os
contador1 = 0
contador2 = 0
contador3 = 0
qtd_cad = 10

print("Bem vindo ao Sistema de Atendimento e Avaliação ao cliente!!")

while qtd_cad > 0:
    nome = input("Digite o seu nome: ")
    idade = input("Digite a sua Idade: ")
    sat = input(f"Qual foi o seu nível de Satisfação com o serviço? (SELECIONE UMA DAS OPÇÕES)\n1.EXCELENTE\n2.BOM\n3.RUIM\nOpção: ")
    if sat == '1':
        contador1 +=1
    elif sat == '2':
        contador2 +=1
    elif sat == '3':
        contador3 +=1
    else:
        print("Opção Inválida")
        print("Tente Novamente!")
        continue
    qtd_cad -= 1

print(f"O Número de RUINS: {contador3}")
print(f"O Número de BONS: {contador2}")
print(f"O Número de EXCELENTES: {contador1}")