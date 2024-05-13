from .delete import del_consultor, del_fixa, del_movel, del_produto
from .get import (
    get_chamadas,
    get_consultores,
    get_fixa,
    get_movel,
    get_planos,
    get_stats,
    get_utils,
    get_vendas,
)
from .post import post_consultor, post_fixa, post_movel, post_produto, post_simulacao
from .put import put_consultor, put_fixa, put_movel, put_produto

__all__ = [
    del_consultor,
    del_fixa,
    del_movel,
    del_produto,
    get_chamadas,
    get_consultores,
    get_fixa,
    get_movel,
    get_planos,
    get_stats,
    get_utils,
    post_consultor,
    post_fixa,
    post_movel,
    post_produto,
    post_simulacao,
    put_consultor,
    put_fixa,
    put_movel,
    put_produto,
    get_vendas,
]

routes = [route.router for route in __all__]
