import requests
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')

def home():
    return "Bem vindo a Loja Vitarella, um lugar acolhedor"


@app.route('/comprar/<id_produto>/<id_usuario>')

def comprarProdutos(id_produto, id_usuario):

    try:
        respostaLoja = requests.get(f'http://cont_compras_usuario:5001/compra/{id_usuario}').json()
    except Exception as e:
        return jsonify({"erro": "Falha na conexão com o serviço de usuário"}), 500

    if respostaLoja['status'] != 'SemDivida':
        return jsonify({"erro": "Este cliente consta com dívida na loja"}), 403
    try:
        respostaCatalogo = requests.get(f'http://cont_compras_catalogo:5002/produto/{id_produto}').json()
    except Exception as e:
        return jsonify({"erro": "Falha na coxeção com o catálogo"}), 500
    if "erro" in respostaCatalogo:
        return jsonify(respostaCatalogo), 404
     
    return jsonify({
        "mensagem": f"Monstrando: {respostaCatalogo['nome']}",
        "preco": respostaCatalogo['preco'],
        "validade": respostaCatalogo['validade']
    })

if __name__ == "__main__":
    app.run(port=5000)