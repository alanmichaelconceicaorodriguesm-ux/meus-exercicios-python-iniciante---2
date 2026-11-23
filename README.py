# Aqui Está e uma utilização do dicionário. 

pessoa = {
    "nome": "Teste.",
    "peso": 0.0,
    "idade": 0
}

print("Dados do usuário logo abaixo:")
print("Nome: ", pessoa["nome"])
print(f"Peso: {pessoa["peso"]}.")
print(pessoa["idade"]) 

print()

# Nestes exemplos de linhas acima coloquei 3 tipos de maneiras de fazer, claro que resultam quase no mesmo resultado.

pessoa["nome"] = "Alan"
pessoa["peso"] = 57.3
pessoa["idade"] = 17

print(f"Nome: {pessoa["nome"]}.")
print(f"Peso: {pessoa["peso"]}.")
print(f"Idade: {pessoa["idade"]}.")

print()

# Este bloco de comando está com informaçãoes inseridas. Acima

pessoa["nome"] = str(input("Digite seu nome: "))
pessoa["peso"] = float(input("Digite seu peso: "))
pessoa["idade"] = int(input("Digite sua idade: "))

print(f"Nome: {pessoa["nome"]}.\nPeso: {pessoa["peso"]}.\nIdade: {pessoa["idade"]}.") 
# Logo acima o usuário insirar seus dados.

print("CADASTRO DE PESSOA")
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))
peso = float(input("Digiite seu peso: "))

print()

print(f"Nome: {nome}.\nIdade: {idade} anos.\nAltura: {altura:.2f} metros.\nPeso: {peso:.2f} kg.")


# Metodologia de dicionário, que é uma estrutura de dados que armazena pares de chave-valor.0

pessoa = {"nome": "Teste.", "peso": 0.0, "cidade": "Madri"}
print(pessoa["nome"])
print(pessoa.get("nome"))
print(pessoa.get("Telefone", "O campo telefone não existe."))

print()

print(pessoa.keys())
print(pessoa.values())
print(pessoa.items())

print()

pessoa = {"nome": "Teste.", "peso": 0.0, "cidade": "Madri"}
pessoa.update({"profissão": "Programador"})
pessoa.pop("profissão")
print(pessoa)
pessoa.clear()
print(pessoa)

print()

# Aqui está um exemplo de como utilizar o dicionário em Python. Palvras-chave são únicas e imutáveis, enquanto os valores podem ser de qualquer tipo de dado. Dicionários são úteis para armazenar informações relacionadas a um objeto ou entidade, como dados de uma pessoa, produto ou configuração de system.
busca = str(input("Digite o código do produto: "))
        for produto in listaproduto:
            if produto["id"] == busca:
                print("Achou!")
            else:
                print("Não achou!")
                            
                id = str(input("Digite o código do produto: "))
                nome = str(input("Nome do produto: "))
                qualidade = str(input("Qualidade do produto: "))
                preco = float(input("Preço do produto: "))
                cor = str(input("Cor do produto: "))
                peso = float(input("Peso do produto: "))
                qtd = int(input("Quantidade do produto: "))
                
                altera = str(input("Deseja alterar esse item (s/n)? "))
#

pessoa = {"nome": "Ali", "idade": 25, "cidade": "Rio"}
pessoa ["profissão"] = "Engenheiro"
print(pessoa)
pessoa["idade"] = 50
print(pessoa)
del  pessoa["profissão"]


# Forma mais refinada de utilizar o dicionário, com a utilização do for para percorrer os itens do dicionário.

pessoa = {"nome": "Teste.", "peso": 0.0, "idade": 0}
for i in pessoa:
    print(i, end=" - ")
    
pessoa = {"nome": "Teste.", "peso": 0.0, "idade": 0}
for i, j in pessoa.items():
    print(i, ": ", j, end=" - ")
    
alunos = {"nome": "Pedro", "cidade": "Madri", "idade": 27}
for chave, valor in alunos.items():
    print(chave, ":", valor, end=" - ") 
    
