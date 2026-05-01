import requests
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')

def home():
    return "Bem vindo a Loja Vitarella, um lugar acolhedor"


@app.route('/comprar/<id_produto/<id_usuario>')

def comprarProdutos(id_produto, id_usuario):

    respostaLoja = requests.get(f'http://cont_compras_usuario:5001/status/{id_usuario}').json()
    

    if respostaLoja['status'] != 'bomPagador':
        return jsonify({"erro": "Este cliente consta com dívida na loja"}), 403

    respostaCatalogo = requests.get(f'http://cont_compras_catalogo:5002/status/{id_produto}').json()

    return jsonify({
        "mensagem": f"Monstrando: {respostaCatalogo['nome']}",
        "preco": respostaCatalogo['url'],
        "validade": respostaCatalogo['validade']
    })

if __name__ == "__main__":
    app.run(port=5000)