# | ------------------------------------------------
# |                                                 
# |            ------- Arc Garden -------           
# |                                                 
# |         Projeto desenvolvido pela equipe        
# |         ARCEUS para o Challenge FIAP 2026       
# |                                                 
# | ------------------------------------------------

# -------------------- BIBLIOTECAS --------------------
import random
from bibliotecas import desenho, entrada

# -------------------- FUNCIONALIDADES DO MODO JOGO --------------------

# jogar.cadastrar_jogador_se_necessario()
# Procedimento que verifica se o perfil foi iniciado e solicita cadastro
# param: dados_jogador Dicionário contendo os atributos do jogador
# return: Não retorna nada
def cadastrar_jogador_se_necessario(dados_jogador: dict) -> None:
    if not dados_jogador["inicializado"]:
        desenho.limpar()
        desenho.titulo("CADASTRO DE JOGADOR")
        
        while True:
            username = input("NOME DE USUÁRIO: ").strip()
            if 0 < len(username) <= 25:
                break
            print("ERRO! O nome de usuário deve ter entre 1 e 25 caracteres.")

        while True:
            nome_jardim = input("NOME DO SEU JARDIM: ").strip().upper()
            if len(nome_jardim) > 0:
                break
            print("ERRO! O nome do jardim não pode ser vazio.")

        dados_jogador["username"] = username
        dados_jogador["nome_jardim"] = nome_jardim
        dados_jogador["inicializado"] = True
        print("\nCADASTRO REALIZADO COM SUCESSO!")
        desenho.espera_entrada()

# jogar.simular_missoes()
# Procedimento que exibe as missões disponíveis e adiciona pontos para o jogador
# param: dados_jogador Dicionário de atributos do jogador
# param: lista_missoes Lista das missões cadastradas no sistema
# return: Não retorna nada
def simular_missoes(dados_jogador: dict, lista_missoes: list) -> None:
    if len(lista_missoes) == 0:
        print("\nNENHUMA MISSÃO CADASTRADA NO SISTEMA!")
        desenho.espera_entrada()
        return

    while True:
        desenho.limpar()
        desenho.linha()
        desenho.titulo("SIMULAR MISSÕES")
        
        for idx, m in enumerate(lista_missoes, start=1):
            qtd_feita = dados_jogador["missoes_feitas"].get(m["nome"], 0)
            pts_str = f"{m['pts']} PTS"
            progresso_str = f"{qtd_feita}/{m['tempo_qtd']}X ({m['tempo']})"
            print(f"{idx:<2} | {m['nome']:26} | {m['dificuldade']:8} | {pts_str:7} | {progresso_str}")

        desenho.linha()
        print(" 0 | VOLTAR")
        desenho.linha()

        escolha = entrada.inteiro("\nEscolha a missão feita: ")

        if escolha == 0:
            break

        if 1 <= escolha <= len(lista_missoes):
            missao = lista_missoes[escolha - 1]
            qtd_feita = dados_jogador["missoes_feitas"].get(missao["nome"], 0)

            if qtd_feita >= missao["tempo_qtd"]:
                print("\nVOCÊ JÁ ATINGIU O LIMITE DESSA MISSÃO!")
                desenho.espera_entrada()
                continue

            confirmar = input(f"CONFIRMA A REALIZAÇÃO DE '{missao['nome']}'? (S/N): ").strip().upper()
            if confirmar == "S":
                dados_jogador["missoes_feitas"][missao["nome"]] = qtd_feita + 1
                dados_jogador["arc_score"] += missao["pts"]
                dados_jogador["arc_score_total"] += missao["pts"]
                
                print(f"\n+ {missao['pts']} ARC-SCORE ADICIONADOS! 💧")
                desenho.espera_entrada()
        else:
            print("OPÇÃO INVÁLIDA!")
            desenho.espera_entrada()

# jogar.ver_arc_score()
# Procedimento que exibe o saldo de Arc-Score do jogador e uma mensagem personalizada
# param: dados_jogador Dicionário contendo os dados do jogador
# return: Não retorna nada
def ver_arc_score(dados_jogador: dict) -> None:
    desenho.limpar()
    pts = dados_jogador["arc_score"]
    desenho.titulo(f"VOCÊ TEM {pts} ARC-SCORE 💧")
    
    if pts < 100:
        print("\nPOUCOS PONTOS! FAÇA MAIS MISSÕES!")
    elif pts < 300:
        print("\nVOCÊ ESTÁ INDO BEM!")
    else:
        print("\nARC-SCORE INSANO 🔥")
        
    desenho.espera_entrada()

