# Função que calcula a média de três notas
def calcular_media(n1, n2, n3):
    return (n1 + n2 + n3) / 3

def main():
    try:
        nota1 = float(input("Digite a primeira nota: "))
        nota2 = float(input("Digite a segunda nota: "))
        nota3 = float(input("Digite a terceira nota: "))
    except ValueError:
        print("Erro: Por favor, digite apenas valores numéricos.")
        return

    media = calcular_media(nota1, nota2, nota3)
    print(f"A média final do aluno é: {media:.2f}")
if __name__ == "__main__":
    main()