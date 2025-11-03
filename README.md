🚚 Sabor Express — Rota Inteligente (Flask)

Solução de otimização de entregas para o delivery Sabor Express usando algoritmos clássicos de IA. O sistema agrupa pontos próximos com K‑Means e sugere rotas com A*, oferecendo visualização clara de resultados e uma interface moderna para envio de dados.

**Principais objetivos**
- Otimizar rotas entre múltiplos pontos de entrega.
- Reduzir custos operacionais (tempo e combustível).
- Aumentar a satisfação do cliente com entregas mais rápidas.
- Aplicar algoritmos clássicos (K‑Means, A*) de forma simples e escalável.

**O que há de novo no design**
- Layout moderno e responsivo (tema escuro) com cards.
- Área de upload “arrasta‑e‑solta” para CSV (dropzone).
- Tabelas estilizadas para clusters e “badges” de rota com setas.

**Abordagem**
- Representação do mapa como grafo (NetworkX):
  - Nodos: bairros/pontos de entrega.
  - Arestas: ruas (pesos por distância estimada).
- Agrupamento (K‑Means): cria “zonas de entrega” a partir do CSV.
- Roteamento (A*): encontra o caminho mais curto dentro do grafo.
- Visualização: gráficos gerados com Matplotlib e exibição amigável no navegador.

**Algoritmos**
- Busca heurística: `A*` — menor rota entre dois pontos.
- Clustering: `K‑Means` — agrupamento eficiente de entregas.
- Exploração de grafos (opcional): `BFS/DFS` — conectividade.
- Visualização: `Matplotlib + NetworkX`.

**Grafo simplificado**
```
   A
  / \
 B   C
  \ / 
   D
   |
   E
```
Distâncias: A–B=3, A–C=2, B–D=4, C–D=1, D–E=5.

**Resultados (exemplo)**
- Entregas agrupadas em zonas próximas (reduz deslocamentos).
- Rotas com menor custo dentro dos clusters.
- Visualizações claras dos clusters e das rotas propostas.
- Redução média estimada: ~35% no tempo de rota (cenários simulados).

**Estrutura do projeto**
```
sabor-express-main/
├── app.py                  # Aplicação Flask
├── requirements.txt        # Dependências
├── README.md               # Documentação
├── src/
│   ├── clustering.py       # K‑Means
│   ├── graph.py            # Grafo + A*
│   └── utils.py            # Funções auxiliares
├── data/
│   ├── entregas.csv        # Pontos de entrega (exemplo)
│   └── mapa.csv            # Nós/Arestas (exemplo)
├── templates/
│   ├── index.html          # Upload e instruções
│   └── resultado.html      # Resultados (clusters/rotas)
└── static/
    ├── style.css           # Tema moderno responsivo
    ├── cluster_plot.png    # Exemplo de visualização
    └── cluster_pilot.png   # Imagem auxiliar
```

**Como executar**
1. Abra o terminal na pasta do projeto.
2. Crie e ative o ambiente virtual (Windows):
   - `python -m venv .venv`
   - `.\.venv\Scripts\activate`
3. Instale as dependências:
   - `pip install -r requirements.txt`
4. Rode o servidor (porta 5000):
   - `flask --app app.py run --debug --port 5000`
   - Alternativa: `python app.py` (usa a configuração padrão).
5. Acesse no navegador: `http://127.0.0.1:5000`.
6. Faça upload do `entregas.csv` e visualize:
   - Clusters gerados (tabela estilizada).
   - Rota sugerida (badges com setas).
   - Gráfico dos clusters.

**Formato esperado do CSV**
- Colunas de exemplo: `x, y` (coordenadas) ou campos que o `clustering.py` consiga ler.
- Ajuste o arquivo conforme seu cenário real; os exemplos em `data/` ajudam a validar.

**Exemplo de saída (clusters)**
```
x   y   cluster
10  20  0
12  22  0
50  80  1
52  82  1
15  25  0
60  85  1
```
Rota otimizada (exemplo): `A → C → D → E`.

**Limitações e melhorias**
- Não considera trânsito em tempo real.
- Grafo simplificado para fins didáticos.
- K‑Means exige definição de `k` previamente.

Melhorias sugeridas:
- Integrar APIs de mapas (Google Maps, OpenStreetMap).
- Heurísticas híbridas (Genético + A*) para cenários maiores.
- Aprendizado por reforço para rotas dinâmicas.
- Dashboard interativo (frontend) para visualizações.

Licença
- Uso educacional/didático. Ajuste conforme necessidade do seu curso/empresa.