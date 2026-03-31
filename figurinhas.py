def mdc(n1, n2):
    if n2 == 0:
        return n1
    else:
        return mdc(n2, n1 % n2)


N = int(input("Informe o número de casos de teste: "))

if N > 3000 or N < 1:
    print("Número de casos de teste inválido!")
    exit(1)

for i in range(N):

    vicente = int(input("Número de figurinhas de Vicente: "))
    ricardo = int(input("Número de figurinhas de Ricardo: "))

    if vicente > 1000 or vicente < 1:
        print("Vicente tem figurinhas demais ou não tem figurinhas")
        exit(1)

    if ricardo > 1000 or ricardo < 1:
        print("Ricardo tem figurinhas demais ou não tem figurinhas")
        exit(1)

    resultado = mdc(vicente, ricardo)

    print(f"O MDC de {vicente} e {ricardo} é {resultado}")