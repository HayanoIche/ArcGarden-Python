# | ------------------------------------------------
# |                                                 
# |            ------- Arc Garden -------           
# |                                                 
# |         Projeto desenvolvido pela equipe        
# |         ARCEUS para o Challenge FIAP 2026       
# |                                                 
# | ------------------------------------------------

# -------------------- BIBLIOTECAS --------------------
from bibliotecas import desenho, entrada
import menu

# -------------------- VARIÁVEIS DOS TIPOS DE PLANTAS --------------------

# Lista dos modelos/espécies pré-cadastrados no sistema (TipoPlanta)
lista_de_tipos_plantas = [
    {
        "nome": "CACTO",
        "nivel_inicial": 1,
        "nivel_maximo": 5,
        "categoria": "COMUM",
        "xp_atual": 0,
        "xp_maximo": 50,
        "descricao": "PLANTA RESISTENTE QUE ARMAZENA ÁGUA E SOBREVIVE EM CONDIÇÕES EXTREMAS."
    },
    {
        "nome": "SUCULENTA",
        "nivel_inicial": 1,
        "nivel_maximo": 5,
        "categoria": "COMUM",
        "xp_atual": 0,
        "xp_maximo": 50,
        "descricao": "PEQUENA E ADAPTÁVEL, PERFEITA PARA INICIANTES NO CULTIVO."
    },
    {
        "nome": "TULIPA",
        "nivel_inicial": 1,
        "nivel_maximo": 5,
        "categoria": "RARO",
        "xp_atual": 0,
        "xp_maximo": 100,
        "descricao": "FLOR ELEGANTE QUE FLORESCE EM CONDIÇÕES ESPECÍFICAS."
    },
    {
        "nome": "ÁRVORE ANTIGA",
        "nivel_inicial": 1,
        "nivel_maximo": 5,
        "categoria": "ULTRA RARO",
        "xp_atual": 0,
        "xp_maximo": 250,
        "descricao": "ÁRVORE PODEROSA COM CRESCIMENTO LENTO E GRANDE VALOR."
    }
]

# -------------------- FUNÇÕES DE CRUD --------------------

# plantas.adicionar()
# Procedimento que adiciona um novo modelo de TipoPlanta na lista
# :param planta_nome: Nome da espécie da planta
# :param planta_categoria: Categoria de raridade (COMUM, RARO, ULTRA RARO)
# :param planta_xp_maximo: Quantidade máxima de XP necessária para o nível
# :param planta_descricao: Texto descritivo sobre a espécie
# :return: Retorna True após adicionar com sucesso
def adicionar(planta_nome: str, planta_categoria: str, planta_xp_maximo: int, planta_descricao: str) -> bool:
    lista_de_tipos_plantas.append(
        {
            "nome": planta_nome,
            "nivel_inicial": 1,
            "nivel_maximo": 5,
            "categoria": planta_categoria,
            "xp_atual": 0,  
            "xp_maximo": planta_xp_maximo,
            "descricao": planta_descricao
        }
    )
    return True

# plantas.atualizar()
# Função que atualiza os dados de um TipoPlanta de acordo com a opção
# param planta: Dicionário contendo os dados do TipoPlanta
# param opcao: Opção de campo selecionada no menu de edição
# return: Retorna True se a edição for realizada com sucesso, False se não
def atualizar(planta: dict, opcao: str) -> bool:
    match opcao:
        case "1":
            novo_nome = input("NOVO NOME DO TIPO DE PLANTA: ").strip().upper()
            if novo_nome == "":
                print("ERRO! O NOME NÃO PODE FICAR VAZIO!")
                return False
            if pegar(novo_nome) is not None and novo_nome != planta["nome"]:
                print("ERRO! ESSE TIPO DE PLANTA JÁ EXISTE!")
                return False
            planta["nome"] = novo_nome

        case "2":
            menu.desenhar("Tipo da planta")
            escolha = input("Escolha: ")
            match escolha:
                case "1":
                    planta["categoria"] = "COMUM"
                case "2":
                    planta["categoria"] = "RARO"
                case "3":
                    planta["categoria"] = "ULTRA RARO"
                case _:
                    print("ERRO! OPÇÃO INVÁLIDA!")
                    return False

        case "3":
            while True:
                xp_maximo = entrada.inteiro("NOVO XP MÁXIMO: ")
                if xp_maximo <= 0:
                    print("ERRO! O XP MÁXIMO DEVE SER MAIOR QUE ZERO!")
                else:
                    planta["xp_maximo"] = xp_maximo
                    break

        case "4":
            nova_desc = input("NOVA DESCRIÇÃO: ").strip()
            if nova_desc == "":
                print("ERRO! A DESCRIÇÃO NÃO PODE FICAR VAZIA!")
                return False
            planta["descricao"] = nova_desc

        case _:
            return False

    return True

# plantas.pegar()
# Função que busca um TipoPlanta na lista pelo seu nome
# param planta_nome: Nome da espécie a ser buscada
# return: Retorna o dicionário do TipoPlanta ou None caso não encontre
def pegar(planta_nome: str) -> dict | None:
    for planta in lista_de_tipos_plantas:
        if planta.get("nome") == planta_nome:
            return planta
    return None

# plantas.remover()
# Função que remove um TipoPlanta da lista de espécies
# param planta_nome: Nome da espécie a ser removida
# return: Retorna True se for removido, False caso não encontre
def remover(planta_nome: str) -> bool:
    for num, item in enumerate(lista_de_tipos_plantas):
        if item.get("nome") == planta_nome:
            lista_de_tipos_plantas.pop(num)
            return True
    return False

