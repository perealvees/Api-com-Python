import pandas as pd
from flask import Flask

app = Flask(__name__)

#construir as funcionalidades
@app.route('/')
def homepage():
  return 'A API esta no ar'

@app.route('/pegarvendas')
def pegarvendas():
  tabela = pd.read_csv('12-18 - Criando API no Python.csv')
  total_vendas = tabela['Vendas'].sum()
  resposta = {'total_vendas': total_vendas}
  return jsonify(resposta)

  
#rodar nossa api
app.run(host='0.0.0.0')


