tamanho = float(input("Digite o tamanho do arquivo em MB: "))
velocidade = float(input("Digite a velocidade de sua internet em Mbps: "))
tempo = (tamanho / (velocidade*60))
print("O tempo para download é: {:.1f}s" .format(tempo))