# -------------------- TELAS E PROCEDIMENTOS DE GERENCIAMENTO --------------------

# plantas.criando()
# Procedimento de interface interativa para cadastro de novo TipoPlanta
# return: Não retorna nada
def criando() -> None:
    desenho.limpar()
    desenho.linha()
    print()
    desenho.titulo("CRIANDO TIPO DE PLANTA")

    while True:
        nome = input("NOME DO TIPO DE PLANTA: ").strip().upper()
        if nome == "":
            print("ERRO! O NOME NÃO PODE FICAR VAZIO!")
        elif pegar(nome) is not None:
            print("ERRO! ESSE TIPO DE PLANTA JÁ EXISTE!")
        else:
            break

    while True:
        menu.desenhar("Tipo da planta")
        escolha = input("Escolha a categoria: ")
        match escolha:
            case "1":
                categoria = "COMUM"
                break
            case "2":
                categoria = "RARO"
                break
            case "3":
                categoria = "ULTRA RARO"
                break
            case _:
                print("ERRO! OPÇÃO INVÁLIDA!")

    while True:
        xp_maximo = entrada.inteiro("XP MÁXIMO: ")
        if xp_maximo <= 0:
            print("ERRO! O XP MÁXIMO DEVE SER MAIOR QUE ZERO!")
        else:
            break

    descricao = input("DESCRIÇÃO: ").strip()
    adicionar(nome, categoria, xp_maximo, descricao)
    print(f"\nTIPO DE PLANTA '{nome}' CRIADO COM SUCESSO!")
    desenho.espera_entrada()

# plantas.atualizando()
# Procedimento de interface para alteração de Tipos de Plantas existentes
# return: Não retorna nada
def atualizando() -> None:
    desenho.limpar()
    desenho.linha()
    print()
    desenho.titulo("EDITANDO TIPOS DE PLANTAS")
    print()

    if len(lista_de_tipos_plantas) == 0:
        print("NENHUM TIPO DE PLANTA FOI CRIADO!")
        desenho.espera_entrada()
        return

    for num, planta in enumerate(lista_de_tipos_plantas):
        print(f"  {num + 1}. {planta['nome']}")

    print()

    while True:
        escolha = entrada.inteiro("QUAL DESEJA EDITAR: ")
        if 1 <= escolha <= len(lista_de_tipos_plantas):
            planta = lista_de_tipos_plantas[escolha - 1]
            break
        print("ERRO! ESSA OPÇÃO NÃO EXISTE!")

    while True:
        desenho.limpar()
        desenho.linha()
        print()
        desenho.titulo(f"EDITANDO: {planta['nome']}")
        print()

        menu.desenhar("Editando planta")
        escolha = input("ESCOLHA: ").strip()

        
        if escolha == "5":
            break

        resultado = atualizar(planta, escolha)
        if resultado:
            print("TIPO DE PLANTA ATUALIZADO!")
        desenho.espera_entrada()

# plantas.listar()
# Procedimento que exibe na tela todos os Tipos de Plantas e suas propriedades
# return: Não retorna nada
def listar() -> None:
    desenho.limpar()
    desenho.linha()
    print()
    desenho.titulo("TIPOS DE PLANTAS CADASTRADOS")
    print()

    if len(lista_de_tipos_plantas) == 0:
        print("NENHUM TIPO DE PLANTA CADASTRADO!")
    else:
        for num, planta in enumerate(lista_de_tipos_plantas):
            print(f"NOME.............: {planta['nome']}")
            print(f"NÍVEL INICIAL....: {planta['nivel_inicial']}")
            print(f"NÍVEL MÁXIMO.....: {planta['nivel_maximo']}")
            print(f"CATEGORIA........: {planta['categoria']}")
            print(f"XP INICIAL.......: {planta['xp_atual']}")
            print(f"XP MÁXIMO........: {planta['xp_maximo']}")
            print(f"DESCRIÇÃO........: {planta['descricao']}")
            print()
            desenho.linha()

    desenho.espera_entrada()

# plantas.excluindo()
# Procedimento de interface para exclusão de um TipoPlanta
# return: Não retorna nada
def excluindo() -> None:
    desenho.limpar()
    desenho.linha()
    print()
    desenho.titulo("EXCLUINDO TIPO DE PLANTA")

    if len(lista_de_tipos_plantas) == 0:
        print("\nNENHUM TIPO DE PLANTA CADASTRADO!")
        desenho.espera_entrada()
        return

    print()
    for num, planta in enumerate(lista_de_tipos_plantas):
        print(f"  {num + 1}. {planta['nome']}")

    print()

    while True:
        escolha = entrada.inteiro("QUAL DESEJA EXCLUIR: ")
        if 1 <= escolha <= len(lista_de_tipos_plantas):
            planta = lista_de_tipos_plantas[escolha - 1]

            print(f"\nTIPO SELECIONADO: {planta['nome']}")
            confirmar = input("DESEJA REALMENTE EXCLUIR? (S/N): ").upper().strip()

            if confirmar == "S":
                remover(planta["nome"])
                print(f"TIPO DE PLANTA {planta['nome']} EXCLUÍDO!")
                break
            elif confirmar == "N":
                print("EXCLUSÃO CANCELADA!")
                break
            else:
                print("ERRO! DIGITE S OU N!")
        else:
            print("ERRO! ESSA OPÇÃO NÃO EXISTE!")

    desenho.espera_entrada()