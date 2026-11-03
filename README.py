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
