def tem_caractere(um_caractere, uma_string):
    if(uma_string.find(um_caractere) == -1):
        return False
    else:
        return True


#escolha de palavra

print("+----------JOGO DA FORCA----------+")
palavra = ""
while True:
    palavra = input("Digite uma palavra: ")
    if(not tem_caractere(" ", palavra)):
        break
    else:
        print("Digite apenas uma palavra")
        print("+---------------------------------+")
