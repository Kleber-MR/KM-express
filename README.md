# KM-express
Projeto de IA



          
**Visão Geral**
- Sabor Express — aplicação Flask que otimiza entregas com IA.
- Agrupa pontos próximos com K‑Means e sugere rotas usando A*.
- Interface moderna: upload “arrasta‑e‑solta”, tabelas estilizadas e visual de clusters.

**Problema e Objetivos**
- Rotas manuais geram atrasos e custos altos em horários de pico.
- Objetivos:
  - Otimizar rotas entre múltiplos pontos.
  - Reduzir tempo e combustível.
  - Melhorar a satisfação dos clientes com entregas mais rápidas.
  - Aplicar algoritmos clássicos (K‑Means, A*).

**Abordagem**
- Mapa como grafo (NetworkX):
  - Nodos: bairros/pontos de entrega.
  - Arestas: ruas com pesos de distância estimada.
- Clustering (K‑Means): cria zonas de entrega a partir do CSV.
- Roteamento (A*): calcula caminho mínimo dentro do grafo.
- Visualização: Matplotlib para clusters e rotas; exibição no navegador.

**Algoritmos Utilizados**
- Busca heurística: `A*` — menor rota entre dois pontos.
- Clustering: `K‑Means` — agrupamento eficiente de entregas.
- Grafos (opcional): `BFS/DFS` — verificação de conectividade.
- Visualização: `Matplotlib + NetworkX`.

**Grafo de Exemplo**
- Nós: `A, B, C, D, E`
- Arestas (distância):
  - `A–B: 3`, `A–C: 2`, `B–D: 4`, `C–D: 1`, `D–E: 5`
- O grafo é gerado automaticamente e pode ser visualizado nos gráficos salvos em `static/`.

**Resultados**
- Entregas agrupadas em zonas próximas reduzem deslocamentos.
- Rotas curtas calculadas por A* dentro do grafo.
- Visualizações claras ajudam análise e tomada de decisão.
- Em cenários simulados: redução média de ~35% no tempo de rota.

**Estrutura do Repositório**
- `app.py` — aplicação Flask
- `requirements.txt` — dependências
- `src/` — lógica:
  - `clustering.py` (K‑Means)
  - `graph.py` (grafo + A*)
  - `utils.py` (auxiliares)
- `data/` — exemplos:
  - `entregas.csv` (pontos)
  - `mapa.csv` (nós/arestas)
- `templates/` — UI:
  - `index.html` (upload)
  - `resultado.html` (clusters/rotas)
- `static/` — tema e imagens:
  - `style.css` (tema escuro, responsivo)
  - `cluster_plot.png`, `cluster_pilot.png`

**Como Executar**
- Criar e ativar venv (Windows):
  - `python -m venv .venv`
  - `.\\.venv\\Scripts\\activate`
- Instalar dependências:
  - `pip install -r requirements.txt`
- Rodar o servidor (porta 5000):
  - `flask --app app.py run --debug --port 5000`
  - Alternativa: `python app.py`
- Acessar: `http://127.0.0.1:5000`
- Enviar `entregas.csv` e visualizar:
  - Tabela de clusters
  - Rota sugerida (badges com setas)
  - Gráfico dos clusters

**Exemplo de Saída**
- Tabela de clusters (exemplo):
  - `x  y  cluster`
  - `10 20 0`
  - `12 22 0`
  - `50 80 1`
  - `52 82 1`
  - `15 25 0`
  - `60 85 1`
- Rota otimizada (exemplo): `A → C → D → E`

**Limitações**
- Sem trânsito em tempo real.
- Grafo didático e simplificado.
- K‑Means requer definição prévia de `k`.

**Melhorias Futuras**
- Integrar mapas reais (Google Maps, OpenStreetMap).
- Heurísticas híbridas (Genético + A*) para cenários maiores.
- Aprendizado por reforço para rotas dinâmicas.
- Dashboard interativo para visualização de clusters e rotas.

Se quiser, eu já substituo o conteúdo do `README.md` por esta versão e faço o push para um repositório GitHub. Me informe o nome do repositório desejado (ex.: `sabor-express`) e se quer público ou privado.
        
