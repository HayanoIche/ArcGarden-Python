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

import csv, json

# arquivos.pegar_conteudo()
# Procedimento que desenha uma linha no terminal
# param path: O caminho do arquivo a ser lido
# return: Retorna todo o arquivo desejado
def pegar_conteudo(path: str) -> str:
    try:
        arquivo = open(path, "r", encoding="utf-8")
        conteudo = arquivo.read()
        arquivo.close()

        return conteudo
    except: 
        print(f"Erro! Arquivo ({path}) não encontrado!")

        return ""


# Arquivos CSV

'''
def grava_csv(caminho: str):
    with open(caminho, "a", newline="", encoding="utf-8") as arquivo:
        gravador = csv.writer(arquivo, delimiter=",")

        gravador.writerow(["Nome", "Idade", "Altura"])

        while(True):
            nome = input("Nome: ")

            if nome == "":
                break
            else:
                idade = int(input("Idade: "))
                altura = float(input("Altura: "))
                gravador.writerow([nome, idade, altura])

def ler_csv(caminho: str):
    with open(caminho, "r", newline="", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo, delimiter=",")

        for linha in leitor:
            print(linha)

        print(len(arquivo))
'''

# Arquivos json

'''
def grava_json():
    pessoas = []

    while(True):
        nome = input("Nome: ")
        if nome == "":
            break
        else:
            idade = int(input("Idade: "))
            altura = float(input("Altura: "))

            pessoa = {
                "nome": nome,
                "idade": idade,
                "altura": altura
            }

            pessoas.append(pessoa)

    with open("pessoas.json", "a", encoding="utf-8") as arquivo:
        pessoas = json.dump(pessoas, arquivo, indent=4)

def ler_json():
    pessoas = []

    with open("pessoas.json", "a", encoding="utf-8") as arquivo:
        pessoas = json.load(arquivo)

    for pessoas in pessoa:
        print("Nome: ", pessoa["nome"])
        print("Idade: ", pessoa["idade"])
        print("Altura: ", pessoa["idade"])

'''  