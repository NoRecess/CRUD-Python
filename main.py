listaPecas = []


# Começo da função cadastrarPeca

def cadastrarPeca(registroPeca):
    print("O código do produto cadastrado é: {} ".format(registroPeca))
    nome = input("Digite o produto que deseja cadastrar: ")
    fabricante = input("Digite o nome do fabricante: ")
    valorPeca = input("Digite o valor do produto: ")
    dicionarioPeca = {'cod': registroPeca,
                      'nome': nome,
                      'fabricante': fabricante,
                      'valor': valorPeca}

    listaPecas.append(dicionarioPeca.copy())


# Fim da função cadastrarPeca


# Começo da função consultarPeca
def consultarPeca():
    while True:
        try:
            print("---* Consultar peças *---")
            opConsultar = int(input("Entre com a opção desejada:\n"
                                    "1 - Consultar todas as peças\n"
                                    "2 - Consultar por código\n"
                                    "3 - Consultar por fabricante\n"
                                    "4 - Retornar.\n"
                                    ">>"))
            if opConsultar == 1:
                print("Peças cadastradas:")
                for peca in listaPecas:
                    for key, value in peca.items():  # Seleciona cada dicionário da ListaPecas.
                        print("{} : {}".format(key, value))  # Seleciona cada conjunto chave/valor do dicionário.
            elif opConsultar == 2:
                print("Consultar por código:")
                codigo = int(input("Digite o código do produto: "))
                for peca in listaPecas:
                    if peca['cod'] == codigo:
                        for key, value in peca.items():
                            print("{} : {}".format(key, value))
            elif opConsultar == 3:
                print("Consultar por fabricante:")
                fabricante = input("Digite o nome do fabricante: ")
                for peca in listaPecas:
                    if peca['fabricante'] == fabricante:
                        for key, value in peca.items():
                            print("{} : {}".format(key, value))
            elif opConsultar == 4:
                break
            else:
                print("Opção inválida!")
                continue
        except ValueError:
            print("Opção inválida!")
            continue


# Fim da função consultarPeca

# Começo da função removerPeca
def removerPeca():
    print("Remover peça:")
    remover = int(input("Digite o código do produto que deseja remover: "))
    for peca in listaPecas:
        if peca['cod'] == remover:
            listaPecas.remove(peca)


# Fim da função removerPeca

# Começo função Main
print("Bem vindo ao programa de Guilherme Machado Sperb")  # RU:4095371
registro = 0
while True:
    try:
        opcao = int(input("Digite a opção desejada: \n"
                          "1 - Cadastrar Peça\n"
                          "2 - Consultar Peça\n"
                          "3 - Remover Peça\n"
                          "4 - Sair"
                          "\n>>"))
        if opcao == 1:
            registro = registro + 1
            cadastrarPeca(registro)
        elif opcao == 2:
            consultarPeca()
        elif opcao == 3:
            removerPeca()
        elif opcao == 4:
            print("Programa finalizado!")  # Finaliza o programa.
            break
        else:
            print("Opção não encontrada no menu!")
            continue
    except ValueError:
        print("Valor não reconhecido, digite novamente.")
        continue

# Fim função Main
