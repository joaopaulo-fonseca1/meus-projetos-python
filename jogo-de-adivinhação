
import random

numero_secreto = random.randint(1, 10)
# Limite de 5 tentativas (sem ponto e vírgula!)
numero_tentativa = 5

while True:
    tentativa = int(input("Digite um número entre 1 e 10: "))

    if tentativa == numero_secreto:
        print("ACERTOOOOOOOOU! ")
        break
    elif tentativa < numero_secreto:  
        print("Tente um número maior! ")
    else:                            
        print("Tente um número menor! ")

    numero_tentativa = numero_tentativa - 1  
    print("Tentativas restantes:", numero_tentativa)
    print("-" * 30) 

    if numero_tentativa == 0:
        print(f"Você perdeu! O número secreto era {numero_secreto}. ")
        break
