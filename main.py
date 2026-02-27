aluno: str
atividade: float
trabalho: float
pb: float
media: float
soma: float
nota_bimestre: float

#dados de entrada

aluno = input("Digite o nome do aluno: ")
atividade = float(input("Nota das atividades: "))
trabalho = float(input("Nota de trabalho: "))
pb = float(input("Agora, digite a nota da prova bimestral: "))

#expressão do cálculo

soma = (atividade + trabalho) + pb

print(f"Nota final de {aluno} é {soma}")







