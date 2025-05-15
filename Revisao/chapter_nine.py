# 🧱 1. Criando uma classe simples


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Oi, meu nome é {self.nome} e tenho {self.idade} anos.")


geisa = Pessoa("Geisa", 40)
geisa.apresentar()


print("----------------------\n")
# 🧰 2. Atributos padrão


class Conta:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0

    def exibe_saldo(self):
        print(f"{self.titular} tem ${self.saldo}")


geisa = Conta("Geisa")
geisa.exibe_saldo()

print("----------------------\n")
# 🧬 3. Herdando de outra classe


class Admin(Pessoa):  # Herdando da classe Pessoa
    def __init__(self, nome, idade, permissao):
        super().__init__(nome, idade)  # chama o construtor da classe mãe
        self.permissao = permissao

    def mostrar_permissao(self):
        print(f"Permissão: {self.permissao}")


admin1 = Admin("Geisa", 40, "acesso total")

admin1.apresentar()
admin1.mostrar_permissao()
