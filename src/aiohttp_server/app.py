from aiohttp import web
from ..controllers.test_controller import TestController

from aiojobs.aiohttp import setup


async def teste(request):
    return web.json_response("O servidor de ia está funcionando corretamente")


class Servidor:
    @staticmethod
    async def init():
        app = web.Application()
        app.add_routes([
            web.get("/api/score", TestController.get_score),
            # web.post("rota", ControladorClasse.metodo),
            web.get("/api/", teste)
        ])
        setup(app)
        return app

