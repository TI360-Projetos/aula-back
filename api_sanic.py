from sanic import Sanic
from sanic.response import json
from sanic_ext import Config, Extend

app = Sanic("ListaDeDesejosApp")
app.extend(config=Config(http_auto_trace=True))
app.config.HEALTH = True


@app.get("/")
async def index(request):
    return json({"message": "Lista de desejos TI 360"})

@app.get("/hello")
async def hello():
    return "Hello RESTEasy"


if __name__ == "__main__":
    app.run(debug=True, access_log=True, port=5000, auto_reload=True)