print()

# Logo abaixo tem um exercício de um dicionário sobre as notas dos alunos.

print()

turma = [{"nome": "Carlos", "nota": 8.5},
        {"nome": "Ali", "nota": 7.8}, 
        {"nome": "Rali", "nota": 9.0}]


for aluno in turma:
    print(aluno["nome"], aluno["nota"])

print()

aluno1 = {"nome": "Carlos", "nota": 8.5}
aluno2 = {"nome": "Ali", "nota": 7.8} 
aluno3 = {"nome": "Rali", "nota": 9.0}

turma = [aluno1, aluno2, aluno3]

for aluno in turma:
    print(aluno["nome"], aluno["nota"])

print()

turma = [{"nome": "Carlos", "nota": 8.5},
        {"nome": "Ali", "nota": 7.8}, 
        {"nome": "Rali", "nota": 9.0}]


aluno4 = {"nome": "Tatiana", "nota": 10.0}
aluno0 = {"nome": "J", "nota": 10.0}

turma.append(aluno4)
turma.insert(0, aluno0)

for aluno in turma:
    print(aluno["nome"], aluno["nota"])

# Aqui Está e uma utilização do dicionário. 

pessoa = {
    "nome": "Teste.",
    "peso": 0.0,
    "idade": 0
}

print("Dados do usuário logo abaixo:")
print("Nome: ", pessoa["nome"])
print(f"Peso: {pessoa["peso"]}.")
print(pessoa["idade"]) 

print()

# Nestes exemplos de linhas acima coloquei 3 tipos de maneiras de fazer, claro que resultam quase no mesmo resultado.

pessoa["nome"] = "Alan"
pessoa["peso"] = 57.3
pessoa["idade"] = 17

print(f"Nome: {pessoa["nome"]}.")
print(f"Peso: {pessoa["peso"]}.")
print(f"Idade: {pessoa["idade"]}.")

print()

# Este bloco de comando está com informaçãoes inseridas. Acima

pessoa["nome"] = str(input("Digite seu nome: "))
pessoa["peso"] = float(input("Digite seu peso: "))
pessoa["idade"] = int(input("Digite sua idade: "))

print(f"Nome: {pessoa["nome"]}.\nPeso: {pessoa["peso"]}.\nIdade: {pessoa["idade"]}.") 

# Logo acima o usuário insirar seus dados.

print("CADASTRO DE PESSOA")
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))
peso = float(input("Digiite seu peso: "))

print()

print(f"Nome: {nome}.\nIdade: {idade} anos.\nAltura: {altura:.2f} metros.\nPeso: {peso:.2f} kg.")

pessoa = {}

pessoa["nome"] = "Alan"
pessoa["peso"] = 57.3
pessoa["idade"] = 17

print(f"Nome: {pessoa["nome"]}.\nPeso: {pessoa["peso"]}.\nIdade: {pessoa["idade"]}.") 

pessoa["nome"] = str(input("Digite seu nome: "))
pessoa["peso"] = float(input("Digite seu peso: "))
pessoa["idade"] = int(input("Digite sua idade: "))

print(f"Nome: {pessoa["nome"]}.\nPeso: {pessoa["peso"]}.\nIdade: {pessoa["idade"]}.") 
 

print("CADASTRO DE PESSOA")
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))
peso = float(input("Digiite seu peso: "))

print()

print(f"Nome: {nome}.\nIdade: {idade} anos.\nAltura: {altura:.2f} metros.\nPeso: {peso:.2f} kg.")

pessoa = {}

pessoa["nome"] = "Alan"
pessoa["peso"] = 57.3
pessoa["idade"] = 17

print(f"Nome: {pessoa["nome"]}.\nPeso: {pessoa["peso"]}.\nIdade: {pessoa["idade"]}.") 

pessoa["nome"] = str(input("Digite seu nome: "))
pessoa["peso"] = float(input("Digite seu peso: "))
pessoa["idade"] = int(input("Digite sua idade: "))

