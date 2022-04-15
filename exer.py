from flask import Flask , render_template, jsonify, request

# flask importa todas as ''portas' automaticamente na pasta de templates

app = Flask(__name__)

@app.route('/')
def principal():
    return  'Ola'

@app.route('/teste')
def teste():
    return  render_template("teste.html")

@app.route('/testedoido/<string:nome>/<string:idade>')
def testepriziada(nome, idade):
    return  jsonify({'nome':nome, 'idade':idade})


@app.route('/jogo', methods=["GET", "POST"])
def jogo():
    if request.method == "GET":
        return render_template("jogo.html")
    else:
        numero = 0
        palpite = int(request.form.get("name"))
        if numero == palpite:
            return 'Acertou'
        else:
            return 'Errouuuuuuu'


@app.route('/<string:nome>')
def error(nome):
    variavel = f'pagina {nome} não tem'
    return render_template("error.html", variavel_nome = variavel)

app.run(debug=True)