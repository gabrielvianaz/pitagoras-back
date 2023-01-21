from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/pitagoras', methods=['GET'])
def calcular_pitagoras():
    try:
        adjacente = int(request.args.get('adjacente'))
        oposto = int(request.args.get('oposto'))
        hipotenusa = (adjacente ** 2 + oposto ** 2) ** 0.5

        return jsonify(hipotenusa)

    except:
        return {
            "erro": "É obrigatório o envio dos parâmetros 'adjacente' e 'oposto' na requisição. Eles devem ser números!"
        }, 400


if __name__ == "__main__":
    app.run(debug=True)
