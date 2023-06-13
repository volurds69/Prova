from Classes import ContaLuz,Contas

historicoContas = Contas()

historicoContas.addContaLuz(ContaLuz("125","001",150))
historicoContas.addContaLuz(ContaLuz("125","002",175))
historicoContas.addContaLuz(ContaLuz("125","003",190))
historicoContas.addContaLuz(ContaLuz("125","004",150))
print(historicoContas.mediaConsumidor())