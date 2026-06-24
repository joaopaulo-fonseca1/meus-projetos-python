####Sistema de Registros Acadêmicos em Python

def inserir():
    nota = int(input("Digite a nota: "))
    listanota.append(nota)
    print("Nota inserida com sucesso!\n")

def remover():
    # Proteção: só remove se a lista não estiver vazia
    if len(listanota) > 0:
        listanota.pop()
        print("Última nota removida com sucesso!\n")
    else:
        print("A lista já está vazia!\n")

def media():
    # Proteção: evita o erro de divisão por zero
    if len(listanota) > 0:
        media_final = sum(listanota) / len(listanota)
        print(f"A média é: {media_final:.2f}\n")
    else:
        print("Nenhuma nota cadastrada para calcular a média!\n")
listanota = []

while True:
    print("Seja bem vindo ao sistema acadêmico!")
    print("Qual operação desejas realizar?")
    print("1 - Inserir nota \n2 - Remover última nota \n3 - Ver a média da turma \n4 - Sair")
    
    opcao = int(input("Escolha uma opção: "))
    print("-" * 30)

    if opcao == 1:
        inserir()
    elif opcao == 2:
        remover()
    elif opcao == 3:
        media()
    elif opcao == 4:
        print("Saindo do sistema... Até logo!")
        break
