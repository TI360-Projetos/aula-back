# -*- coding: UTF-8 -*-
from time import sleep

from flask import Flask, abort, jsonify, request
from flask_cors import CORS, cross_origin
from validate_docbr import CPF

app = Flask(__name__)
cors = CORS(app)

lista_imoveis = []

@app.route("/")
def inicio():
    return jsonify({"message": "Cadastro de alunos do TI360"})

@app.route("/imoveis", methods=["GET"])
def imoveis():
    sleep(1)
    return jsonify(lista_imoveis)

@app.route("/imoveis", methods=["POST"])
def cadastrar_imovel():
    dados = request.get_json()

    if "cpf" in dados:
        cpf = CPF()
        if not cpf.validate(dados["cpf"]):
            abort(412, "CPF inválido")

    lista_imoveis.append(dados)
    return jsonify(dados), 201

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5005)
