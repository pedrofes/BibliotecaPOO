class Livro:

	def __init__(self,titulo, autor, ano_publicacao, edicao):
		self.titulo = titulo
		self.autor = autor
		self.ano_publicacao = ano_publicacao
		self.edicao = edicao
		self.disponivel = True

	def emprestar(self):
		self.disponivel = False

	def devolver(self):
			self.disponivel = True

	def __str__(self):
		return f'Título: {self.titulo} - Autor: {self.autor} - Ano de publicação: {self.ano_publicacao} - Edição: {self.edicao} - Disponível: {self.disponivel}.'