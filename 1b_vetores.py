# Problema: Criar um vetor para ser preenchido com nomes

#Minha Soluução

#1) import da lib os pra fazer o limpa tela após cada operação
import os

# 2) Decxlaro uma lista vazia
# Escolho a lista por que é só pra inserção de um mesmo tipo de dado
in_list_name = []

# 3) Faço um loop for com um range/limite de 3 iterações
for i in range(3):
    # Dentro do loop crio um input pra entrada de dados do user a ser armazenada na var value
    value = input("\nInforme nome: ")
    # Insiro o valor de value ao fim da lista com .append(value)
    in_list_name.append(value)
    # chamo a lib os com o metodo system passando por param o comando "cls" que limpa o terminal
    os.system("cls")

# 4) Exibo um titulo em string seguido da lista de nomes
# uso print f pra utilizar template string
print(f"in_list_name:\n{in_list_name}")
#5) Pulo uma linha
print()

# 5) Exibo uma string com o titulo
print("names in in_list_name:")
# 6) Crio um loop for pra percorrer cada item de toda a lista
for name in in_list_name:
    # Exibo o item referente a cada iteração
    print(name)
