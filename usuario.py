class Usuario:

    def __init__(self, nome, cpf, email):
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.livros_emprestados = []

    def pegar_livro_emprestado(self, livro):

        if livro.disponivel:
            self.livros_emprestados.append(livro)
            livro.emprestar()
        else:
            print('Livro indisponível no momento para emprestar.')
            return

    def devolver_livro(self, livro):

        if livro in self.livros_emprestados:
            self.livros_emprestados.remove(livro)
            livro.devolver()
            print('Parabéns, você devolveu o livro à biblioteca.')
        else:
            print('O usuário não possui este livro emprestado.')

    def __str__(self):
        if self.livros_emprestados:
            livros_emprestados_deste_usuario = ', '.join(livro.titulo for livro in self.livros_emprestados)
        else:
            livros_emprestados_deste_usuario = 'Nenhum'
        return f'Usuário {self.nome} - CPF: {self.cpf} - E-mail: {self.email} - Livros emprestados: {len(self.livros_emprestados)} - Títulos: {livros_emprestados_deste_usuario}.'
