# Aviso:
#### O repositório dessa API foi movido para o Github privado da Freecel.


# API Freecel

Essa API foi desenvolvida para substituir a utilização das planilhas do BKO. Visando centralizar dados 
num banco SQL para facilitar trabalhos científicos/analíticos à longo prazo, além de diminuir a margem de
erro na geração dos rankings e métricas de desempenho da empresa. 

Também automatiza a consulta de quantidade de chamadas dos consultores através do Vivo Gestão.

Para fazer requisições à api, é necessário solicitar um token de acesso ao Victor ou Shady. Você pode 
alterar a função de autenticação para retornar sempre True caso você queira utilizar a API em ambiente 
de testes.


## Bibliotecas utilizadas:

- [Gunicorn](https://gunicorn.org/) - Servidor WSGI para aplicações web Python.
- [Uvicorn](https://www.uvicorn.org/) - Servidor ASGI para rodar aplicações FastAPI.
- [Pandas](https://pandas.pydata.org/) - Biblioteca para manipulação e análise de dados.
- [Python-dotenv](https://pypi.org/project/python-dotenv/) - Carrega variáveis de ambiente de um arquivo .env.
- [FastAPI](https://fastapi.tiangolo.com/) - Framework web moderno e de alta performance para construir APIs com Python.
- [pytz](https://pypi.org/project/pytz/) - Biblioteca para trabalhar com fusos horários em Python.
- [Requests](https://requests.readthedocs.io/) - Biblioteca para fazer requisições HTTP de maneira simples.
- [Pydantic](https://pydantic-docs.helpmanual.io/) - Biblioteca para validação de dados e criação de modelos de dados em Python.
- [cpf-cnpj-validate](https://pypi.org/project/cpf-cnpj-validate/) - Biblioteca para validação de CPF e CNPJ.
- [email-validator](https://pypi.org/project/email-validator/) - Biblioteca para validação de endereços de e-mail.
- [asyncpg](https://github.com/MagicStack/asyncpg) - Biblioteca para interação com bancos de dados PostgreSQL de forma assíncrona.
- [Pytest](https://docs.pytest.org/) - Framework de testes para Python.
- [python-multipart](https://andrew-d.github.io/python-multipart/) - Biblioteca para parsear dados multipart em requisições HTTP.
- [tabula-py](https://github.com/chezou/tabula-py) - Biblioteca para extrair tabelas de arquivos PDF.
- [PyPDF2](https://pypi.org/project/PyPDF2/) - Biblioteca para manipulação de arquivos PDF.
- [reportlab](https://www.reportlab.com/) - Biblioteca para gerar documentos PDF com Python.

### Pré-requisitos

- Python 3.7 ou superior
- Pip (gerenciador de pacotes do Python)

### Instalação e execução

1. Clone o repositório para sua máquina local:

```sh
git clone https://github.com/shadyrajab/freecel-api.git
cd abertura-conta-bancaria
```

2. Instale as dependências:
```sh
pip install -r requirements.txt
```

3. Executando a Aplicação
```sh
uvicorn main:app --reload
```

# Acessando a API e executando requests:

Você pode acessar o SWAGER da API através desse link: http://127.0.0.1:8000/docs


### Endpoints:

- **/consultores** - GET/POST/DELETE consultores ao banco de dados da Freecel;
- **/consultores/{nome_consultor}** - GET métricas de desempenho de um consultor e todas as suas vendas;
- **/vendas/fixa** - GET/POST/DELETE vendas da esteira fixa;
- **/vendas/movel** - GET/POST/DELETE vendas da esteira móvel;
- **/vendas/geral8** - GET vendas de todas as esteiras;
- **/planos** - GET/POST/PUT/DELETE planos da Vivo;

- **/chamadas** - GET chamadas de todos os consultores da Freecel. Automatiza o processo de ir ao Vivo Gestão fazer a contagem de ligações de cada consultor;

- **/stats/{esteira}** - GET métricas e rankings de vendas por esteira;

- **/simulacao** - POST faz análise de contrato de maneira automatizada. Lê todos os PDFS e transforma em planilhas, depois retorna as análises necessárias para o BKO;

- **/utils** - GET variáveis para serem utilizadas pelo front-end;


### Front-end:

O Front-end do projeto pode ser encontrado nesse link: https://github.com/shadyrajab/freecel-dashboard
