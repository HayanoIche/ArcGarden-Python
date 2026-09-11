# | ------------------------------------------------
# |                                                 
# |            ------- Arc Garden -------           
# |                                                 
# |         Projeto desenvolvido pela equipe        
# |         ARCEUS para o Challenge FIAP 2026       
# |                                                 
# | ------------------------------------------------
 
# |  Arquivo auxiliar com as funções das missões

# -------------------- BIBLIOTECAS --------------------
import menu
from bibliotecas import desenho, entrada

# -------------------- VARIÁVEIS DAS MISSÕES --------------------

# Lista das missões pré-cadastradas no sistema
lista_de_missoes = [
    {
        "nome": "BANHO CURTO (ATÉ 5 MIN)",
        "dificuldade": "MÉDIO",
        "pts": 50,
        "tempo_qtd": 1,
        "tempo": "DIA"
    },
    {
        "nome": "DESLIGAR DA TOMADA",
        "dificuldade": "FÁCIL",
        "pts": 25,
        "tempo_qtd": 2,
        "tempo": "DIA"
    },
    {
        "nome": "CAPTAR ÁGUA DA CHUVA",
        "dificuldade": "DIFÍCIL",
        "pts": 90,
        "tempo_qtd": 1,
        "tempo": "SEMANA"
    },
    {
        "nome": "PLANTAR ÁRVORE REAL",
        "dificuldade": "ESPECIAL",
        "pts": 150,
        "tempo_qtd": 1,
        "tempo": "MÊS"
    }
]

# -------------------- FUNÇÕES DE CRUD --------------------

# missoes.adicionar()
# Procedimento que adiciona uma nova missão na lista global
# param missao_nome: Nome da missão
# param missao_dificuldade: Grau de dificuldade (FÁCIL, MÉDIO, DIFÍCIL, ESPECIAL)
# param missao_pts: Pontuação fornecida ao concluir a missão
# param missao_tempo_qtd: Quantidade limite de vezes que pode ser feita
# param missao_tempo: Unidade de tempo da limitação (DIA, SEMANA, MÊS)
# return: Retorna True após adicionar com sucesso
def adicionar(missao_nome: str, missao_dificuldade: str, missao_pts: int, missao_tempo_qtd: int, missao_tempo: str) -> bool:
    lista_de_missoes.append(
        {
            "nome": missao_nome,
            "dificuldade": missao_dificuldade,
            "pts": missao_pts,
            "tempo_qtd": missao_tempo_qtd,
            "tempo": missao_tempo
        }
    )
    return True

# missoes.pegar()
# Função que busca uma missão na lista pelo nome
# param: missao_nome Nome da missão
# return: Retorna o dicionário da missão ou None se não encontrar
def pegar(missao_nome: str) -> dict | None:
    for missao in lista_de_missoes:
        if missao.get("nome") == missao_nome:
            return missao
    return None

# missoes.remover()
# Função que remove uma missão da lista global
# param: missao_nome Nome da missão a ser removida
# return Retorna True se for removida com sucesso, False caso contrário
def remover(missao_nome: str) -> bool:
    for num, missao in enumerate(lista_de_missoes):
        if missao.get("nome") == missao_nome:
            lista_de_missoes.pop(num)
            return True
    return False

# missoes.atualizar()
# Função que edita um campo específico de uma missão selecionada
# param: missao Dicionário contendo os dados da missão
# param: opcao. Opção de campo para edição
# return: Retorna True em sucesso de alteração, False em insucesso
def atualizar(missao: dict, opcao: str) -> bool:
    match opcao:
        case "1":
            novo_nome = input("NOVO NOME DA MISSÃO: ").strip().upper()
            if novo_nome == "":
                print("ERRO! O NOME NÃO PODE FICAR VAZIO!")
                return False
            if pegar(novo_nome) is not None and novo_nome != missao["nome"]:
                print("ERRO! ESSA MISSÃO JÁ EXISTE!")
                return False
            missao["nome"] = novo_nome

        case "2":
            menu.desenhar("Dificuldade da missao")
            escolha = input("Escolha: ")
            match escolha:
                case "1":
                    missao["dificuldade"] = "FÁCIL"
                case "2":
                    missao["dificuldade"] = "MÉDIO"
                case "3":
                    missao["dificuldade"] = "DIFÍCIL"
                case "4":
                    missao["dificuldade"] = "ESPECIAL"
                case _:
                    print("ERRO! OPÇÃO INVÁLIDA!")
                    return False

        case "3":
            while True:
                pts = entrada.inteiro("NOVOS PONTOS: ")
                if pts < 0:
                    print("ERRO! OS PONTOS NÃO PODEM SER NEGATIVOS!")
                else:
                    missao["pts"] = pts
                    break

        case "4":
            while True:
                tempo_qtd = entrada.inteiro("NOVA QUANTIDADE DE TEMPO: ")
                if tempo_qtd <= 0:
                    print("ERRO! A QUANTIDADE DE TEMPO DEVE SER MAIOR QUE ZERO!")
                else:
                    missao["tempo_qtd"] = tempo_qtd
                    break

        case "5":
            menu.desenhar("Tipo de tempo")
            escolha = input("Escolha: ")
            match escolha:
                case "1":
                    missao["tempo"] = "DIA"
                case "2":
                    missao["tempo"] = "SEMANA"
                case "3":
                    missao["tempo"] = "MÊS"
                case _:
                    print("ERRO! OPÇÃO INVÁLIDA!")
                    return False

        case _:
            return False

    return True

