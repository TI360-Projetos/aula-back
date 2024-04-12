# -*- coding: UTF-8 -*-

import logging

import pymysql
from flask import Flask, jsonify, request
from flask_api import status
from flask_sqlalchemy import SQLAlchemy

pymysql.install_as_MySQLdb()

# configuração do log
logging.basicConfig(level=logging.INFO)

# configuração do log do sqlalchemy
logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)

db = SQLAlchemy()
app = Flask(__name__)
# configuração do banco de dados
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "mysql+mysqldb://root:root@0.tcp.sa.ngrok.io:10352/aula"
db.init_app(app)


class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(60))


class ListaDeDesejos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(60))


class ListaDeDesejosProduto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_produto = db.Column(db.Integer, nullable=False)
    id_lista_de_desejos = db.Column(db.Integer, nullable=False)


with app.app_context():
    db.create_all()

    db.session.add(Produto(nome="Celular"))
    db.session.add(Produto(nome="Notebook"))
    db.session.add(Produto(nome="TV"))
    db.session.add(Produto(nome="Fogão"))
    db.session.add(Produto(nome="Geladeira"))
    db.session.add(Produto(nome="Microondas"))
    db.session.add(Produto(nome="Cadeira"))
    db.session.add(Produto(nome="Mesa"))

    db.session.commit()


@app.route("/")
def index():
    return jsonify({"message": "Lista de desejos TI 360"})


@app.route("/produtos", methods=["GET"])
def listar_produtos():
    produtos = Produto.query.all()
    return jsonify([{"id": produto.id, "nome": produto.nome} for produto in produtos])


@app.route("/lista-de-desejos/<int:id>", methods=["GET"])
def listar_desejos(id):
    desejo = ListaDeDesejos.query.filter(ListaDeDesejos.id == id).first()
    return (
        jsonify({"id": desejo.id, "nome": desejo.nome}),
        status.HTTP_200_OK,
    )


@app.route("/lista-de-desejos", methods=["POST"])
def criar_lista_de_desejos():
    try:
        dados = request.get_json()
        nome = dados["nome"]

        desejo = db.session.add(ListaDeDesejos(nome=nome))
        db.session.commit()

        return (
            jsonify({}),
            status.HTTP_201_CREATED,
        )

    except KeyError:
        return jsonify({"mensagem": "Dados inválidos"}), status.HTTP_400_BAD_REQUEST


@app.route("/lista-de-desejos/<int:id>/produto/<int:id_produto>", methods=["POST"])
def adicionar_produto(id, id_produto):
    try:

        lista_de_desejos = ListaDeDesejos.query.filter(ListaDeDesejos.id == id).first()
        produto = Produto.query.filter(Produto.id == id_produto).first()

        lista_de_desejos_produto = ListaDeDesejosProduto(
            id_produto=produto.id, id_lista_de_desejos=lista_de_desejos.id
        )

        # SELECT * FROM lista_de_desejos_produto
        # WHERE id_produto = 1 AND id_lista_de_desejos = 1

        # SELECT * FROM lista_de_desejos_produto WHERE id = 1

        db.session.add(lista_de_desejos_produto)
        db.session.commit()

        return (
            jsonify(
                {
                    "id": lista_de_desejos_produto.id,
                    "id_produto": lista_de_desejos_produto.id_produto,
                    "id_lista_de_desejos": lista_de_desejos_produto.id_lista_de_desejos,
                }
            ),
            status.HTTP_201_CREATED,
        )

    except KeyError:
        return jsonify({"mensagem": "Dados inválidos"}), status.HTTP_400_BAD_REQUEST


@app.route("/lista-de-desejos/<int:id>/produtos", methods=["GET"])
def listar_lista_de_desejos_produtos(id):
    lista_de_desejos = ListaDeDesejos.query.get(id)
    lista_de_desejos_produtos = ListaDeDesejosProduto.query.filter(
        ListaDeDesejosProduto.id_lista_de_desejos == lista_de_desejos.id
    ).all()

    lista_de_desejos_produtos_id = [
        produto.id_produto for produto in lista_de_desejos_produtos
    ]

    produtos = Produto.query.filter(Produto.id.in_(lista_de_desejos_produtos_id)).all()

    return jsonify([{"id": produto.id, "nome": produto.nome} for produto in produtos])


@app.route("/lista-de-desejos/<int:id>", methods=["DELETE"])
def deletar_lista_de_desejos(id):
    lista_de_desejos_produto = ListaDeDesejosProduto.query.get(id)
    db.session.delete(lista_de_desejos_produto)
    db.session.commit()

    return {}

if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=8080)
