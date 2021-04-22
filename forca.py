import random, math

def tem_caractere(um_caractere, uma_string):
    if(uma_string.find(um_caractere) == -1):
        return False
    else:
        return True

def revelar_letra(uma_palavra, a_palavra_mostrada, uma_letra):
    
    uma_palavra_vetor = " ".join(uma_palavra).split(" ")
    a_palavra_mostrada_vetor = " ".join(a_palavra_mostrada).split(" ")
    
    indice = 0
    for i in range(0, uma_palavra_vetor.count(uma_letra)):
        indice = uma_palavra_vetor.index(uma_letra, indice, len(uma_palavra_vetor))
        a_palavra_mostrada_vetor[indice] = uma_letra
        indice += 1
    return "".join(a_palavra_mostrada_vetor)

def revelar_uma_letra(uma_palavra, a_palavra_mostrada, um_indice):
    print(um_indice)
    uma_palavra_vetor = " ".join(uma_palavra).split(" ")
    a_palavra_mostrada_vetor = " ".join(a_palavra_mostrada).split(" ")
    
    a_palavra_mostrada_vetor[um_indice] = uma_palavra_vetor[um_indice]
    return "".join(a_palavra_mostrada_vetor)

#escolha de palavra

print("+----------JOGO DA FORCA----------+")
palavra = ""
while True:
    palavra = input("Digite uma palavra: ").lower()
    if(not tem_caractere(" ", palavra) and palavra.isalpha()):
        break
    else:
        print("\nDigite apenas uma palavra, sem numeros")
        print("+---------------------------------+")

numero_de_vidas = 6
numero_de_dicas = math.floor(len(palavra) / 3)
palavra_mostrada = "_" * len(palavra)

for i in range(random.randint(100,1000)):
    print()

print("+----------JOGO DA FORCA----------+")
while True:
    print("+---------------------------------+")
    print(f"Você tem {numero_de_vidas} vidas e {numero_de_dicas} dicas")
    print("O que deseja fazer")
    print("1. Dica")
    print("2. Chutar uma letra")
    print("3. Chutar a palavra")
    print("0. Sair")
    opcao = int(input(": "))

    if(opcao == 1):
        if(numero_de_dicas < 0):
            print("Sem mais dicas")
        else:
            indice_aleatorio = random.randint(0, len(palavra) - 1)
            palavra_mostrada = revelar_uma_letra(palavra, palavra_mostrada, indice_aleatorio)
            print(palavra_mostrada)
            numero_de_dicas-=1


    if(opcao == 2):
        pass
        #chutar letra
    if(opcao == 3):
        pass
        #chutar palavra