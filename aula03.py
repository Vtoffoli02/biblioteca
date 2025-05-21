nome = "alinu"


idade=0
altura=1.90

peso: float = 99
idade: int = 77

input("digite a sua idade")

valor = 10/3

print("conta",valor)

idade = int(input("digite sua idade:"))

print("a idade digitada foi:",idade,"ea sua alturae:",altura)
print(f"o resultado do calculo e:{idade * altura} continua {valor}")

def somar(a,b):
    resultado = a + b
    return resultado

    resultado_soma = somar(38,58)
    print(resultado_soma)

def saudar(nome="visitante",idade=10):
    print(f"ola,{nome}sua idade e {idade}!")

#chamando a funcão
saudar()
saudar(idade=45,nome="jose")