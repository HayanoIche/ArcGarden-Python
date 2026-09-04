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

# arquivos.pegar_conteudo()
# Procedimento que desenha uma linha no terminal
# :param path: O caminho do arquivo a ser lido
# :return: Retorna todo o arquivo desejado
def pegar_conteudo(path: str) -> str:
    try:
        # Lendo o conteúdo
        arquivo = open(path, "r", encoding="utf-8")
        conteudo = arquivo.read()
        arquivo.close()

        return conteudo
    except: # Caso não ache o arquivo
        print(f"Erro! Arquivo ({path}) não encontrado!")

        return ""
