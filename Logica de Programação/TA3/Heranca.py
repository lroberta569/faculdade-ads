#HERANÇA EM PYTHON
class Pessoa:
    def __init__(self):
        self.cpf = None
        self.nome = None
        self.endereco = None

class Funcionario(Pessoa):
    def __init__(self):
        self.matricula = None
        self.salario = None
    def baterPonto(self):
        #Código aqui
        pass
    def fazerLogin(self):
        #Código aqui
        pass

f1 = Funcionario()
f1.nome = "Funcionário A"
print(f1.nome)

class Cliente(Pessoa):
     def __init__(self):
        self.dataCadastro = None
        self.venda = None

c1 = Cliente()
c1.cpf = "111.111.111-11"
print(c1.cpf)