# jogar.gerenciar_jardim()
# Procedimento que exibe as plantas do jogador e permite regálas
# param: dados_jogador Dicionário de atributos do jogador
# return: Não retorna nada
def gerenciar_jardim(dados_jogador: dict) -> None:
    while True:
        desenho.limpar()
        desenho.titulo(f"JARDIM: {dados_jogador['nome_jardim']}")
        print(f"ARC-SCORE DISPONÍVEL: {dados_jogador['arc_score']} 💧\n")

        if len(dados_jogador["plantas"]) == 0:
            print("SEU JARDIM ESTÁ VAZIO!")
            desenho.espera_entrada()
            break

        for idx, planta in enumerate(dados_jogador["plantas"], start=1):
            falta_xp = planta["xp_maximo"] - planta["xp_atual"]
            print(f"{idx}. {planta['nome']} | LV: {planta['level_planta']} (CATEGORIA: {planta['raridade']})")
            print(f"   XP: {planta['xp_atual']}/{planta['xp_maximo']} (Falta: {falta_xp} XP)")
            print(f"   DESCRIÇÃO: {planta['descricao']}\n")

        print("1 - Regar Planta (25💧)")
        print("0 - Voltar")
        
        opcao = input("\nEscolha: ").strip()
        if opcao == "0":
            break

        if opcao == "1":
            if dados_jogador["arc_score"] < 25:
                print("SÃO NECESSÁRIOS 25💧 PARA REGAR!")
                desenho.espera_entrada()
                continue

            num_planta = entrada.inteiro("Digite o número da planta que deseja regar: ")
            if 1 <= num_planta <= len(dados_jogador["plantas"]):
                p = dados_jogador["plantas"][num_planta - 1]

                if p["level_planta"] >= 5:
                    print(f"{p['nome']} JÁ ESTÁ NO NÍVEL MÁXIMO!")
                    desenho.espera_entrada()
                    continue

                dados_jogador["arc_score"] -= 25
                p["xp_atual"] += 25

                if p["xp_atual"] >= p["xp_maximo"]:
                    p["level_planta"] += 1
                    p["xp_atual"] = 0
                    print(f"\n🔥 {p['nome']} SUBIU PARA O NÍVEL {p['level_planta']}!")

                    if p["level_planta"] >= 5:
                        p["xp_atual"] = p["xp_maximo"]
                        p["premiada"] = True
                        print(f"✨ {p['nome']} ATINGIU O NÍVEL MÁXIMO!")

                print(f"VOCÊ REGOU {p['nome']} POR 25💧!")
                desenho.espera_entrada()
            else:
                print("PLANTA INVÁLIDA!")
                desenho.espera_entrada()

# jogar.abrir_pacote()
# Procedimento para compra de pacotes que gera mais plantas
# param: dados_jogador Dicionário contendo os dados do jogador
# param: lista_pacotes Lista de pacotes disponíveis na loja
# return: Não retorna nada
def abrir_pacote(dados_jogador: dict, lista_pacotes: list) -> None:
    if len(lista_pacotes) == 0:
        print("\nNENHUM PACOTE DISPONÍVEL NA LOJA!")
        desenho.espera_entrada()
        return

    while True:
        desenho.limpar()
        desenho.titulo("COMPRAR PACOTES")
        print(f"SEU ARC-SCORE: {dados_jogador['arc_score']} 💧\n")

        for idx, pacote in enumerate(lista_pacotes, start=1):
            print(f"{idx} - 📦 {pacote['nome']} ({pacote['preco']} 💧)")
        print("0 - VOLTAR")

        escolha = entrada.inteiro("\nEscolha o pacote: ")
        if escolha == 0:
            break

        if 1 <= escolha <= len(lista_pacotes):
            pacote = lista_pacotes[escolha - 1]

            if dados_jogador["arc_score"] < pacote["preco"]:
                print("\nPONTOS INSUFICIENTES!")
                desenho.espera_entrada()
                continue

            todas_plantas = pacote["plantas_comuns"] + pacote["plantas_raras"] + pacote["plantas_ultra_raras"]
            if len(todas_plantas) == 0:
                print("\nESTE PACOTE NÃO POSSUI PLANTAS CADASTRADAS!")
                desenho.espera_entrada()
                continue

            dados_jogador["arc_score"] -= pacote["preco"]
            tipo_sorteado = random.choice(todas_plantas)

            ja_possui = False
            for p in dados_jogador["plantas"]:
                if p["nome"] == tipo_sorteado["nome"]:
                    ja_possui = True
                    p["level_planta"] = min(p["level_planta"] + 2, 5)
                    print(f"\nVOCÊ JÁ POSSUI {tipo_sorteado['nome']}! AUMENTOU +2 NÍVEIS!")
                    break

            if not ja_possui:
                nova_planta = {
                    "planta_id": len(dados_jogador["plantas"]) + 1,
                    "raridade": tipo_sorteado["categoria"],
                    "level_planta": 1,
                    "premiada": False,
                    "nome": tipo_sorteado["nome"],
                    "xp_atual": 0,
                    "xp_maximo": tipo_sorteado["xp_maximo"],
                    "descricao": tipo_sorteado["descricao"]
                }
                dados_jogador["plantas"].append(nova_planta)
                print(f"\n🎉 VOCÊ CONSEGUIU A SEMENTE DE {tipo_sorteado['nome']}!")

            desenho.espera_entrada()

# jogar.ver_ranking()
# Procedimento que desenha a tabela com a classificação geral dos jogadores
# param: dados_jogador Dicionário contendo os dados do jogador
# return: Não retorna nada
def ver_ranking(dados_jogador: dict) -> None:
    desenho.limpar()
    desenho.titulo("RANKING DE JOGADORES")

    usuarios = [
        (dados_jogador["username"], dados_jogador["arc_score_total"]),
        ("PlatãO642", 50), ("Zeni_Reação", 200), ("AR1stótolo", 150),
        ("PETERBOT_", 140), ("Cyndaquil_Lover", 400), ("Machado33", 100),
        ("Wongyu<3", 220), ("Mibr_Aspas", 500), ("Sabugoso3333", 300)
    ]

    usuarios_ordenados = sorted(usuarios, key=lambda u: u[1], reverse=True)

    for i, (nome, pontos) in enumerate(usuarios_ordenados, start=1):
        if nome == dados_jogador["username"]:
            print(f"\033[1;32m#{i:<2} - {nome:<15} {pontos:>5} PTS💧\033[0m")
        else:
            print(f"#{i:<2} - {nome:<15} {pontos:>5} PTS💧")

    desenho.espera_entrada()