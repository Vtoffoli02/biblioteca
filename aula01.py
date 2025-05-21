
#programaçao procedural

#variaveis
#padrão de projeto
#tipar as variaveis
#snackcase =palavra_palavra exemplo: status_curso

#aqui essas variaveis estão no escopo global
print("inicio")
idade: int=38
nome:str="mario"
status_curso:bool= True
peso: float= 34.400

#essa função nao recebe e nao retorna nenhum parametro
def exibe_dados_aluno():
    print("1.a idade do aluno",nome, "e:",idade,"anos", sep='|')
    print(f"2.a idade do aluno: {nome} e {idade} anos")

    return "ok"

#chamar a função aqui
exibe_dados_aluno()
print("fim")

#nao recebe e nao devolve nenhum retorno
def exibenome():
    print("nome")


def exibenome(nome: str):
    print("nome")



#outras estruturas de dados-> complexas
tuplanumeros=(10,20,30,40)


print("numeros exibidos?",mostraNumeros(tuplanumeros))

listadados=["teste","debug"]

print(listadados(0))

print(listadados(1))

print(listadados(0)(1))



#orientação a objeto

#programação funcional