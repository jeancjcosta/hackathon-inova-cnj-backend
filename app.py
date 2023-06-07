from src.aiohttp_server.app import Servidor
from aiohttp import web
import src.flask_server.app as Servidor

if __name__ == "__main__":
#     web.run_app(Servidor.init(), host="127.0.0.1", port="8000")
    Servidor.init()
