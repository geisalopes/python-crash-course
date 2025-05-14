# 🧑‍💻 1. input() – Entrada do usuário

# nome = input("Qual o seu nome?")
# print(f"Olá, {nome.title()}!")

# idade = int(input("Quantos anos voce tem?"))
# print(idade)


# 🔁 2. Laço while

# numero = 1

# while numero <= 5:
#     print(numero)
#     numero += 1


# ❗ 3. Sinalizadores (flags)

# ativo = True
# while ativo:
#     mensagem = input("Digite algo (ou 'sair'): ")
#     if mensagem == "sair":
#         ativo = False
#     else:
#         print(mensagem)


# 🔁 4. Usando break e continue

# break: Encerra o laço imediatamente
# continue: Pula para a próxima iteração

# while True:
#     cidade = input("Cidade visitada (ou 'sair'): ")
#     if cidade == "sair":
#         break
#     print(f"Você quer ir para {cidade.title()}")


# 📥 5. Laço com input() e while

prompt = "Digite sua cidade (ou 'sair'): "
while True:
    idade = input(prompt)
    if idade == "sair":
        break
    idade = int(idade)
    if idade < 3:
        print("Entrada gratuita")
    elif idade < 12:
        print("Ingresso 10$")
    else:
        print("Ingresso 15$")