for chave, vaga in pessoa.items():
    print(chave, ":", vaga)


listaproduto = []
while True:
    print("DIGITE A OPÇÃO")
    print("1 - Cadastrar.")
    print("2 - Alterar.")
    print("3 - Excluir.")
    print("4 - Listar.")
    print("5 - Consultar.")
    print("6 - Sair")

    opc = int(input("Opção: "))

    if opc  == 1:
        
        while True:
            id = int(input("Digite o código do produto: "))
            nome = str(input("Nome do produto: "))
            qualidade = str(input("Qualidade do produto: "))
            preco = float(input("Preço do produto: "))
            cor = str(input("Cor do produto: "))
            peso = float(input("Peso do produto: "))
            qtd = int(input("Quantidade do produto: "))
            

            
            listaproduto.append({"nome": nome, "qualidade": qualidade, "preco": preco, "cor": cor, "peso": peso, "qtd": qtd})
            
            sn = str(input("Deseja sair (S/N)? ")).lower()
            if sn == "s":
                break
            
        print(listaproduto)

    elif opc  == 2:
        print()
    elif opc  == 3:
        print()
    elif opc  == 4:
        print()
    elif opc  == 5:
        print()
    elif opc  == 6:
        print()
        break
    else:
        print()
           

listaproduto = []
opc = 0
while opc != 6:
    print("DIGITE A OPÇÃO")
    print("1 - Cadastrar Produto.")
    print("2 - Alterar.")
    print("3 - Excluir.")
    print("4 - Listar.")
    print("5 - Consultar.")
    print("6 - Sair")

    opc = int(input("Opção: "))

    if opc  == 1:

        while True:
            id = int(input("Digite o código do produto: "))
            nome = str(input("Nome do produto: "))
            qualidade = str(input("Qualidade do produto: "))
            preco = float(input("Preço do produto: "))
            cor = str(input("Cor do produto: "))
            peso = float(input("Peso do produto: "))
            qtd = int(input("Quantidade do produto: "))
            

            
            listaproduto.append({"nome": nome, "qualidade": qualidade, "preco": preco, "cor": cor, "peso": peso, "qtd": qtd})
            
            sn = str(input("Deseja sair (S/N)? ")).lower()
            if sn == "s":
                break
            
            print()
            
        print(listaproduto)

    elif opc  == 2:
        print()
    elif opc  == 3:
        print()
    elif opc  == 4:
        print()
    elif opc  == 5:
        print()
    elif opc  == 6:
        print()
        break
    else:
        print()

listaproduto = []
opc = 0
while opc != 6:
    print("DIGITE A OPÇÃO")
    print("1 - Cadastrar Produto.")
    print("2 - Alterar.")
    print("3 - Excluir.")
    print("4 - Listar.")
    print("5 - Consultar.")
    print("6 - Sair")

    opc = str(input("Opção: "))

    if opc  == "1":

        while True:
            id = int(input("Digite o código do produto: "))
            nome = str(input("Nome do produto: "))
            qualidade = str(input("Qualidade do produto: "))
            preco = float(input("Preço do produto: "))
            cor = str(input("Cor do produto: "))
            peso = float(input("Peso do produto: "))
            qtd = int(input("Quantidade do produto: "))
            
            listaproduto.append({"nome": nome, "qualidade": qualidade, "preco": preco, "cor": cor, "peso": peso, "qtd": qtd})
            
            sn = str(input("Deseja sair (S/N)? ")).lower()
            if sn == "s":
                break
            
            print()
            
        print(listaproduto)

    elif opc  == "2":
        print()
    elif opc  == "3":
        print()
    elif opc  == "4":
        print()
    elif opc  == "5":
        print()
    elif opc  == "6":
        print()
        break
    else:
        print()


elif opc == "2":
    busca = int(input("Digite o código do produto: "))

    for produto in listaproduto:
        if produto["id"] == busca:
            print("Achou!")
            # Faça a alteração aqui
            break
    else:
        print("Não achou!")

