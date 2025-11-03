from flask import Flask, render_template, request
from src.graph import Graph
from src.clustering import agrupar_entregas
import pandas as pd
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resultado', methods=['POST'])
def resultado():
    # Lê os dados enviados pelo formulário
    arquivo = request.files['arquivo']
    caminho = os.path.join('data', arquivo.filename)
    arquivo.save(caminho)

    # Lê os pontos de entrega
    entregas = pd.read_csv(caminho)

    # Aplica o K-Means para agrupar as entregas
    agrupamentos, imagem = agrupar_entregas(entregas)

    # Cria grafo e encontra rota otimizada (A*)
    grafo = Graph()
    grafo.gerar_exemplo()  # grafo de exemplo
    rota = grafo.a_star('A', 'E')

    return render_template(
        'resultado.html',
        clusters=agrupamentos,
        imagem=imagem,
        rota=rota
    )

if __name__ == '__main__':
    app.run(debug=True)
