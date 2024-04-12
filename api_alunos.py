## pip install Flask
## para rodar o servidor: python api_alunos.py
import uuid

from flask import Flask, jsonify, request

api = Flask(__name__)

alunos = []

STATUS_HTTP_OK = 200
STATUS_HTTP_NOT_FOUND = 404
STATUS_HTTP_CREATED = 201

def buscar_aluno(id):
    """
    Busca um aluno pelo id
    :param id: id do aluno a ser buscado
    :return: aluno encontrado ou None, caso não encontre
    """
    for aluno in alunos:
        if aluno['id'] == id:
            return aluno

    return None

@api.route("/alunos", methods=['POST'])
def cadastrar_aluno():
    dados = request.get_json()
    dados["id"] = uuid.uuid4()
    alunos.append(dados)

    return jsonify(alunos), STATUS_HTTP_CREATED

@api.route("/alunos", methods=['GET'])
def listar_alunos():
    return jsonify(alunos), STATUS_HTTP_OK

@api.route("/alunos/<uuid:id>", methods=['GET'])
def detalhe_aluno(id):
    aluno = buscar_aluno(id)
    if aluno:
        return jsonify(aluno), STATUS_HTTP_OK

    return jsonify({"mensagem": "Aluno não encontrado"}), STATUS_HTTP_NOT_FOUND


@api.route("/alunos/<uuid:id>", methods=['PUT'])
def atualizar_aluno(id):
    aluno = buscar_aluno(id)
    if aluno:
        aluno = request.get_json()
        return jsonify(aluno), STATUS_HTTP_OK

    return jsonify({"mensagem": "Aluno não encontrado"}), STATUS_HTTP_NOT_FOUND

@api.route("/alunos/<uuid:id>", methods=['DELETE'])
def deletar_aluno(id):
    aluno = buscar_aluno(id)
    if aluno:
        aluno["status"] = "inativo"
        return jsonify(alunos), STATUS_HTTP_OK

    return jsonify({"mensagem": "Aluno não encontrado"}), STATUS_HTTP_NOT_FOUND

@api.route("/alunos/<uuid:id>/ativar", methods=['PATCH'])
def ativar_aluno(id):
    aluno = buscar_aluno(id)
    if aluno:
        aluno["status"] = "ativo"
        return jsonify(alunos), STATUS_HTTP_OK

    return jsonify({"mensagem": "Aluno não encontrado"}), STATUS_HTTP_NOT_FOUND

if __name__ == "__main__":
    api.run(debug=True, host="localhost", port=8080)