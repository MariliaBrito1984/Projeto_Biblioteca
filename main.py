# Definindo a lista vazia de livros e a variável global de ID

lista_livro = []
id_global = 1

print('Bem-Vendo ao controle de livros da Marilia Brito da Silva Evangelista')

# Função para cadastrar um novo livro

def cadastrar_livro(id):
        global id_global
        id_global += 1
        print('*' * 67)
        print('-' * 23, 'Menu Cadastra Livro', '-' * 22)
        print('id: ',id)
        nome = input("Digite o nome do livro: ")
        autor = input("Digite o nome do autor: ")
        editora = input("Digite o nome da editora: ")
        livro = {'id': id, 'nome': nome, 'autor': autor, 'editora': editora}
        lista_livro.append(livro)


# Função para consultar livros
def consultar_livro():
    print('*' * 66)
    print('-' * 22, 'Menu Consultar Livro', '-' * 22)
    global id_global
    while True:
        print('Escolha o opção desejada:')
        print('1 - Consultar Todos os livros')
        print('2 - Consultar livros por id')
        print('3 - Consultar livro(s) por autor')
        print('4 - Retornar...')
        opcao = int(input('>> '))
        print('-' * 17)

        if opcao == 1:
            for livro in lista_livro:
                print("id:", livro['id'])
                print("nome:", livro['nome'])
                print("autor:", livro['autor'])
                print("editora:", livro['editora'])
                print('-' * 17)

        elif opcao == 2:
            id_consulta = int(input("Digite o id do livro: "))
            for livro in lista_livro:
                if livro['id'] == id_consulta:
                    print("id:", livro['id'])
                    print("nome:", livro['nome'])
                    print("autor:", livro['autor'])
                    print("editora:", livro['editora'])
                    print('-' * 17)
                else:
                    print("Livro não encontrado.")

        elif opcao == 3:
            autor_consulta = input("Digite o nome do autor: ")
            for livro in lista_livro:
                if livro['autor'] == autor_consulta:
                    print('id:', livro['id'])
                    print('nome:', livro['nome'])
                    print('autor:', livro['autor'])
                    print('editora:', livro['editora'])
                    print('-' * 17)

        elif opcao == 4:
            return
        else:
            print('Opção inválida.')

    print('-' * 17)


# Função para remover os livros

def remover_livro():
    print('*' * 66)
    print('-' * 23, 'Menu Remover Livro', '-' * 23)
    id_remover = int(input('Digite o id do livro a ser removido: '))
    for livro in lista_livro:
        if livro['id'] == id_remover:
            lista_livro.remove(livro)
            print('Livro removido com sucesso!')
            return
    print('Livro não encontrado.')

# Função principal para o menu iniciar
def main():
    while True:
        print('*' * 69)
        print('-' * 27, 'Menu Principal','-' * 26)
        print('Escolha a opção desejada:')
        print('1 - Cadastrar Livro')
        print('2 - Consultar Livro(s)')
        print('3 - Renomear Livro')
        print('4 - Sair')
        opcao_menu = int(input('>> '))

        if opcao_menu == 1:
            cadastrar_livro(id_global)
        elif opcao_menu == 2:
            consultar_livro()
        elif opcao_menu == 3:
            remover_livro()
        elif opcao_menu == 4:
            print('Encerrando o programa...')
            break
        else:
            print('Opção inválida')
        continue


# Executando a função principal
opcao = main()
