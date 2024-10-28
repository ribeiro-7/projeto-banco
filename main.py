import banco
import pessoas
import contas


c1 = pessoas.Cliente('Arthur', 19)
cc1  = contas.ContaCorrente(111, 222, 0, 0)
c1.conta = cc1
banco = banco.Banco()
banco.clientes.extend([c1])
banco.contas.extend([cc1])
banco.agencias.extend([111])

print(banco.autenticar(c1, cc1))

c2 = pessoas.Cliente('Glauco', 19)
cc2 = contas.ContaPoupanca(123, 777, 0)
c2.conta = cc2
banco.clientes.extend([c2])
banco.contas.extend([cc2])
banco.agencias.extend([123])

print(banco.autenticar(c2, cc2))

print(banco)