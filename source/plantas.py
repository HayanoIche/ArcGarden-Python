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

# -------------------- VARIÁVEIS DAS PLANTAS --------------------

lista_de_plantas = list()

# -------------------- FUNÇÕES --------------------

# ----- CRUD -----
def adicionar(planta_nome: str) -> bool:
    global lista_de_plantas
    
    lista_de_plantas.append(
        {
            "NOME": planta_nome
        }
    )
    
    return True

def atualizar(planta_nome: str) -> bool:
    global lista_de_plantas
    
    for num, item in enumerate(lista_de_plantas):
        if (item.get("nome") != None):
            if (item.get("nome") == planta_nome):

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