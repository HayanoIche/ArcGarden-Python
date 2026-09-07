# | ------------------------------------------------
# |                                                 
# |            ------- Arc Garden -------           
# |                                                 
# |         Projeto desenvolvido pela equipe        
# |         ARCEUS para o Challenge FIAP 2026       
# |                                                 
# | ------------------------------------------------

# |  Arquivo auxiliar com as funções das plantas

# -------------------- BIBLIOTECAS --------------------
from bibliotecas import desenho

# -------------------- VARIÁVEIS DAS PLANTAS --------------------

lista_de_plantas = list()

# -------------------- FUNÇÕES --------------------

# ----- CRUD -----
def adicionar(planta_nome: str) -> bool:
    global lista_de_plantas
    
    lista_de_plantas.append(
        {
            "nome": planta_nome
        }
    )
    
    return True

def atualizar(planta_nome: str) -> bool:
    global lista_de_plantas
    
    for num, item in enumerate(lista_de_plantas):
        if (item.get("nome") != None):
            if (item.get("nome") == planta_nome):
                novo_nome = input("NOVO NOME DA PLANTA: ")
                item["nome"] = novo_nome
                # Atualizar
                
                return True
    
    return False

def pegar(planta_nome: str) -> bool:
    global lista_de_plantas
    
    for num, item in enumerate(lista_de_plantas):
        if (item.get("nome") != None):
            if (item.get("nome") == planta_nome):
                return item
    
    return None

def remover(planta_nome: str):
    global lista_de_plantas
    
    for num, item in enumerate(lista_de_plantas):
        if (item.get("nome") != None):
            if (item.get("nome") == planta_nome):
                lista_de_plantas.pop(num)
                return True
    
    return False

def criando() -> None:
    desenho.limpar()
    desenho.linha()
    print()
    desenho.titulo("CRIANDO PLANTA")

    while True:
        nome = input("NOME DA PLANTA: ")

        if pegar(nome) != None:
            print("ERRO! ESSA PLANTA JÁ EXISTE!")
        else:
            adicionar(nome)
            print(f"PLANTA {nome} CRIADA!")
            break
    desenho.espera_entrada()

def atualizando() -> None:
    desenho.limpar()
    desenho.linha()
    print()
    desenho.titulo("EDITANDO PLANTAS")
    nome = input("QUAL PLANTA DESEJA EDITAR: ")
    resultado = atualizar(nome)
    if resultado:
        print("PLANTA ATUALIZADA!")
    else:
        print("ERRO! ESSA PLANTA NÃO EXISTE!")
    desenho.espera_entrada()

def listar() -> None:
    desenho.limpar()
    desenho.linha()
    print()
    desenho.titulo("PLANTAS CADASTRADAS")
    print()

    if len(lista_de_plantas) == 0:
        print("NENHUMA PLANTA FOI CRIADA!")

    else:
        for num, planta in enumerate(lista_de_plantas):
            print(f"  {num + 1}. {planta['nome']}")

    print()
    desenho.linha()
    desenho.espera_entrada()


def excluindo() -> None:

    desenho.limpar()
    desenho.linha()
    print()
    desenho.titulo("EXCLUINDO PLANTA")

    if len(lista_de_plantas) == 0:
        print()
        print("NENHUMA PLANTA CADASTRADA!")
        desenho.espera_entrada()
        return

    print()

    for num, planta in enumerate(lista_de_plantas):
        print(f"  {num + 1}. {planta['nome']}")

    print()

    while True:
        escolha = input("QUAL PLANTA DESEJA EXCLUIR: ")

        if escolha.isdigit():
            escolha = int(escolha)

            if escolha >= 1 and escolha <= len(lista_de_plantas):
                planta = lista_de_plantas[escolha - 1]

                print()
                print(f"PLANTA SELECIONADA: {planta['nome']}")
                confirmar = input("DESEJA REALMENTE EXCLUIR? (S/N): ").upper()

                if confirmar == "S":
                    remover(planta["nome"])
                    print(f"PLANTA {planta['nome']} EXCLUÍDA!")
                    break

                elif confirmar == "N":
                    print("EXCLUSÃO CANCELADA!")
                    break

                else:
                    print("ERRO! DIGITE S OU N!")

            else:
                print("ERRO! ESSA OPÇÃO NÃO EXISTE!")

        else:
            print("ERRO! DIGITE APENAS UM NÚMERO!")

    desenho.espera_entrada()