# Aula 02 - Criando Rotas e Configurações

#adicionar biblioteca

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Index"

def teste():
    return "<h1> TESTE 1</h1>"

def teste2():
    return "<h2> TESTE 1</h2>"

app.add_url_rule("/teste" , "teste", teste)
app.add_url_rule("/teste2" , "teste2", teste2)

if __name__ == '__main__':
  app.run(debug=True, port="3030")
#debug=True (Atualiza sozinho e mostra histórico de nav e mostra erro no navegador)
  