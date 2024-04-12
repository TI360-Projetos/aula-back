# -*- coding: UTF-8 -*-
from flask import Flask, abort, jsonify, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)

temperaturas = []

@app.route("/")
def inicio():
    return jsonify({"message": "API de sensores"})

@app.route("/temperatura") # Read 
def temperatura():
    return jsonify(temperaturas)

@app.route("/temperatura", methods=["PUT"]) # Update
def atualizar_temperatura():
    dados = request.get_json()
    temperaturas[0] = dados
    return jsonify(dados)

@app.route("/temperatura", methods=["POST"]) # Create
def cadastrar_temperatura():
    dados = request.get_json()
    temperaturas.append(dados)
    return jsonify(dados), 201

@app.route("/temperatura", methods=["DELETE"]) # Delete
def deletar_temperatura():
    if len(temperaturas) == 0:
        abort(404, "Sem temperaturas para deletar")

    temperaturas.pop()
    return jsonify(temperaturas)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5006)


    