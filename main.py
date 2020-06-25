from flask import Flask,render_template, request

app = Flask(__name__)

@app.route("/novo_desafio", methods=['GET','POST'])
def novo_desafio():
    if request.method == 'POST':
        try:
            lista = [str(request.form['desafio']),str(request.form['resposta']),str(request.form['link']),str(request.form['estado'])]
            #aqui vai ser chamado o metodo para salvar no banco
            return render_template('ok.html')
        except:
            return render_template('server error')    
    render_template('cadastro_desafio.html')


@app.route("/finalistas")
def text_html():
    return render_template('finalista.html',)