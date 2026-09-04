# | ------------------------------------------------
# |                                                 
# |            ------- Arc Garden -------           
# |                                                 
# |         Projeto desenvolvido pela equipe        
# |         ARCEUS para o Challenge FIAP 2026       
# |                                                 
# | ------------------------------------------------
 
# |  Biblioteca para ler arquivos
# |  desenvolvida por Matheus Vidal
# |  e Igor Hayano

def ler_completo(path: str) -> str:
    arquivo = open(path, "r", encoding="utf-8")
    conteudo = arquivo.read()
    arquivo.close()
    return conteudo
