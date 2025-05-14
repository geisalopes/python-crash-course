# 🗂 1. Criando um dicionário
pessoa = {"nome": "geisa", "idade": 40, "cidade": "berlin"}


# 🔍 2. Acessando valores
print(pessoa["nome"])  # geisa
print(pessoa["idade"])  # 40

print("--------------------\n")

# 🧱 3. Adicionando e modificando pares
pessoa["profissão"] = "desenvolvedora"
pessoa["idade"] = 41

print(pessoa["nome"])  # geisa
print(pessoa["idade"])  # 41
print(pessoa["profissão"])

# 🧹 4. Removendo pares
del pessoa["cidade"]

print("--------------------\n")

# 🔁 5. Iterando com for

#     Sobre chaves:
for chave in pessoa:
    print(chave)

print("--------------------\n")

# Chaves + valores:
for chave, valor in pessoa.items():
    print(f"{chave.title()}: {valor}")
print("--------------------\n")

# 🧾 6. Métodos úteis
pessoa.get("telefone", "Nao encontrado")  # Evita erro se a chave não existir

pessoa = {"nome": "geisa", "idade": 40}

print(pessoa.get("nome"))  # geisa
print(pessoa.get("cidade", "N/A"))  # N/A (porque "cidade" não está no dicionário)
print(pessoa.get("idade", "desconhecida"))  # 40

print("--------------------\n")
# 📦 7. Dicionários aninhados

# Lista de dicionários:

usuarios = [{"nome": "geisa", "idade": 41}, {"nome": "diogo", "idade": 46}]

# Dicionário com listas:

pizza = {"massa": "fina", "ingredientes": ["tomate", "manjericao", "azeitona"]}

print(pizza)
