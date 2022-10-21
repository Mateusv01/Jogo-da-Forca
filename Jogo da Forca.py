palavras = [
     "palavra",
     "abracadabra",
     "mochila",
     "cabo",
     "vacina",
     "meia",
     "cadeira",
     "abacate",
     "cebola",
     "radio"
     ]

print("==========ESCOLHA DE PALAVRA==========")
indice = int(input("Digite um número"))
palavra = palavras[(indice*776) % len(palavras)]

for espaço in range(50):
     print()















letras_descobertas = []
digitadas = []
erros = 0


print("\n====JOGO DA FORCA=====")

for i in range(0,len(palavra)):
     letras_descobertas.append("-")

acertou = False

while acertou == False :
     letra = input("Digite a letra: ").lower().strip()
     if letra in digitadas:
          print("Você já fez essa tentativa") 
          continue
     else:
          digitadas += letra
          if letra in palavra:
               letras_descobertas += letra
          else:
               erros += 1
               print("Errou")
               if erros == 1:
                    print("""|====FORCA====||             
|----         |
||  O         |
||            |
||            |
||______      |
|=============|""")

               if erros == 2:
                    print("""|====FORCA====||             
|----         |
||  O         |
||  |         |
||            |
||______      |
|=============|""")
               if erros == 3:
                    print("""|====FORCA====||             
|----         |
||  O         |
||  |/        |
||            |
||______      |
|=============|""")
               if erros == 4:
                    print("""|====FORCA====||             
|----         |
||  O         |
|| \|/        |
||            |
||______      |
|=============|""")
               if erros == 5:
                    print("""|====FORCA====||             
|----         |
||  O         |
|| \|/        |
|| /          |
||______      |
|=============|""")
               if erros == 6:
                    print("""|====FORCA====||             
|----         |
||  O         |
|| \|/        |
|| /|         |
||______      |
|==ENFORCADO==|""") 
                    print("Enforcado")
                    print(f"A palavra era {palavra}")
                    break
                    
      







     for i in range(0,len(palavra)):
          if letra == palavra[i]:
               letras_descobertas[i] = letra
          print(letras_descobertas[i])
     acertou = True

     for x in range(0,len(letras_descobertas)):
          if letras_descobertas[x] == "-" :
               acertou = False


               
          
