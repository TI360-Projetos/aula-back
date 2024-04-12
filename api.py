from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/")
def hello_ti360():
    return jsonify({"message": "Hello TI360!"})

@app.route("/servicos")
def servicos():
    return jsonify({"message": "Serviços TI360!"})

@app.route("/servicos", methods=["PUT", "POST", "PATCH"])
def servicos_edicao():
    return jsonify({"message": "Serviços Edição TI360!"}), 201

@app.route("/mensagens", methods=["GET"])
def ola_ti360_get():
    return jsonify({"mensagem": "Olá TI360 GET!"})

@app.route("/mensagens", methods=["POST"])
def ola_ti360_post():
    dados = request.get_json()

    if "celular" not in dados:
        return {"message": "Celular não informado!"}, 400
    
    if "email" not in dados:
        return {"message": "Email não informado!"}, 400

    print(dados['celular'])
    print(dados['email'])
    print(f"celular: {dados['celular']} email: {dados['email']}")

    return {"message": "Cadastro realizado com sucesso!"}, 201

@app.route("/mensagens", methods=["PUT"])
def editar_mensagens():
    return jsonify({"mensagem": "Edição realizada com sucesso!"})

@app.route("/mensagens", methods=["DELETE"])
def deletar_mensagens():
    return jsonify({"mensagem": "Remoção realizada com sucesso!"})

@app.route("/mensagens/<id>", methods=["GET"])
def pegar_mensagens(id):
    return jsonify({"mensagem": f"Olá seu id é {id}!"})

@app.route("/alunos/erro", methods=["GET", "POST"])
def erro():
    return jsonify({"mensagem": "Erro!"}), 500

if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=8080)