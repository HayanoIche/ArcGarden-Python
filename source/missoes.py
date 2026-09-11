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
# Procedimento que adiciona uma nova missão na lista
# param: l Lista de missões
# param: n Nome da missão
# param: d Grau de dificuldade (FÁCIL, MÉDIO, DIFÍCIL, ESPECIAL)
# param: p Pontuação fornecida ao concluir a missão
# param: t_q Quantidade limite de vezes que pode ser feita
# param: t Unidade de tempo da limitação (DIA, SEMANA, MÊS)
# return: Retorna True após adicionar com sucesso
def adicionar(l: list, n: str, d: str, p: int, t_q: int, t: str) -> bool:
    try:
        nova_missao = {
            "nome": n,
            "dificuldade": d,
            "pts": p,
            "tempo_qtd": t_q,
            "tempo": t
        }
        l.append(nova_missao)
    except Exception as err:
        print(f"Ops, erro ao tentar criar a missão: {err}")
        return False
    else:
        return True
    finally:
        print("Registro finalizado.")

# missoes.pegar()
# Função que busca uma missão na lista pelo nome
# param: l Lista de missões
# param: n Nome da missão
# return: Retorna o dicionário da missão ou None se não encontrar
def pegar(l: list, n: str) -> dict | None:
    try:
        for m in l:
            if m.get("nome") == n:
                return m
    except Exception as err:
        print(f"Erro ao procurar essa missão: {err}")
    finally:
        print("Busca finalizada.")
    return None

# missoes.remover()
# Função que remove uma missão da lista
# param: l Lista de missões
# param: n Nome da missão a ser removida
# return: Retorna True se for removida com sucesso, False caso contrário
def remover(l: list, n: str) -> bool:
    sucesso = False
    try:
        for num, m in enumerate(l):
            if m.get("nome") == n:
                l.pop(num)
                sucesso = True
                break
    except Exception as err:
        print(f"Não deu para apagar a missão: {err}")
        return False
    else:
        return sucesso
    finally:
        print("Remoção finalizada.")

# missoes.atualizar()
# Função que edita um campo específico de uma missão selecionada
# param: m Dicionário contendo os dados da missão
# param: op Opção de campo para edição
# param: l Lista de missões
# return: Retorna True em sucesso de alteração, False em insucesso
def atualizar(m: dict, op: str, l: list) -> bool:
    alterado = False
    try:
        match op:
            case "1":
                novo_nome = input("NOVO NOME DA MISSÃO: ").strip().upper()
                if novo_nome == "":
                    print("ERRO! O NOME NÃO PODE FICAR VAZIO!")
                    return False
                if pegar(l, novo_nome) is not None and novo_nome != m["nome"]:
                    print("ERRO! ESSA MISSÃO JÁ EXISTE!")
                    return False
                m["nome"] = novo_nome
                alterado = True

            case "2":
                menu.desenhar("Dificuldade da missao")
                escolha = input("Escolha: ")
                match escolha:
                    case "1":
                        m["dificuldade"] = "FÁCIL"
                        alterado = True
                    case "2":
                        m["dificuldade"] = "MÉDIO"
                        alterado = True
                    case "3":
                        m["dificuldade"] = "DIFÍCIL"
                        alterado = True
                    case "4":
                        m["dificuldade"] = "ESPECIAL"
                        alterado = True
                    case _:
                        print("ERRO! OPÇÃO INVÁLIDA!")
                        return False

            case "3":
                while True:
                    pts = entrada.inteiro("NOVOS PONTOS: ")
                    if pts < 0:
                        print("ERRO! OS PONTOS NÃO PODEM SER NEGATIVOS!")
                    else:
                        m["pts"] = pts
                        alterado = True
                        break

            case "4":
                while True:
                    tempo_qtd = entrada.inteiro("NOVA QUANTIDADE DE TEMPO: ")
                    if tempo_qtd <= 0:
                        print("ERRO! A QUANTIDADE DE TEMPO DEVE SER MAIOR QUE ZERO!")
                    else:
                        m["tempo_qtd"] = tempo_qtd
                        alterado = True
                        break

            case "5":
                menu.desenhar("Tipo de tempo")
                escolha = input("Escolha: ")
                match escolha:
                    case "1":
                        m["tempo"] = "DIA"
                        alterado = True
                    case "2":
                        m["tempo"] = "SEMANA"
                        alterado = True
                    case "3":
                        m["tempo"] = "MÊS"
                        alterado = True
                    case _:
                        print("ERRO! OPÇÃO INVÁLIDA!")
                        return False

            case _:
                return False
    except Exception as err:
        print(f"Erro ao mudar os dados da missão: {err}")
        return False
    else:
        return alterado
    finally:
        print("Edição finalizada.")

