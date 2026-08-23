class Biblioteca:

    def __init__(self):
        self.usuarios_cadastrados = []
        self.todos_os_livros = []

    def adicionar_livro(self, livro):

        if livro in self.todos_os_livros:
            print('Este livro já está cadastrado na biblioteca.')
            return

        self.todos_os_livros.append(livro)
        print('Livro cadastrado com sucesso!')

    def cadastrar_usuario(self, usuario):

        for usuario_cadastrado in self.usuarios_cadastrados:

            if usuario_cadastrado.cpf == usuario.cpf:
                print('CPF já cadastrado para outro usuário.')
                return

            if usuario_cadastrado.email == usuario.email:
                print('E-mail já cadastrado para outro usuário.')
                return

        self.usuarios_cadastrados.append(usuario)
        print('Usuário cadastrado com sucesso!')

    def listar_livros(self):

        if not self.todos_os_livros:
            print('Nenhum livro cadastrado no sistema da biblioteca até o momento.')
            return

        print('Estes são todos os livros cadastrados na biblioteca no momento.')

        for livro in self.todos_os_livros:
            print(livro)

    def listar_usuarios(self):

        if not self.usuarios_cadastrados:
            print('Nenhum usuário cadastrado no sistema da biblioteca no momento.')
            return

        print('Estes são todos os usuários cadastrados no sistema da biblioteca no momento.')

        for usuario in self.usuarios_cadastrados:
            print(usuario)

    def realizar_emprestimo(self, usuario, livro):

        if usuario not in self.usuarios_cadastrados:
            print('Usuário não cadastrado no sistema da biblioteca.')
            return

        if livro not in self.todos_os_livros:
            print('Livro não cadastrado no sistema da biblioteca.')
            return

        usuario.pegar_livro_emprestado(livro)

    def realizar_devolucao(self, usuario, livro):

        if usuario not in self.usuarios_cadastrados:
            print('Usuário não cadastrado no sistema da biblioteca.')
            return

        if livro not in self.todos_os_livros:
            print('Livro não cadastrado no sistema da biblioteca.')
            return

        usuario.devolver_livro(livro)

    def listar_livros_disponiveis(self):

        livro_disponiveil_para_aluguel = False

        if not self.todos_os_livros:
            print('Nenhum livro cadastrado no sistema.')
            return

        for livro in self.todos_os_livros:
            if livro.disponivel:
                livro_disponivel_para_aluguel = True
                print(livro)

        if not livro_disponivel_para_aluguel:
            print('Todos os livros estão emprestados no momento.')
            return

    def listar_livros_emprestados(self):

        livro_emprestado_encontrado = False

        if not self.todos_os_livros:
            print('Nenhum livro cadastrado no sistema.')
            return

        for livro in self.todos_os_livros:
            if not livro.disponivel:
                livro_emprestado_encontrado = True
                print(livro)

        if not livro_emprestado_encontrado:
            print('Todos os livros estão disponíveis para empréstimo no momento.')
            return

    def buscar_livro(self, titulo):

        for livro in self.todos_os_livros:
            if livro.titulo == titulo:
                print('Livro localizado:')
                return livro

        return None
