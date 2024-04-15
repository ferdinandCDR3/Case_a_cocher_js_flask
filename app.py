from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['POST'])
def traiter_champ_texte():
    donnees = request.get_json()
    # champ_texte = donnees['champTexte']
    # Faire quelque chose avec la valeur du champ texte
    # return 'Données reçues : ' + champ_texte
    return donnees

if __name__ == '__main__':
    app.run()