# -------------------- TELAS E PROCEDIMENTOS DE GERENCIAMENTO --------------------

# missoes.criando()
# Procedimento de interface para cadastro de novas missões
# param: l Lista de missões
# return: Não retorna nada
def criando(l: list) -> None:
    desenho.limpar()
    desenho.linha()
    print()
    desenho.titulo("CRIANDO MISSÃO")

    while True:
        nome = input("NOME DA MISSÃO: ").strip().upper()
        if nome == "":
            print("ERRO! O NOME NÃO PODE FICAR VAZIO!")
        elif pegar(l, nome) is not None:
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

    if adicionar(l, nome, dificuldade, pts, tempo_qtd, tempo):
        print(f"MISSÃO {nome} CRIADA!")
    desenho.espera_entrada()

# missoes.atualizando()
# Procedimento de interface para seleção e edição de missões
# param: l Lista de missões
# return: Não retorna nada
def atualizando(l: list) -> None:
    desenho.limpar()
    desenho.linha()
    print()
    desenho.titulo("EDITANDO MISSÕES")
    print()

    if len(l) == 0:
        print("NENHUMA MISSÃO FOI CRIADA!")
        desenho.espera_entrada()
        return

    for num, m in enumerate(l):
        print(f"  {num + 1}. {m['nome']}")

    print()

    while True:
        escolha = entrada.inteiro("QUAL MISSÃO DESEJA EDITAR: ")
        if 1 <= escolha <= len(l):
            missao = l[escolha - 1]
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

        resultado = atualizar(missao, escolha, l)
        if resultado:
            print("MISSÃO ATUALIZADA!")

        desenho.espera_entrada()

    desenho.espera_entrada()

# missoes.excluindo()
# Procedimento de interface para exclusão de missões
# param: l Lista de missões
# return: Não retorna nada
def excluindo(l: list) -> None:
    desenho.limpar()
    desenho.linha()
    print()
    desenho.titulo("EXCLUINDO MISSÃO")

    if len(l) == 0:
        print("\nNENHUMA MISSÃO CADASTRADA!")
        desenho.espera_entrada()
        return

    print()
    for num, m in enumerate(l):
        print(f"  {num + 1}. {m['nome']}")

    print()

    while True:
        escolha = entrada.inteiro("QUAL MISSÃO DESEJA EXCLUIR: ")
        if 1 <= escolha <= len(l):
            missao = l[escolha - 1]

            print(f"\nMISSÃO SELECIONADA: {missao['nome']}")
            confirmar = input("DESEJA REALMENTE EXCLUIR? (S/N): ").upper().strip()

            if confirmar == "S":
                if remover(l, missao["nome"]):
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
# param: l Lista de missões
# return: Não retorna nada
def listar(l: list) -> None:
    desenho.limpar()
    desenho.titulo("MISSÕES")
    
    if len(l) == 0:
        print("NENHUMA MISSÃO FOI CRIADA!")
    else:
        for num, m in enumerate(l, start=1):
            pts_str = f"{m['pts']} PTS"
            tempo_str = f"{m['tempo_qtd']}X/{m['tempo']}"
            print(f"{num:<2} | {m['nome']:26} | {m['dificuldade']:8} | {pts_str:7} | {tempo_str}")

    desenho.linha()
    desenho.espera_entrada()