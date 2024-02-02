from dataframe.dataframe import DataFrame

class Rankings(
    DataFrame
):
    def __init__(self, ranking, host, database, user, password):
        super().__init__(
            host,
            database,
            user,
            password
        )
        self.ranking = ranking

    def ranking_consultores(self):
        pass