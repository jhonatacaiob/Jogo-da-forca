import random, math

def tem_caractere(um_caractere, uma_serie_de_letras):
    return uma_serie_de_letras.count(um_caractere) == 0


def e_palavra(uma_palavra):
    if(not tem_caractere(" ", uma_palavra) and palavra.isalpha()):
        return True
    else:
        print("\nDigite apenas uma palavra, sem numeros")
        print("+---------------------------------+")
        return False



def revelar_letras(uma_palavra, a_palavra_mostrada, uma_letra):
    
    uma_palavra_vetor = " ".join(uma_palavra).split(" ")
    a_palavra_mostrada_vetor = " ".join(a_palavra_mostrada).split(" ")
    
    indice = 0
    for i in range(0, uma_palavra_vetor.count(uma_letra)):
        indice = uma_palavra_vetor.index(uma_letra, indice, len(uma_palavra_vetor))
        a_palavra_mostrada_vetor[indice] = uma_letra
        indice += 1
    return "".join(a_palavra_mostrada_vetor)

def revelar_uma_letra(uma_palavra, a_palavra_mostrada, um_indice):
    
    uma_palavra_vetor = " ".join(uma_palavra).split(" ")
    a_palavra_mostrada_vetor = " ".join(a_palavra_mostrada).split(" ")
    
    a_palavra_mostrada_vetor[um_indice] = uma_palavra_vetor[um_indice]
    return "".join(a_palavra_mostrada_vetor)

#escolha de palavra

print("+----------JOGO DA FORCA----------+")
palavra = ""
while True:
    #palavra = input("Digite uma palavra: ").lower()
    palavra = "banana"
    if(e_palavra(palavra)):
        break



letras_chutadas = []
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
    opcao = input(": ")
    if(not opcao.isalpha()):
        opcao = int(opcao)
        if(opcao < 0 or opcao > 3):
            print("######## Opcao invalida ###########")
    else:
        print("######## Digite apenas numero ###########")

   
    if(opcao == 1): 
        if(numero_de_dicas <= 0):
            print("Sem mais dicas")
        else:
            indice_aleatorio = random.randint(0, len(palavra) - 1)
            palavra_mostrada = revelar_uma_letra(palavra, palavra_mostrada, indice_aleatorio)
            print(palavra_mostrada)
            numero_de_dicas-=1


    if(opcao == 2):
        letra = input("Digite uma letra: ").lower()[0]
        
        if(not letra.isalpha()):
            print("Digite apenas letras")

        elif(tem_caractere(letra, letras_chutadas)):
            print("Esta letra ja foi chutada!! Tente outra")

        elif(not tem_caractere(letra, palavra)):
            print("Não tem essa letra!! -1 vida")
            letras_chutadas.append(letra)
            numero_de_vidas -= 1

        else:
            palavra_mostrada = revelar_letras(palavra, palavra_mostrada, letra)
            letras_chutadas.append(letra)
            print(palavra_mostrada)

        if(numero_de_vidas == 0):

            print("Infelizmente você não advinhou a palavra")
            exit()

        if(palavra == palavra_mostrada):
            print("Parabens, você descobriu a palavra")
            exit()

    if(opcao == 3):
        print("Se você errar, você perde")
        palavra_chutada = input("Digite uma palavra: ")
        if(not tem_caractere(" ", palavra) and palavra.isalpha()):
            if(palavra_chutada==palavra):
                print("PARABENS!!! VOCÊ ACERTOU")
            else:
                print("Uma pena, você errou")
            exit()
        
        #chutar palavra
    if(opcao == 0):
        exit()
