Exemplo de request usando Python

```py
from requests import request

url = 'https://freecelapi-b44da8eb3c50.herokuapp.com/vendas'
token = 'SEU_TOKEN'
headers = {
    'Authorization': f'Bearer {token}'
}
response = request("GET", url=url, headers=headers)
venda_1 = response.json()[0]
print(venda_1)
```
Resultado: 

```json
{
    'uf': 'DF', 
    'cnpj': '00.686.253/0001-60',
    'plano': 'PACOTE VOZ SIP', 
    'tipo': 'AVANÇADA', 
    'valor_do_plano': 409.0, 
    'quantidade_de_produtos': 1, 
    'valor_acumulado': 409.0, 
    'consultor': 'ANDRE DOS SANTOS', 
    'gestor': 'SOLON HORMIDAS CALDAS', 
    'revenda': 'FREECEL', 
    'faturamento': 'R$ 4800001,00 a R$ 20000000,00', 
    'colaboradores': '100 A 500 COLABORADORES', 
    'cod_cnae': '9411100', 
    'nome_cnae': 'Atividades de organizações associativas patronais e empresariais', 
    'data': '2023-01-01 00:00:00', 
    'id': 1, 
    'ano': 2023, 
    'mês': 'Janeiro'
}

```
