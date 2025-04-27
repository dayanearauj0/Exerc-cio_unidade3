# para estrutura de repetição usa-se while / cadastro 3 alunos
contador = 1
while contador <=3:

# entrada de dados
    print(f"\nCadastro do {contador}º aluno:")
    aluno = input("digite seu nome: ")
    primeiranota = float(input("digite sua primeira nota de 0 à 10: "))
    segundanota =float(input("digite sua segunda nota de 0 à 10: "))

# calculando a mendia 
    media = float(primeiranota + segundanota)/2

# exibindo a media
    print(f"aluno: {aluno}")
    print(f"media: {media:.2f}")

# saida de dados
    if media >= 7:
        print(f"parabéns, sua média foi: {media:.2f} .aluno aprovado")
    elif media >= 5:
        print(f"sua media foi : {media:.2f} .vocÊ está de recuperação!")
    else:
        print(f"sua media foi : {media:.2f} .você foi reprovado!")


    contador += 1




