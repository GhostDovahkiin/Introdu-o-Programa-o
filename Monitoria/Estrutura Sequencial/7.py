print("## Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário ##")
lado = float(input("Digite o tamanho dos lados do quadrado: "))
area = lado**2
area2 = area*2
print("O dobro da área do quadrado de lado {:.0f} é: {:.2f}" .format(lado, area2))
