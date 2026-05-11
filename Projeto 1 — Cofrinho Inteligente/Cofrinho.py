import os
import getpass

historico = []
saldo = 0

def mostrar_menu():
    print("\nPara depositar dinheiro digite --> 1")
    print("Para sacar dinheiro digite --> 2")
    print("Para ver o saldo digite --> 3")
    print("Ver Historico --> 4")
    print("logar/Cadastrar --> 5")
    print("Sair --> 6")
    print("limpar --> 7 \n")

    pass

def carregarUsuarios():
    user = {}
    try:
        with open("user.txt", "r", encoding="utf-8") as f:
            for linha in f:
                linha = linha.strip()
                if linha:
                    usuario, senha = linha.split(":")
                    user[usuario] = senha
    except FileNotFoundError:
        pass

    return user

def logar(user):
    usuario = input("Usuário: ")
    senha = getpass.getpass("Senha: ")
    
    if user.get(usuario) == senha:
        print("Login realizado com sucesso!")
        return True
    else:
        print("Usuário ou senha incorretos.")
        return False

def cadastro(user):
    usuario = input("Crie seu usuário: ")
    
    if usuario in user:
        print("Usuário já existe.")
        return user
    
    senha = getpass.getpass("Crie sua senha: ")
    
    with open("user.txt", "a", encoding="utf-8") as f:
        f.write(f"{user}:{senha}\n")
    
    user[usuario] = senha
    print("Cadastro realizado com sucesso!")
    
    return user
    

def add_historico(historico, mensagem):
    historico.append(mensagem)

def depositar_dinheiro(saldo, valor):
    if valor > 0:
        saldo += valor
        print("\nDeposito concluido com sucesso! \n")
        add_historico(historico, f"Deposito: {valor}")
    else:
        print("\nNão é possivel depossitar esse valor \n")

    return saldo

def sacar_dinheiro(saldo, valor):

    if valor > 0:
        if saldo >= valor:
            saldo -= valor
            print("\nSaque concluido com sucesso! \n")
            add_historico(historico, f"Saque: {valor}")
        else:
            print("\nSaldo insuficiente \n")
    else:
        print("\nNão é possivel sacar esse valor \n")
        
    return saldo

def ver_saldo(saldo):
    print(f"\nSeu saldo é: {saldo} \n")

def limpar():
    os.system('cls')

user = carregarUsuarios()

while True:
    mostrar_menu()
    opcao = input("Escolha: ")

    if opcao == "1":
        try:
            deposito = int(input("\nValor do deposito: "))
        except ValueError:
            print("Digite um valor valido")
            continue
        saldo = depositar_dinheiro(saldo, deposito)
    elif opcao == "2":
        try:
            sacar = int(input("\nQuanto o valor do saque: "))
        except ValueError:
            print("Digite um valor valido")
            continue
        saldo = sacar_dinheiro(saldo, sacar)
    elif opcao == "3":
        ver_saldo(saldo)
    elif opcao == "4":
        print("\n--- Historico ---")
        for i in historico:
            print(i)
    elif opcao == "5":
        while True:
            a = input("Deseja cadastrar(c) ou Logar(l)? ").lower()
            if a == "c":
                user = cadastro(user)
                break
            elif a == "l":
                user = logar(user)
                break
            else:
                print("Tente de novo")        

    elif opcao == "6":
        break
    elif opcao == "7":
        limpar()

