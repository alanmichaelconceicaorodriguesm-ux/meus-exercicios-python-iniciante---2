senha = int(input("Digite sua senha: "))
nome = str(input("Digite seu nome usuário: "))

senha = str(senha)

if senha == "1234" and nome == "Alan":
    print("Acesso concedido.")
    print(f"Usuário: {nome}")
    
else:
    print("Acesso negado.")
    print("Suas ações são inválidas.")
    
print("Obrigado por utilizar nossos serviços")
