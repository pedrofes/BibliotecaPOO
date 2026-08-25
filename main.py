from biblioteca import Biblioteca
from livro import Livro
from usuario import Usuario

biblioteca = Biblioteca()

def cadastrar_livro():

    titulo = input('Digite o título do livro que deseja cadastrar: ').strip()

    if not titulo:
        print('Não deixe o título em branco.')
        return
    
    autor = input('Digite o autor do livro que está cadastrando: ').strip()

    if not autor:
        print('Digite um autor válido para o livro que está sendo cadastrado')
        return

    try:
        ano_publicacao = int(input('Digite o ano da publicação do livro: ').strip())
        if ano_publicacao <= 0:
            print('Digite um número maior do que zero para o ano de publicação')
            return
    except ValueError:
        print('Digite apenas números.')
        return
    try:
        edicao = int(input('Digite a edição do livro: ').strip())
        if edicao <= 0:
            print('Digite um número maior do que zero para cadastrar a edição do livro.')
            return   
    except ValueError:
        print('Digite apenas números para cadastrar a edição do livro.')
        return

    livro = Livro(titulo, autor, ano_publicacao, edicao)

    biblioteca.adicionar_livro(livro)

def cadastrar_usuario():


    nome = input('Digite o nome do usuário que deseja cadastrar: ').strip()
    if not nome:
        print('Digite um nome para o usuário que está sendo cadastrado.')
        return


    cpf = input('Digite o número do CPF com base no seguinte formato XXX.XXX.XXX-XX: ').strip()
    if not cpf:
        print('Digite um CPF para o cadastro.')
        return

    if len(cpf) != 14:
        print('Digite o CPF no formato XXX.XXX.XXX-XX.')
        return

    if cpf[3] != '.' or cpf[7] != '.' or cpf[11] != '-':
        print('Digite o CPF no formato XXX.XXX.XXX-XX.')
        return

    cpf_numeros = cpf.replace('.','').replace('-','')

    if not cpf_numeros.isdigit():
        print('Digite um CPF válido para o cadastro.')
        return

    email = input('Digite o e-mail do usuário: ').strip()
    if not email:
        print('Digite um e-mail para o cadastro')
        return

    if '@' not in email or '.' not in email:
        print('Digite um e-mail válido.')
        return

    usuario = Usuario(nome, cpf, email)

    biblioteca.cadastrar_usuario(usuario)

def listar_todos_os_livros():

    biblioteca.listar_livros()

def listar_usuarios():

    biblioteca.listar_usuarios()

def realizar_emprestimo():
    titulo = input('Digite o título do livro que será emprestado da biblioteca: ').strip()

    if not titulo:
        print('Título vazio. Digite um título para realizar o empréstimo.')
        return

    livro = biblioteca.buscar_livro(titulo) # buscando objeto a partir do título do livro

    if not livro:
        print('Nenhum livro com esse título cadastrado no sistema.')
        return

    cpf = input('Digite o CPF do usuário que pegará o livro emprestado: ').strip()

    if not cpf:
        print('Digite o CPF do usuário que realizará o empréstimo.')
        return

    usuario = biblioteca.buscar_usuario(cpf)

    if not usuario:
        print('Usuário não encontrado no cadastro.')
        return

    biblioteca.realizar_emprestimo(usuario, livro)
    print('Livro emprestado!')


def realizar_devolucao():

    titulo = input('Digite o título do livro que deseja devolver à biblioteca: ').strip()
    
    if not titulo:
        print('Título vazio. Digite um título para realizar a devolução.')
        return
    
    livro = biblioteca.buscar_livro(titulo) # buscando objeto a partir do título do livro

    if not livro:
        print('Nenhum livro com esse título cadastrado no sistema.')
        return

    cpf = input('Digite o CPF do usuário que está realizando a devolução do livro: ').strip()
    
    if not cpf:
        print('Digite o CPF do usuário que está devolvendo o livro.')
        return

    usuario = biblioteca.buscar_usuario(cpf)

    if not usuario:
        print('Usuário não encontrado no cadastro.')
        return

    biblioteca.realizar_devolucao(usuario, livro)

def listar_livros_disponiveis():
    biblioteca.listar_livros_disponiveis()

def listar_livros_emprestados():
    biblioteca.listar_livros_emprestados()

def buscar_livro_pelo_titulo():
    titulo = input('Digite o título do livro que deseja buscar no sistema: ').strip()

    if not titulo:
        print('Digite um título para realizar a busca.')
        return

    livro = biblioteca.buscar_livro(titulo)

    if livro:
        print('Livro encontrado!')
        print(livro)
    else:
        print('Livro não encontrado no sistema.')

def buscar_usuario_pelo_cpf():

    cpf = input('Digite o número do CPF com base no seguinte formato XXX.XXX.XXX-XX: ').strip()

    if not cpf:
        print('Digite um CPF para realizar a busca.')
        return
    
    if len(cpf) != 14:
        print('Digite o CPF no formato XXX.XXX.XXX-XX.')
        return
    
    if cpf[3] != '.' or cpf[7] != '.' or cpf[11] != '-':
        print('Digite o CPF no formato XXX.XXX.XXX-XX.')
        return
    
    cpf_numeros = cpf.replace('.','').replace('-','')

    if not cpf_numeros.isdigit():
        print('Digite um CPF válido para a busca.')
        return
    
    usuario = biblioteca.buscar_usuario(cpf)

    if usuario:
        print(usuario)
    else:
        print('Nenhum usuário encontrado no sistema com este CPF.')

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
        print('10. Buscar usuário pelo CPF')
        print('11. Encerrar o programa')
        try:
            opcao = int(input('Digite o número da opção que deseja selecionar: ').strip())
        except ValueError:
            print('Digite apenas números.')
            continue
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
            buscar_usuario_pelo_cpf()
        elif opcao == 11:
            encerrar_o_programa()
            break
        else:
            print('Digite apenas o número de uma das opções indicadas.')
            continue

menu()