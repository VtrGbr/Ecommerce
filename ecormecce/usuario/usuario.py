from flask import Flask, jsonify

app = Flask(__name__)

# Simulação de Banco de Dados de Usuários
USUARIOS = {
    "user1": {"nome": "Daniel Carmo", "status": "SemDivida"},
    "user2": {"nome": "Vitor Gabriel", "status": "Devendo"}, # Não pagou
    "user3": {"nome": "Matheus Santos", "status": "SemDivida"},
    "user4": {"nome": "Milton Silva", "status": "Devendo"},
    "user5": {"nome": "Pedro Primogenito", "status": "SemDivida"}
}

@app.route('/compra/<id_usuario>')
def verificar_status(id_usuario):
    
    usuario = USUARIOS.get(id_usuario, {"status": "desconhecido"})
    
    return jsonify({
        "id": id_usuario,
        "status": usuario['status']
    })

if __name__ == "__main__":
    app.run(port=5001, host='0.0.0.0')