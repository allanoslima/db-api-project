from flask import Flask, jsonify, request
app = Flask(__name__)

clientes = [
 {
    'id': 1,
    'Nome fantasia': 'Nome fantasia 1',
    'CNPJ': '0000000000',
    'Município': 'município a',
 },
 {
    'id': 2,
    'Nome fantasia': 'Nome fantasia 2',
    'CNPJ': '0000000001',
    'Município': 'município a',
 },
 {
    'id': 3,
    'Nome fantasia': 'Nome fantasia 3',
    'CNPJ': '0000000003',
    'Município': 'município b',
 },
]

@app.route('/clientes',methods=['GET'])
def obter_clientes():
    return jsonify(clientes)

@app.route('/clientes/<int:id>',methods=['GET'])
def obter_clientes_por_id(id):
    for cliente in clientes:
        if cliente.get('id') == id:
            return jsonify(cliente)

@app.route('/clientes',methods=['POST'])
def incluir_novo_cliente():
    novo_cliente = request.get_json()
    clientes.append(novo_cliente)

    return  jsonify(clientes)

@app.route('/clientes/<int:id>',methods=['PUT'])
def editar_cliente_por_id(id):
    cliente_alterado = request.get_json()
    for indice,cliente in enumerate(clientes):
        if cliente.get('id') == id:
            clientes[indice].update(cliente_alterado)
            return jsonify(clientes[indice])

@app.route('/clientes/<int:id>',methods=['DELETE'])
def excluir_clientes(id):
    for indice, cliente in enumerate(clientes):
        if cliente.get('id') == id:
            del clientes[indice]
    return jsonify(clientes)
app.run(port=5000,host='localhost',debug=True)