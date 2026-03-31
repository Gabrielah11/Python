class No:
  def __init__(self, matricula, nome, idade):
    self.proximo = None
    self.nome = nome
    self.idade = idade
    self.matricula = matricula

  def mostrar_no(self):
    print("Matrícula:", self.matricula, "Nome: ", self.nome, "Idade: ", self.idade)
class ListaEncadeada:
  def __init__(self):
    self.primeiro = None


  def lista_vazia(self):
    return self.primeiro is None

  def mostrar_lista(self):
    if self.lista_vazia() is None:
      print("Lista Vazia")
      return None
    atual = self.primeiro
    while atual is not None:
      atual.mostrar_no()
      atual = atual.proximo

  def inserir_inicio(self, nome, idade, matricula):
    novo = No(nome, idade, matricula)
    novo.proximo = self.primeiro
    self.primeiro = novo

  def pesquisar(self, matricula):
    if self.lista_vazia():
      print("LISTA VAZIA")
      return None
    atual = self.primeiro
    while atual is not None and atual.matricula != matricula:
      atual = atual.proximo
    if atual is not None:
      print("Matrícula encontrada")
      atual.mostrar_no()
    else:
      print("Mátricula não encontrada")

  def incluir_fim(self, matricula, nome, idade):
    novo = No(matricula, nome, idade)
    if self.primeiro is None:
      self.primeiro = novo
      return 
    atual = self.primeiro
    while atual.proximo is not None:
      atual = atual.proximo
    atual.proximo = novo

  def excluir(self, matricula):
    if self.lista_vazia():
      print("Lista Vazia")
      return None
    atual = self.primeiro
    anterior = None
    while atual is not None and atual.matricula != matricula:
      anterior = atual
      atual = atual.proximo
    if atual is not None:
      if anterior is None: 
        self.primeiro = atual.proximo
      else:
        anterior.proximo = atual.proximo
        print("Matricula excluida")
    else:
      print("Matricula não encontrada")

  def solicitar_matricula(self, msg):
      return int(input(msg))

  def entrada_aluno(self):
      mat = int(input("Inserir Matrícula: "))
      nome = input("Inserir Nome: ")
      idade = int(input("Inserir Idade: "))
      return mat, nome, idade

def exibir_opcoes():
    print("\n" + "="*30)
    print("      SISTEMA ACADÊMICO")
    print("="*30)
    print("1. Cadastrar no Início")
    print("2. Cadastrar no Fim")
    print("3. Listar Todos")
    print("4. Buscar por Matrícula")
    print("5. Remover Aluno")
    print("0. Sair")

def iniciar_sistema(lista):
    opcao = ""

    while opcao != '0':
        exibir_opcoes()
        opcao = input("Opção: ")

        match opcao:
            case '1':
                m, n, i = lista.entrada_aluno()
                lista.inserir_inicio(m,n,i)
            case '2':
                m, n, i = lista.entrada_aluno()
                lista.incluir_fim(m, n, i)
            case '3':
                lista.mostrar_lista()
            case '4':
                m = lista.solicitar_matricula("Digite o número da matrícula: ")
                lista.pesquisar(m)
            case '5':
                m = lista.solicitar_matricula("Digite a matrícula a ser removida: ")
                lista.excluir(m)
            case '0':
                print("ENCERRANDO")
            case _:
                print("Opção inválida. Por favor, escolha uma opção válida (0-5).")

if __name__ == "__main__":
    lista = ListaEncadeada()
    iniciar_sistema(lista)