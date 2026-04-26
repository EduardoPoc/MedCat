from flask import Flask, rander_template

app = Flask(__name__)
#rotas
@app.route('/')
def home():
    pass


#inicialização
if __name__ == '__main__':
    app.run(debug=True)