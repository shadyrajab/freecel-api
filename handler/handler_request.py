import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(asctime)s - %(message)s",
    datefmt="%d/%m/%Y %H:%M",
)


async def handle_request(client_method, *user, **kwargs):
    function_name = client_method.__name__
    try:
        result = await client_method(**kwargs)
        logging.info(f"{function_name} params {kwargs} by {user}")
        if function_name in {"Consultor", "Ranking", "Freecel"}:
            return result.to_json()

        if function_name in {
            "update_consultor",
            "remove_consultor",
            "add_consultor",
            "update_venda",
            "remove_venda",
            "add_venda",
            "update_produto",
            "remove_produto",
            "add_produto",
            "add_chamada",
            "remove_chamada"
        }:
            logging.info(f"{function_name} params {kwargs} by {user}")
            return {
                "status_code": 200,
                "message": f"Solicitação {function_name} realizada com sucesso",
                "id": result,
                "params": kwargs,
            }

        return result

    except Exception as e:
        logging.error(f"{function_name} params {kwargs} error: {e}")
        return {
            "status_code": 500,
            "message": "Ocorreu um erro ao atender sua solicitação",
            "params": kwargs,
            "exception": str(e),
        }
