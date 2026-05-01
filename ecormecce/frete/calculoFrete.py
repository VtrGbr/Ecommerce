from flask import Flask, jsonify

app = Flask(__name__)

# Simulação de Banco de Dados de Filmes
FRETE = {
    "Maceio": {
        "valor": 0.0, 
        "distancia": 60,
    },
    "São Paulo": {
        "valor": 10.5, 
        "distancia": 160, 
        
    },
    "Rio de Janeiro":{
        "nome": 20,
        "distancia": 180,
        
    },
    "Recife":{
        "valor": 1.0,
        "distancia": 75,
    }
}

@app.route('/frete/<id_cidade>')
def detalhes_filme(id_cidade):
    
    cidade = FRETE.get(id_cidade, None)
    
    if cidade:
        return jsonify(cidade)
    else:
        return jsonify({"erro": "Cidade não encontrada"}), 404
    
    
    

if __name__ == "__main__":
    app.run(port=5003)