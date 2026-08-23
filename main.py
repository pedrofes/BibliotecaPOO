from biblioteca import Biblioteca
from livro import Livro
from usuario import Usuario

def cadastrar_livro():
    pass

def cadastrar_usuario():
    pass

def listar_todos_os_livros():
    pass

def listar_usuarios():
    pass

def realizar_emprestimo():
    pass

def realizar_devolucao():
    pass

def listar_livros_disponiveis():
    pass

def listar_livros_emprestados():
    pass

def buscar_livro_pelo_titulo():
    pass

def encerrar_o_programa():
    print('Programa encerrado.')
    
def menu():
    while True:
        print('===== SISTEMA DA BIBLIOTECA =====')
        print('1. Cadastrar livro')
        print('2. Cadastrar usuário')
        print('3. Listar todos os livros')
        print('4. Listar usuários')
        print('5. Realizar empréstimo')
        print('6. Realizar devolução')
        print('7. Listar livros disponíveis')
        print('8. Listar livros emprestados')
        print('9. Buscar livro pelo título')
        print('10. Encerrar o programa')
        try:
            opcao = int(input('Digite o número da opção que deseja selecionar: ').strip())
        except ValueError:
            print('Digite apenas números.')
            return
        if opcao == 1:
            cadastrar_livro()
        elif opcao == 2:
            cadastrar_usuario()
        elif opcao == 3:
            listar_todos_os_livros()
        elif opcao == 4:
            listar_usuarios()
        elif opcao == 5:
            realizar_emprestimo()
        elif opcao == 6:
            realizar_devolucao()
        elif opcao == 7:
            listar_livros_disponiveis()
        elif opcao == 8:
            listar_livros_emprestados()
        elif opcao == 9:
            buscar_livro_pelo_titulo()
        elif opcao == 10:
            encerrar_o_programa()
            break
        else:
            print('Digite apenas o número de uma das opções indicadas.')
            return

menu()