# -------------------- TELAS E PROCEDIMENTOS DE GERENCIAMENTO --------------------

# missoes.criando()
# Procedimento de interface para cadastro de novas missões
# return: Não retorna nada
def criando() -> None:
    desenho.limpar()
    desenho.linha()
    print()
    desenho.titulo("CRIANDO MISSÃO")

    while True:
        nome = input("NOME DA MISSÃO: ").strip().upper()
        if nome == "":
            print("ERRO! O NOME NÃO PODE FICAR VAZIO!")
        elif pegar(nome) is not None:
            print("ERRO! ESSA MISSÃO JÁ EXISTE!")
        else:
            break

    while True:
        menu.desenhar("Dificuldade da missao")
        escolha = input("Escolha: ")
        match escolha:
            case "1":
                dificuldade = "FÁCIL"
                break
            case "2":
                dificuldade = "MÉDIO"
                break
            case "3":
                dificuldade = "DIFÍCIL"
                break
            case "4":
                dificuldade = "ESPECIAL"
                break
            case _:
                print("ERRO! OPÇÃO INVÁLIDA!")

    while True:
        pts = entrada.inteiro("PONTOS DA MISSÃO: ")
        if pts < 0:
            print("ERRO! OS PONTOS NÃO PODEM SER NEGATIVOS!")
        else:
            break

    while True:
        menu.desenhar("Tipo de tempo")
        escolha = input("Escolha: ")
        match escolha:
            case "1":
                tempo = "DIA"
                break
            case "2":
                tempo = "SEMANA"
                break
            case "3":
                tempo = "MÊS"
                break
            case _:
                print("ERRO! OPÇÃO INVÁLIDA!")

    while True:
        tempo_qtd = entrada.inteiro("QUANTIDADE DE TEMPO: ")
        if tempo_qtd <= 0:
            print("ERRO! A QUANTIDADE DE TEMPO DEVE SER MAIOR QUE ZERO!")
        else:
            break

    adicionar(nome, dificuldade, pts, tempo_qtd, tempo)
    print(f"MISSÃO {nome} CRIADA!")
    desenho.espera_entrada()

# missoes.atualizando()
# Procedimento de interface para seleção e edição de missões
# return: Não retorna nada
def atualizando() -> None:
    desenho.limpar()
    desenho.linha()
    print()
    desenho.titulo("EDITANDO MISSÕES")
    print()

    if len(lista_de_missoes) == 0:
        print("NENHUMA MISSÃO FOI CRIADA!")
        desenho.espera_entrada()
        return

    for num, missao in enumerate(lista_de_missoes):
        print(f"  {num + 1}. {missao['nome']}")

    print()

    while True:
        escolha = entrada.inteiro("QUAL MISSÃO DESEJA EDITAR: ")
        if 1 <= escolha <= len(lista_de_missoes):
            missao = lista_de_missoes[escolha - 1]
            break
        print("ERRO! ESSA OPÇÃO NÃO EXISTE!")

    while True:
        desenho.limpar()
        desenho.linha()
        print()
        desenho.titulo(f"EDITANDO: {missao['nome']}")
        print()

        menu.desenhar("Editando missão")
        escolha = input("ESCOLHA: ")

        if escolha == "6":
            break

        resultado = atualizar(missao, escolha)
        if resultado:
            print("MISSÃO ATUALIZADA!")

        desenho.espera_entrada()

    desenho.espera_entrada()

# missoes.excluindo()
# Procedimento de interface para exclusão de missões
# return: Não retorna nada.
def excluindo() -> None:
    desenho.limpar()
    desenho.linha()
    print()
    desenho.titulo("EXCLUINDO MISSÃO")

    if len(lista_de_missoes) == 0:
        print("\nNENHUMA MISSÃO CADASTRADA!")
        desenho.espera_entrada()
        return

    print()
    for num, missao in enumerate(lista_de_missoes):
        print(f"  {num + 1}. {missao['nome']}")

    print()

    while True:
        escolha = entrada.inteiro("QUAL MISSÃO DESEJA EXCLUIR: ")
        if 1 <= escolha <= len(lista_de_missoes):
            missao = lista_de_missoes[escolha - 1]

            print(f"\nMISSÃO SELECIONADA: {missao['nome']}")
            confirmar = input("DESEJA REALMENTE EXCLUIR? (S/N): ").upper().strip()

            if confirmar == "S":
                remover(missao["nome"])
                print(f"MISSÃO {missao['nome']} EXCLUÍDA!")
                break
            elif confirmar == "N":
                print("EXCLUSÃO CANCELADA!")
                break
            else:
                print("ERRO! DIGITE S OU N!")
        else:
            print("ERRO! ESSA OPÇÃO NÃO EXISTE!")

    desenho.espera_entrada()

# missoes.listar()
# Procedimento que desenha a tabela formatada com todas as missões
# return: Não retorna nada
def listar() -> None:
    desenho.limpar()
    desenho.titulo("MISSÕES")
    
    if len(lista_de_missoes) == 0:
        print("NENHUMA MISSÃO FOI CRIADA!")
    else:
        for num, missao in enumerate(lista_de_missoes, start=1):
            pts_str = f"{missao['pts']} PTS"
            tempo_str = f"{missao['tempo_qtd']}X/{missao['tempo']}"
            print(f"{num:<2} | {missao['nome']:26} | {missao['dificuldade']:8} | {pts_str:7} | {tempo_str}")

    desenho.linha()
    desenho.espera_entrada()