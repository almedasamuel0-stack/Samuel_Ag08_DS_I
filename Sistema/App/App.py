import os
contador1 = 0
contador2 = 0
contador3 = 0
# Contadores das opções 
qtd_cad = 10
# Quantidade de Candidatos

print("Bem vindo ao Sistema de Atendimento e Avaliação ao cliente!!")

while qtd_cad > 0:
    # Condição de repetição do laço
    nome = input("Digite o seu nome: ")
    idade = input("Digite a sua Idade: ")
    sat = input(f"Qual foi o seu nível de Satisfação com o serviço? (SELECIONE UMA DAS OPÇÕES)\n1.EXCELENTE\n2.BOM\n3.RUIM\nOpção: ")
    # Inserção das informações
    if sat == '1':
        contador1 +=1
        # Verificação e atribuição do Excelente
    elif sat == '2':
        contador2 +=1
        # Verificação e atribuição do Bom
    elif sat == '3':
        contador3 +=1
        # Verificação e Atribuição do Ruim
    else:
        print("Opção Inválida")
        print("Tente Novamente!")
        continue
        # Mensagem de opção Inválida e uso o continue para repetção do laço
    qtd_cad -= 1
    # Decrementa um candidato até "romper a condição de repetição"

print(f"O Número de RUINS: {contador3}")
print(f"O Número de BONS: {contador2}")
print(f"O Número de EXCELENTES: {contador1}")
# Imprime os resultados