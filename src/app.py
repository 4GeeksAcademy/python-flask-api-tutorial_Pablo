from flask import Flask, jsonify, request

app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "Otra de prueba", "done": True}
    ]


@app.route('/todos', methods=['GET']) #Ruta de URL y metodo GET
def hello_world():  #Funcion llamada

    json_text = jsonify(todos) #Conversión a JSON

    return json_text

@app.route('/todos', methods=['POST']) #Metodo Post
def add_new_todo():
    request_body = request.json
    todos.append(request_body)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE']) #Metodo Delete
def delete_todo(position):
    pass
    todos.pop(position)
    return jsonify(todos)


if __name__ == '__main__': #Siempre debe ir en la parte final
    app.run(host='0.0.0.0', port=3245, debug=True)