from abc import abstractmethod, ABC

class Conta(ABC):
    def __init__(self, agencia, conta, saldo):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    @abstractmethod
    def sacar(self, valor):
        ...

    def depositar(self, valor):
        self.saldo += valor
        self.mensagem(f', você depositou: R$ {valor}')

    def mensagem(self, msg=''):
        print(f'O seu saldo é: R${self.saldo:.2f}{msg}')  


class ContaPoupanca(Conta):
    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            self.mensagem(f', você sacou: R$ {valor}') 
            return self.saldo
        else:
            print('Saldo insuficiente.')
            self.mensagem()


    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.conta!r}, {self.saldo!r})'
        return f'{class_name}{attrs}' 


class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo, limite):
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def mensagem_corrente(self, msg):
        print(f'O seu saldo é: R$ {msg}')

    def sacar(self, valor):
        saldo_com_limite = self.saldo + self.limite
        limite_utilizado = self.limite - (valor - self.saldo) 
        limite_pos_uso = self.limite - limite_utilizado
        if valor >= self.saldo:
            print(f'Seu saldo é insuficiente, mas você possui um limite extra de {self.limite}. Deseja utilizar ? (s/n)')
            print(f'Seu saldo com limite é: R$ {saldo_com_limite}')
            op = str(input('')).lower()
            if op == 's':
                saldo_com_limite -= valor
                self.mensagem_corrente(f'{saldo_com_limite:.2f} (limite), você sacou: R$ {valor} e utilizou R$ {limite_utilizado:.2f} do seu limite. Seu limite foi atualizado para R$ {limite_pos_uso:.2f}') 
                return self.saldo
            else:
                print('Saldo insuficiente.')
                self.mensagem()
        else:
            self.saldo -= valor
            self.mensagem(f', você sacou: R$ {valor}') 
            return self.saldo

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.conta!r}, {self.saldo}, {self.limite})'
        return f'{class_name}{attrs}'
