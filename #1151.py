
def fib(N, atual, anterior):
  if N <= 1:
    print (anterior)
  else:
    print (anterior, end=" ")
    fib(N-1, atual + anterior, atual)

def main(): 
  N = int(input("Informe um número: "))
  atual = 1
  anterior = 0
  fib(N, atual, anterior)

main()