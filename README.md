# KM-express

Aplicação Flask para otimização de entregas (Sabor Express) usando K‑Means para agrupar pontos próximos e A* para sugerir rotas. Interface moderna com upload de CSV e visualização de clusters.

**Visão Geral**
- Otimiza rotas entre múltiplos pontos de entrega.
- Reduz tempo e combustível com agrupamento e roteamento eficientes.
- Visualiza clusters e rotas no navegador.

**Problema e Objetivos**
- Rotas manuais geram atrasos e custos altos em horários de pico.
- Objetivos:
  - Otimizar rotas entre múltiplos pontos.
  - Reduzir tempo e combustível.
  - Melhorar satisfação dos clientes com entregas mais rápidas.
  - Aplicar algoritmos clássicos (K‑Means, A*).

**Abordagem**
- Mapa como grafo (NetworkX):
  - Nodos: bairros/pontos de entrega.
  - Arestas: ruas com pesos de distância estimada.
- Clustering (K‑Means): cria zonas de entrega a partir do CSV.
- Roteamento (A*): calcula caminho mínimo dentro do grafo.
- Visualização: Matplotlib + NetworkX.

**Grafo de Exemplo**
```
   A
  / \
 B   C
  \ /
   D
   |
   E
```
Distâncias: A–B: 3, A–C: 2, B–D: 4, C–D: 1, D–E: 5.

**Resultados**
- Entregas agrupadas em zonas próximas reduzem deslocamentos.
- Rotas curtas calculadas por A* dentro do grafo.
- Em cenários simulados: redução média de ~35% no tempo de rota.

**Estrutura do Repositório**
- `app.py` — aplicação Flask
- `requirements.txt` — dependências
- `src/` — lógica:
  - `clustering.py` (K‑Means)
  - `graph.py` (grafo + A*)
  - `utils.py` (auxiliares)
- `data/` — exemplos (CSV)
- `templates/` — UI (upload e resultado)
- `static/` — tema e imagens

**Como Executar**
- Criar e ativar venv (Windows):
  - `python -m venv .venv`
  - `\.venv\Scripts\activate`
- Instalar dependências:
  - `pip install -r requirements.txt`
- Rodar o servidor (porta 5000):
  - `flask --app app run --debug --port 5000`
  - Alternativa: `python app.py`
- Acessar: `http://127.0.0.1:5000`
- Enviar `entregas.csv` e visualizar clusters/rotas.

**Exemplo de Saída (clusters)**
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

**Limitações e Melhorias**
- Sem trânsito em tempo real; grafo didático.
- Melhorias futuras: integrar mapas reais, heurísticas híbridas, reforço, dashboard interativo.