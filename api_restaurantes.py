from flask import Flask, abort, jsonify, request
from flask_cors import CORS, cross_origin
from flask_swagger import swagger

app = Flask(__name__)
cors = CORS(app)

@app.route("/documentacao")
def spec():
    return jsonify(swagger(app))

@app.route("/usuarios", methods=["POST"])
def cadastrar_usuarios():
    """
        Criar um novo usuário
        ---
        tags:
          - usuarios
        definitions:
          - schema:
              id: Group
              properties:
                name:
                 type: string
                 description: the group's name
        parameters:
          - in: body
            name: body
            schema:
              id: User
              required:
                - email
                - name
              properties:
                email:
                  type: string
                  description: email for user
                name:
                  type: string
                  description: name for user
                address:
                  description: address for user
                  schema:
                    id: Address
                    properties:
                      street:
                        type: string
                      state:
                        type: string
                      country:
                        type: string
                      postalcode:
                        type: string
                groups:
                  type: array
                  description: list of groups
                  items:
                    $ref: "#/definitions/Group"
        responses:
          201:
            description: User created
        """
    return jsonify({"message": "Cadastro de usuários"})

@app.route("/restaurantes")
def listar_restaurantes():
    return jsonify({"message": "Lista de restaurantes"})

@app.route("/restaurantes", methods=["POST"])
def cadastrar_restaurante():
    return jsonify({"message": "Cadastro de restaurante"})


@app.route("/pedidos", methods=["POST"])
def cadastrar_pedido():
    return jsonify({"message": "Cadastro de pedido"})

@app.route("/pedidos/<int:id>", methods=["GET"])
def listar_pedidos(id):
    return jsonify({"message": f"lista de pedido {id}"})

@app.route("/pedidos", methods=["GET"])
def listar_pedidos_com_filtro():
    parametros = request.args
    id_do_restaturante = parametros.get("id_do_restaurante")
    status = parametros.get("status")
    return jsonify({"message": f"lista de pedidos ID: {id_do_restaturante} | STATUS: {status}"})


@app.get("/hello")
def hello():
    return "Hello RESTEasy"

if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=5002)