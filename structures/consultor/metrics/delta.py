from database.objects import meses

class DeltaMetrics:
    def __init__(self, dataframe):
        self.dataframe = dataframe

    def __get_delta_receita_ou_quantidade_mensal__(self, ano: int, mes: str, key: str) -> int:

        """
            Função privada, retorna o valor do parâmetro ``delta`` para a função ``col.metric`` do streamlit

            O ``delta_receita_ou_quantidade_mensal`` é a diferença entre a receita ou quantidade de vendas 
            do mês referência  comparado com a receita ou quantidade do mês passado.

            Parâmetros
            ---------

            ano : int
            
                O ano atual que servirá como referência para o ``delta``

            mes : str

                O mês atual que servirá como referência para o ``delta`` 
            
            key : str

                O nome da coluna que deseja calcular o delta. Deve ser ``RECEITA`` ou ``QUANTIDADE``

        """

        media_atual, media_mes_passado = '', ''

        # Retorna o primeiro ano que o consultor realizou uma venda
        primeiro_ano = min(self.years)

        # A função irá retornar 0 caso não haja venda anterior à do mês e ano referência.
        if ano == primeiro_ano and mes == 'Janeiro':
            return 0 
        
        # Se o mês referência for o mês de ``Janeiro``, então o ano referência será o ano passado.
        ano_delta = ano - 1 if mes == 'Janeiro' else ano

        index_mes_passado = meses.index(mes) - 1
        mes_delta = meses[index_mes_passado]

        if key == 'RECEITA':
            media_atual = self.receita(ano = ano, mes = mes)
            media_mes_passado = self.receita(ano_delta, mes_delta)
        
        elif key == 'QUANTIDADE':
            media_atual = self.quantidade(ano = ano, mes = mes)
            media_mes_passado = self.quantidade(ano_delta, mes_delta)

        else:
            raise ValueError('O valor do parâmetro key deve ser RECEITA OU QUANTIDADE')


        return media_atual - media_mes_passado