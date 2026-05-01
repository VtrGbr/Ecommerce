from flask import Flask, jsonify

app = Flask(__name__)

# Simulação de Banco de Dados de Filmes
PRODUTOS = {
    "Leguminosa": {
        "nome": "Feijão", 
        "preco": 5.0, 
        "validade": "03/07/2022"
    },
    "Graos": {
        "nome": "Arroz", 
        "preco": 4.50, 
        "validade": "15/08/2023"
    },
    "Proteina":{
        "nome": "Contra-filé",
        "preco": 25.50,
        "validade": "17/07/2021"
    },
    "Verduras":{
        "nome": "Tomate",
        "preco": 2.50,
        "validade":"25/04/2020"
    }
}

@app.route('/produto/<id_produto>')
def detalhes_filme(id_produto):
    
    produto = PRODUTOS.get(id_produto, None)
    
    if produto:
        return jsonify(produto)
    else:
        return jsonify({"erro": "produto não encontrado"}), 404
    
    
    

if __name__ == "__main__":
    app.run(port=5002)