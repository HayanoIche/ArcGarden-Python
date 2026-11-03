# ArcGarden – Sistema de Gerenciamento de Plantas

## Sobre o projeto

O ArcGarden é um sistema desenvolvido em Python para auxiliar no gerenciamento de plantas, permitindo cadastrar, consultar, alterar e excluir registros.

## Funcionalidades

- Cadastro de plantas.
- Consulta das plantas cadastradas.
- Alteração dos dados das plantas.
- Exclusão de plantas.
- Integração com banco de dados Oracle.
- Consumo de API externa.
- Exportação e utilização de dados em JSON.

## Tecnologias utilizadas

- Python
- Oracle Database
- Biblioteca oracledb
- Pandas
- Requests
- JSON
- API REST

## Como executar

1. Instale o Python.
2. Na pasta principal do projeto, instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

3. Configure os dados de conexão com o Oracle no arquivo correspondente.
4. Entre na pasta `source/` e execute o arquivo `main.py`:

   ```bash
   cd source
   python main.py
   ```

## Estrutura do projeto

- `source/`: arquivos Python do sistema.
- `textos/`: arquivos de apoio e documentação.
- `Documento-Python.pdf`: documentação do projeto.

## Projeto acadêmico

Desenvolvido como parte da Sprint 4 do curso FIAP.