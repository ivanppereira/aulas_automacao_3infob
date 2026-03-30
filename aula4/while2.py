#While

continuar = True

while continuar:
    print("Digite o nome do aluno: ")
    aluno = input()

    resp = int(input('Deseja continuar: \n0 para Não\n1 para SIM'))
    if resp == 0:
        continuar = False
    
   