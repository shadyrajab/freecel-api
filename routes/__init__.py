from .delete import (
    del_aparelho,
    del_consultor,
    del_fixa,
    del_inovacao,
    del_migracao,
    del_movel,
    del_produto,
)
from .get import (
    get_aparelhos,
    get_chamadas,
    get_consultores,
    get_fixa,
    get_inovacoes,
    get_migracoes,
    get_movel,
    get_produtos,
    get_stats,
    get_utils,
    get_vendas,
)
from .post import (
    post_aparelho,
    post_consultor,
    post_fixa,
    post_inovacao,
    post_migracao,
    post_movel,
    post_produto,
    post_simulacao,
)
from .put import (
    put_aparelho,
    put_consultor,
    put_fixa,
    put_inovacao,
    put_migracao,
    put_movel,
    put_produto,
)

__all__ = [
    del_aparelho,
    del_consultor,
    del_fixa,
    del_inovacao,
    del_migracao,
    del_movel,
    del_produto,
    get_aparelhos,
    get_chamadas,
    get_consultores,
    get_fixa,
    get_inovacoes,
    get_migracoes,
    get_movel,
    get_produtos,
    get_stats,
    get_utils,
    post_aparelho,
    post_consultor,
    post_fixa,
    post_inovacao,
    post_migracao,
    post_movel,
    post_produto,
    post_simulacao,
    put_aparelho,
    put_consultor,
    put_fixa,
    put_inovacao,
    put_migracao,
    put_movel,
    put_produto,
    get_vendas,
]

routes = [route.router for route in __all__]
