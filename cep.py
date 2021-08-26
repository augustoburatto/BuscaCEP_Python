from flask import Flask, render_template, request, redirect, session, flash, url_for
#render template: passando o nome do modelo e a variáveis ele vai renderizar o template
#request: faz as requisições da nosa aplicação
#redirect: redireciona pra outras páginas
#session: armazena informações do usuário
#flash: mensagem de alerta exibida na tela
#url_for: vai para aonde o redirect indica
import pycep_correios

app = Flask(__name__)

#configuração da rota index.
@app.route('/')
def index():
    return render_template('index.html', titulo='ViaCEP')
    #renderizando o template lista e as variáveis desejadas. 

@app.route('/buscar', methods=['POST'])
def buscar():
    endereco = pycep_correios.consultar_cep(request.form['num_cep'])
    cep = endereco['cep']
    rua = endereco['end']
    bairro = endereco['bairro']
    cidade = endereco['cidade']
    uf = endereco['uf']
    return render_template('index.html', titulo='ViaCEP', cep=cep, rua=rua, bairro=bairro, cidade=cidade, uf=uf)

app.run(debug = True)