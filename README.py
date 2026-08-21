# meus-exercicios-python-iniciante - 2
São questões simples para minha pessoa ter uma ser noção do meu progresso. 

nome = str(input("Qual é o seu nome? "))

if nome == "Alan":
    print("Que nome bonito.")

elif nome == "Alice" or nome == "Gabriel" or nome == "João":
    print("Seu nome é bem popular no Bradil.") 
    
elif nome == "Alecsander":
    print("Até que é legal. Dá pro gasto.")
    
elif nome in "Ana Jéssica Carol Juliana":
    print("Belo nome feminino.")
        
else:
    print("Seu nome até que é normal.")
        
print("Olá,", nome, ".")
