from flask import Flask,render_template, request
import db

app = Flask(__name__)

@app.route("/novo_desafio", methods=['GET','POST'])
def novo_desafio():
    if request.method == 'POST':
        try:
            lista = [str(request.form['desafio']),str(request.form['resposta']),str(request.form['link']),str(request.form['estado'])]
            db.novo_desafio(lista)
            return render_template('ok.html')
        except:
            return render_template('server error')    
    render_template('cadastro_desafio.html')


@app.route("/finalistas")
def text_html():
    fin = db.consultar_finalistas()
    return render_template('finalista.html',fin = fin)


