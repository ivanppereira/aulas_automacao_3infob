'''
Crie um app que solicite duas notas do usuário, 
após calcule a média das notas. Se a media for maior ou igual a 6
mostre uma mensagem dizendo que o aluno está aprovado. Se a média for
menor que 6, peça para o aluno digitar a nota do exame final. Calcule
novamente a media após o exame final ((media + exame final) / 2). Se a 
média final for maior que 6 mostre a mensagem aprovado, senão mostre que 
o aluno foi reprovado.
'''

#Entrada
nota1 = float(input('Digite a primeira Nota'))
nota2 = float(input('Digite a segunda Nota'))

#Processamento
media = (nota1 + nota2) / 2

if media >= 6:
    print('Aluno aprovado')
else:
    exame_final = float(input('Digite a nota do exame final'))
    nova_media = (media + exame_final) / 2
    
    if nova_media >= 6:
        print('Aluno aprovado')
    else:
        print('Reprovado')

