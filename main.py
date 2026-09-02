import json
import os
import webbrowser
from pathlib import Path
from random import uniform, seed

import numpy as np

from anubia.anubia import DeepLearning


# ============================================================
# CONFIGURAÇÕES
# ============================================================

NUM_INDIVIDUOS = 100
SEED = 42

seed(SEED)
np.random.seed(SEED)


# ============================================================
# SENSORES
# ============================================================

SENSORES = [
    "visão",
    "som",
    "proximidade",
    "ameaça",
    "social",
    "novidade"
]


# ============================================================
# PERCEPÇÕES PRODUZIDAS PELA REDE
# ============================================================

PERCEPCOES = [
    "alegria",
    "medo",
    "surpresa",
    "confiança",
    "confusão"
]


# ============================================================
# EVENTOS
# ============================================================

eventos = {

    "surpresa_aniversario": {
        "nome": "Surpresa de aniversário",

        "descricao":
            "O indivíduo entra em um ambiente onde encontra pessoas "
            "conhecidas preparando uma comemoração inesperada.",

        "sensores": [
            0.90,
            0.80,
            0.60,
            0.00,
            0.95,
            0.90
        ]
    },

    "conflito_bar": {
        "nome": "Conflito em um bar",

        "descricao":
            "O indivíduo presencia uma discussão intensa entre pessoas "
            "próximas, acompanhada de ruído e tensão social.",

        "sensores": [
            0.80,
            0.90,
            0.85,
            0.90,
            0.70,
            0.60
        ]
    },

    "acidente_transito": {
        "nome": "Acidente de trânsito",

        "descricao":
            "O indivíduo presencia uma colisão entre veículos e precisa "
            "interpretar rapidamente um acontecimento inesperado.",

        "sensores": [
            0.95,
            1.00,
            0.90,
            0.85,
            0.30,
            0.80
        ]
    },

    "encontro_especial": {
        "nome": "Encontro especial",

        "descricao":
            "O indivíduo encontra uma pessoa com quem possui forte "
            "vínculo social.",

        "sensores": [
            0.80,
            0.60,
            0.90,
            0.00,
            1.00,
            0.95
        ]
    },

    "pedido_ajuda": {
        "nome": "Pedido de ajuda",

        "descricao":
            "Uma pessoa próxima solicita ajuda para resolver um "
            "problema inesperado.",

        "sensores": [
            0.70,
            0.75,
            0.65,
            0.20,
            0.90,
            0.70
        ]
    },

    "elogio": {
        "nome": "Receber um elogio",

        "descricao":
            "O indivíduo recebe um comentário positivo inesperado "
            "sobre uma atitude ou realização.",

        "sensores": [
            0.60,
            0.80,
            0.50,
            0.00,
            0.90,
            0.65
        ]
    },

    "rejeicao_social": {
        "nome": "Rejeição social",

        "descricao":
            "O indivíduo tenta estabelecer uma interação social, "
            "mas recebe uma resposta negativa.",

        "sensores": [
            0.60,
            0.75,
            0.70,
            0.25,
            0.90,
            0.80
        ]
    },

    "lixo_praca": {
        "nome": "Lixo na praça",

        "descricao":
            "O indivíduo percebe resíduos espalhados em um espaço "
            "público utilizado pela comunidade.",

        "sensores": [
            0.80,
            0.30,
            0.70,
            0.10,
            0.60,
            0.50
        ]
    },

    "problema_comunidade": {
        "nome": "Problema coletivo",

        "descricao":
            "O indivíduo percebe um problema que afeta várias "
            "pessoas de sua comunidade.",

        "sensores": [
            0.75,
            0.70,
            0.80,
            0.35,
            0.90,
            0.80
        ]
    },

    "boas_noticias": {
        "nome": "Receber boas notícias",

        "descricao":
            "O indivíduo recebe uma informação positiva inesperada "
            "que altera suas expectativas.",

        "sensores": [
            0.70,
            0.85,
            0.50,
            0.00,
            0.70,
            0.90
        ]
    },

    "noticia_preocupante": {
        "nome": "Notícia preocupante",

        "descricao":
            "O indivíduo recebe uma informação inesperada que "
            "representa uma possível dificuldade.",

        "sensores": [
            0.70,
            0.90,
            0.60,
            0.65,
            0.70,
            0.95
        ]
    },

    "desconhecido_aproxima": {
        "nome": "Pessoa desconhecida se aproxima",

        "descricao":
            "Uma pessoa desconhecida se aproxima e inicia uma "
            "interação sem contexto prévio.",

        "sensores": [
            0.80,
            0.70,
            0.90,
            0.40,
            0.65,
            0.85
        ]
    },

    "vencer_desafio": {
        "nome": "Vencer um desafio",

        "descricao":
            "O indivíduo conclui uma tarefa difícil após investir "
            "tempo e esforço.",

        "sensores": [
            0.70,
            0.65,
            0.40,
            0.00,
            0.65,
            0.80
        ]
    },

    "perder_objeto": {
        "nome": "Perder um objeto importante",

        "descricao":
            "O indivíduo percebe que perdeu um objeto importante "
            "e precisa compreender o que aconteceu.",

        "sensores": [
            0.80,
            0.50,
            0.70,
            0.45,
            0.30,
            0.80
        ]
    },

    "receber_presente": {
        "nome": "Receber um presente",

        "descricao":
            "O indivíduo recebe um presente inesperado de outra pessoa.",

        "sensores": [
            0.85,
            0.70,
            0.55,
            0.00,
            0.95,
            0.90
        ]
    },

    "encontrar_dinheiro": {
        "nome": "Encontrar algo inesperado",

        "descricao":
            "O indivíduo encontra algo de valor ou relevância que "
            "não esperava encontrar.",

        "sensores": [
            0.90,
            0.30,
            0.60,
            0.00,
            0.30,
            0.95
        ]
    }
}


# ============================================================
# CRIAÇÃO DE INDIVÍDUOS
# ============================================================

def criar_individuo():

    return np.array([
        uniform(0.2, 1.0),  # visão
        uniform(0.2, 1.0),  # som
        uniform(0.2, 1.0),  # proximidade
        uniform(0.2, 1.0),  # ameaça
        uniform(0.2, 1.0),  # social
        uniform(0.2, 1.0)   # novidade
    ])


individuos = [
    criar_individuo()
    for _ in range(NUM_INDIVIDUOS)
]


# ============================================================
# CÁLCULO DA PERCEPÇÃO
# ============================================================

def calcular_percepcao(sensor):

    alegria = (
        sensor[4] +
        sensor[5]
    ) / 2

    medo = (
        sensor[3] +
        sensor[2]
    ) / 2

    surpresa = sensor[5]

    confianca = (
        sensor[4] -
        sensor[3]
    )

    confusao = (
        sensor[1] +
        sensor[5]
    ) / 2

    return np.clip(
        [
            alegria,
            medo,
            surpresa,
            confianca,
            confusao
        ],
        0,
        1
    )


# ============================================================
# DATASET DE TREINAMENTO
# ============================================================

X_train = []
Y_train = []


for individuo in individuos:

    for evento in eventos.values():

        sensores = np.array(
            evento["sensores"],
            dtype=float
        )

        percepcao_sensorial = (
            sensores * individuo
        )

        percepcao = calcular_percepcao(
            percepcao_sensorial
        )

        X_train.append(
            percepcao_sensorial.tolist()
        )

        Y_train.append(
            percepcao.tolist()
        )


X_train = np.array(X_train)
Y_train = np.array(Y_train)


# ============================================================
# TREINAMENTO
# ============================================================

print("=" * 70)
print("TREINAMENTO DA REDE DE PERCEPÇÃO")
print("=" * 70)

print(
    f"Indivíduos: {NUM_INDIVIDUOS}"
)

print(
    f"Eventos: {len(eventos)}"
)

print(
    f"Entradas: {X_train.shape}"
)

print(
    f"Saídas: {Y_train.shape}"
)


truman = DeepLearning(
    X_train,
    Y_train,
    learning_rate=0.01,
    hidden_layers=[12, 12],
    activation="tanh"
)


truman.train(
    epochs=10000,
    verbose=False
)


print(
    "Treinamento concluído."
)


# ============================================================
# PREVISÃO
# ============================================================

def prever(individuo, sensores):

    sensores = np.array(
        sensores,
        dtype=float
    )

    entrada = (
        sensores * individuo
    )

    entrada = entrada.reshape(
        1,
        -1
    )

    resultado = truman.predict(
        entrada
    )

    resultado = np.array(
        resultado[0],
        dtype=float
    )

    return np.clip(
        resultado,
        0,
        1
    )


# ============================================================
# AVALIAR UM EVENTO
# ============================================================

def avaliar_evento(evento_id):

    resultados = []

    sensores = eventos[evento_id]["sensores"]

    for individuo in individuos:

        resultado = prever(
            individuo,
            sensores
        )

        resultados.append(
            resultado
        )

    return np.array(
        resultados
    )


# ============================================================
# INTERPRETAÇÃO DA PERCEPÇÃO
# ============================================================

def interpretar_percepcao(media):

    indice = int(
        np.argmax(media)
    )

    dominante = PERCEPCOES[indice]

    intensidade = float(
        media[indice]
    )

    if intensidade >= 0.80:
        nivel = "muito alta"

    elif intensidade >= 0.60:
        nivel = "alta"

    elif intensidade >= 0.40:
        nivel = "moderada"

    elif intensidade >= 0.20:
        nivel = "baixa"

    else:
        nivel = "muito baixa"

    textos = {

        "alegria":
            "A população apresenta uma resposta predominantemente "
            "positiva. Os estímulos sociais e/ou a novidade parecem "
            "contribuir fortemente para essa interpretação.",

        "medo":
            "A população identifica o cenário como potencialmente "
            "ameaçador. Os estímulos relacionados à ameaça e à "
            "proximidade possuem maior influência.",

        "surpresa":
            "A novidade do acontecimento possui grande influência. "
            "Os indivíduos reconhecem uma mudança inesperada no "
            "ambiente.",

        "confiança":
            "Os estímulos sociais são relativamente mais fortes "
            "que os sinais associados à ameaça, favorecendo "
            "uma interpretação de confiança.",

        "confusão":
            "O evento combina estímulos diferentes e pode exigir "
            "maior processamento para que os indivíduos determinem "
            "como interpretar a situação."
    }

    return {
        "dominante": dominante,
        "intensidade": intensidade,
        "nivel": nivel,
        "texto": textos[dominante]
    }


# ============================================================
# CALCULA TODOS OS RESULTADOS
# ============================================================

resultados_eventos = {}

for evento_id in eventos:

    resultados = avaliar_evento(
        evento_id
    )

    media = resultados.mean(
        axis=0
    )

    interpretacao = interpretar_percepcao(
        media
    )

    resultados_eventos[evento_id] = {

        "nome": eventos[evento_id]["nome"],

        "descricao":
            eventos[evento_id]["descricao"],

        "sensores":
            eventos[evento_id]["sensores"],

        "resultados":
            resultados.tolist(),

        "media":
            media.tolist(),

        "interpretacao":
            interpretacao
    }


# ============================================================
# DADOS PARA O GRÁFICO DE COMPARAÇÃO
# ============================================================

comparacao_eventos = []

for evento_id, dados in resultados_eventos.items():

    comparacao_eventos.append({

        "id": evento_id,

        "nome": dados["nome"],

        "media": dados["media"]
    })


# ============================================================
# CONVERTE DADOS PARA JAVASCRIPT
# ============================================================

dados_json = json.dumps(
    resultados_eventos,
    ensure_ascii=False
)

comparacao_json = json.dumps(
    comparacao_eventos,
    ensure_ascii=False
)


# ============================================================
# GERA HTML
# ============================================================

def gerar_dashboard():

    primeiro_evento = list(eventos.keys())[3]

    html = f"""
<!DOCTYPE html>

<html lang="pt-BR">

<head>

<meta charset="UTF-8">

<meta name="viewport"
      content="width=device-width, initial-scale=1.0">

<title>
    Simulação de Percepção da População
</title>


<script src="https://cdn.plot.ly/plotly-3.0.1.min.js"></script>


<style>

* {{
    box-sizing: border-box;
}}

body {{

    margin: 0;

    font-family:
        Arial,
        Helvetica,
        sans-serif;

    background:
        #f1f5f9;

    color:
        #172033;
}}

header {{

    background:
        linear-gradient(
            135deg,
            #172554,
            #312e81,
            #4c1d95
        );

    color: white;

    padding:
        40px 6%;
}}

header h1 {{

    font-size: 36px;

    margin:
        0 0 12px;
}}

header p {{

    max-width: 900px;

    line-height: 1.7;

    margin: 0;

    opacity: 0.92;
}}

.container {{

    width: 92%;

    max-width: 1550px;

    margin:
        30px auto;
}}

.controls {{

    display: flex;

    flex-wrap: wrap;

    gap: 20px;

    background: white;

    padding: 24px;

    border-radius: 18px;

    box-shadow:
        0 6px 24px
        rgba(0,0,0,0.07);

    margin-bottom: 25px;
}}

.control {{

    display: flex;

    flex-direction: column;

    gap: 8px;

    min-width: 280px;
}}

.control label {{

    font-weight: bold;

    font-size: 14px;

    color: #475569;
}}

select {{

    padding:
        12px 14px;

    border:
        1px solid #cbd5e1;

    border-radius: 10px;

    font-size: 16px;

    background: white;

    cursor: pointer;
}}

.event-card {{

    background: white;

    padding: 28px;

    border-radius: 18px;

    box-shadow:
        0 6px 24px
        rgba(0,0,0,0.06);

    margin-bottom: 25px;
}}

.event-card h2 {{

    margin-top: 0;

    font-size: 28px;
}}

.event-card p {{

    line-height: 1.7;

    color: #475569;
}}

.interpretation {{

    background:
        linear-gradient(
            135deg,
            #eef2ff,
            #f5f3ff
        );

    border-left:
        6px solid #6366f1;

    border-radius: 15px;

    padding: 25px;

    margin-bottom: 25px;
}}

.interpretation h2 {{

    margin-top: 0;
}}

.interpretation strong {{

    color: #312e81;
}}

.cards {{

    display: grid;

    grid-template-columns:
        repeat(
            auto-fit,
            minmax(190px, 1fr)
        );

    gap: 15px;

    margin-bottom: 30px;
}}

.card {{

    background: white;

    border-radius: 16px;

    padding: 21px;

    box-shadow:
        0 5px 20px
        rgba(0,0,0,0.05);
}}

.card h3 {{

    margin: 0;

    font-size: 14px;

    text-transform: uppercase;

    color: #64748b;
}}

.card-value {{

    font-size: 35px;

    font-weight: bold;

    margin:
        8px 0;
}}

.progress {{

    width: 100%;

    height: 8px;

    background: #e2e8f0;

    border-radius: 20px;

    overflow: hidden;
}}

.progress-fill {{

    height: 100%;

    background:
        linear-gradient(
            90deg,
            #6366f1,
            #8b5cf6
        );

}}

.section-title {{

    font-size: 25px;

    margin:
        35px 0 18px;
}}

.grid {{

    display: grid;

    grid-template-columns:
        repeat(
            auto-fit,
            minmax(
                500px,
                1fr
            )
        );

    gap: 22px;
}}

.chart {{

    background: white;

    border-radius: 18px;

    padding: 10px;

    box-shadow:
        0 5px 22px
        rgba(0,0,0,0.06);

    overflow: hidden;
}}

.full-chart {{

    background: white;

    border-radius: 18px;

    padding: 10px;

    box-shadow:
        0 5px 22px
        rgba(0,0,0,0.06);
}}

footer {{

    text-align: center;

    color: #64748b;

    padding: 45px;
}}

@media(max-width: 800px) {{

    .grid {{
        grid-template-columns: 1fr;
    }}

    header h1 {{
        font-size: 27px;
    }}

}}

</style>

</head>


<body>


<header>

<h1>
    🧠 Simulação de Percepção da População
</h1>

<p>
    Modelo computacional que simula como indivíduos diferentes
    recebem os mesmos estímulos ambientais e produzem respostas
    perceptivas diferentes devido às suas características sensoriais.
</p>

</header>


<div class="container">


<!-- =======================================================
     CONTROLES
======================================================= -->

<div class="controls">

<div class="control">

<label>
    EVENTO
</label>

<select id="eventoSelect"></select>

</div>


<div class="control">

<label>
    INDIVÍDUO
</label>

<select id="individuoSelect"></select>

</div>

</div>


<!-- =======================================================
     EVENTO
======================================================= -->

<div class="event-card">

<h2 id="eventoNome"></h2>

<p id="eventoDescricao"></p>

<p>

<strong>
    População analisada:
</strong>

{NUM_INDIVIDUOS} indivíduos

</p>

<p>

<strong>
    Dimensões perceptivas:
</strong>

{", ".join(PERCEPCOES)}

</p>

</div>


<!-- =======================================================
     INTERPRETAÇÃO
======================================================= -->

<div class="interpretation">

<h2>
    🧠 Interpretação da população
</h2>

<p>

<strong>
    Percepção dominante:
</strong>

<span id="dominante"></span>

</p>


<p>

<strong>
    Intensidade:
</strong>

<span id="intensidade"></span>

</p>


<p>

<strong>
    Classificação:
</strong>

<span id="nivel"></span>

</p>


<p id="interpretacaoTexto"></p>

</div>


<!-- =======================================================
     CARDS
======================================================= -->

<div
    class="cards"
    id="cards"
>
</div>


<!-- =======================================================
     PERFIL
======================================================= -->

<h2 class="section-title">
    📊 Perfil perceptivo do evento
</h2>


<div class="grid">

<div class="chart">

<div id="radar"></div>

</div>


<div class="chart">

<div id="boxplot"></div>

</div>

</div>


<!-- =======================================================
     INDIVÍDUOS
======================================================= -->

<h2 class="section-title">

👥 Diferenças entre indivíduos

</h2>


<div class="grid">

<div class="chart">

<div id="heatmap"></div>

</div>


<div class="chart">

<div id="ranking"></div>

</div>

</div>


<!-- =======================================================
     COMPARAÇÃO
======================================================= -->

<h2 class="section-title">

🌎 Comparação entre eventos

</h2>


<div class="full-chart">

<div id="comparacao"></div>

</div>


<!-- =======================================================
     INDIVÍDUO
======================================================= -->

<h2 class="section-title">

👤 Perfil individual

</h2>


<div class="grid">

<div class="chart">

<div id="sensores"></div>

</div>


<div class="chart">

<div id="individuoEventos"></div>

</div>

</div>


</div>


<footer>

Simulação computacional de percepção individual

</footer>


<script>


// ==========================================================
// DADOS
// ==========================================================

const DADOS = {dados_json};

const COMPARACAO = {comparacao_json};

const PERCEPCOES = [
    "alegria",
    "medo",
    "surpresa",
    "confiança",
    "confusão"
];

const SENSORES = [
    "visão",
    "som",
    "proximidade",
    "ameaça",
    "social",
    "novidade"
];


// ==========================================================
// ELEMENTOS
// ==========================================================

const eventoSelect =
    document.getElementById(
        "eventoSelect"
    );

const individuoSelect =
    document.getElementById(
        "individuoSelect"
    );


// ==========================================================
// PREENCHE EVENTOS
// ==========================================================

for (
    const id in DADOS
) {{

    const option =
        document.createElement(
            "option"
        );

    option.value = id;

    option.textContent =
        DADOS[id].nome;

    eventoSelect.appendChild(
        option
    );
}}


// ==========================================================
// PREENCHE INDIVÍDUOS
// ==========================================================

for (
    let i = 0;
    i < {NUM_INDIVIDUOS};
    i++
) {{

    const option =
        document.createElement(
            "option"
        );

    option.value = i;

    option.textContent =
        "Indivíduo " + i;

    individuoSelect.appendChild(
        option
    );
}}


// ==========================================================
// CONFIGURAÇÃO GERAL
// ==========================================================

const config = {{
    responsive: true,
    displaylogo: false
}};


// ==========================================================
// RADAR
// ==========================================================

function atualizarRadar(
    dados
) {{

    const valores =
        dados.media.slice();

    valores.push(
        valores[0]
    );

    const labels =
        PERCEPCOES.slice();

    labels.push(
        labels[0]
    );

    Plotly.react(
        "radar",
        [{{
            type: "scatterpolar",

            r: valores,

            theta: labels,

            fill: "toself",

            name: "População",

            hovertemplate:
                "<b>%{{theta}}</b><br>" +
                "Intensidade: %{{r:.2f}}" +
                "<extra></extra>"
        }}],
        {{
            title:
                "Percepção média da população",

            polar: {{
                radialaxis: {{
                    visible: true,
                    range: [0, 1]
                }}
            }},

            margin: {{
                t: 70,
                l: 50,
                r: 50,
                b: 40
            }},

            showlegend: false
        }},
        config
    );
}}


// ==========================================================
// BOXPLOT
// ==========================================================

function atualizarBoxplot(
    dados
) {{

    const traces = [];

    for (
        let i = 0;
        i < PERCEPCOES.length;
        i++
    ) {{

        traces.push({{
            type: "box",

            y:
                dados.resultados.map(
                    linha => linha[i]
                ),

            name:
                PERCEPCOES[i],

            boxpoints:
                "all",

            jitter:
                0.35,

            pointpos:
                0,

            hovertemplate:
                "<b>" +
                PERCEPCOES[i] +
                "</b><br>" +
                "Valor: %{{y:.2f}}" +
                "<extra></extra>"
        }});
    }}

    Plotly.react(
        "boxplot",
        traces,
        {{
            title:
                "Distribuição das percepções",

            yaxis: {{
                range: [0, 1],

                title:
                    "Intensidade"
            }},

            margin: {{
                t: 70,
                l: 60,
                r: 30,
                b: 50
            }}
        }},
        config
    );
}}


// ==========================================================
// HEATMAP
// ==========================================================

function atualizarHeatmap(
    dados
) {{

    const individuos = [];

    for (
        let i = 0;
        i < dados.resultados.length;
        i++
    ) {{

        individuos.push(
            "Indivíduo " + i
        );
    }}

    Plotly.react(
        "heatmap",
        [{{
            type: "heatmap",

            z:
                dados.resultados,

            x:
                PERCEPCOES,

            y:
                individuos,

            zmin: 0,

            zmax: 1,

            colorscale:
                "Viridis",

            hovertemplate:
                "<b>%{{y}}</b><br>" +
                "%{{x}}: %{{z:.2f}}" +
                "<extra></extra>"
        }}],
        {{
            title:
                "Mapa perceptivo individual",

            margin: {{
                t: 70,
                l: 100,
                r: 30,
                b: 60
            }}
        }},
        config
    );
}}


// ==========================================================
// RANKING
// ==========================================================

function atualizarRanking(
    dados
) {{

    const ranking = [];

    for (
        let i = 0;
        i < dados.resultados.length;
        i++
    ) {{

        const valor =
            dados.resultados[i].reduce(
                (a, b) => a + b,
                0
            ) /
            PERCEPCOES.length;

        ranking.push({{
            id: i,
            valor: valor
        }});
    }}


    ranking.sort(
        (a, b) =>
            b.valor - a.valor
    );


    const melhores =
        ranking.slice(
            0,
            15
        );


    Plotly.react(
        "ranking",
        [{{
            type: "bar",

            orientation: "h",

            x:
                melhores
                    .map(
                        item =>
                            item.valor
                    )
                    .reverse(),

            y:
                melhores
                    .map(
                        item =>
                            "Indivíduo " +
                            item.id
                    )
                    .reverse(),

            text:
                melhores
                    .map(
                        item =>
                            item.valor.toFixed(2)
                    )
                    .reverse(),

            textposition:
                "auto",

            hovertemplate:
                "<b>%{{y}}</b><br>" +
                "Intensidade média: " +
                "%{{x:.2f}}" +
                "<extra></extra>"
        }}],
        {{
            title:
                "15 indivíduos mais intensamente afetados",

            xaxis: {{
                range: [0, 1],

                title:
                    "Intensidade média"
            }},

            margin: {{
                t: 70,
                l: 100,
                r: 30,
                b: 50
            }}
        }},
        config
    );
}}


// ==========================================================
// COMPARAÇÃO ENTRE EVENTOS
// ==========================================================

function atualizarComparacao() {{

    const traces = [];

    for (
        let i = 0;
        i < PERCEPCOES.length;
        i++
    ) {{

        traces.push({{
            type: "bar",

            name:
                PERCEPCOES[i],

            x:
                COMPARACAO.map(
                    evento =>
                        evento.nome
                ),

            y:
                COMPARACAO.map(
                    evento =>
                        evento.media[i]
                ),

            hovertemplate:
                "<b>%{{x}}</b><br>" +
                PERCEPCOES[i] +
                ": %{{y:.2f}}" +
                "<extra></extra>"
        }});
    }}


    Plotly.react(
        "comparacao",
        traces,
        {{
            title:
                "Como a população percebe diferentes eventos",

            barmode:
                "group",

            yaxis: {{
                range: [0, 1],

                title:
                    "Percepção média"
            }},

            xaxis: {{
                tickangle:
                    -40
            }},

            margin: {{
                t: 70,
                l: 60,
                r: 30,
                b: 130
            }}
        }},
        config
    );
}}


// ==========================================================
// PERFIL SENSORIAL
// ==========================================================

function atualizarSensores(
    individuoId
) {{

    const evento =
        DADOS[eventoSelect.value];

    const dadosIndividuo =
        individuoId;

    const sensores =
        evento.resultados;

    const resultado =
        DADOS[eventoSelect.value]
            .resultados[dadosIndividuo];


    Plotly.react(
        "sensores",
        [{{
            type: "bar",

            x:
                SENSORES,

            y:
                evento.sensores,

            text:
                evento.sensores.map(
                    valor =>
                        valor.toFixed(2)
                ),

            textposition:
                "auto",

            hovertemplate:
                "<b>%{{x}}</b><br>" +
                "Estímulo: %{{y:.2f}}" +
                "<extra></extra>"
        }}],
        {{
            title:
                "Estímulos do evento",

            yaxis: {{
                range: [0, 1],

                title:
                    "Intensidade"
            }},

            margin: {{
                t: 70,
                l: 60,
                r: 30,
                b: 70
            }}
        }},
        config
    );
}}


// ==========================================================
// PERFIL INDIVIDUAL EM TODOS OS EVENTOS
// ==========================================================

function atualizarIndividuoEventos(
    individuoId
) {{

    const traces = [];

    for (
        let i = 0;
        i < PERCEPCOES.length;
        i++
    ) {{

        traces.push({{
            type: "scatter",

            mode: "lines+markers",

            name:
                PERCEPCOES[i],

            x:
                COMPARACAO.map(
                    evento =>
                        evento.nome
                ),

            y:
                COMPARACAO.map(
                    evento =>

                        DADOS[evento.id]
                            .resultados[
                                individuoId
                            ][i]
                ),

            hovertemplate:
                "<b>%{{x}}</b><br>" +
                PERCEPCOES[i] +
                ": %{{y:.2f}}" +
                "<extra></extra>"
        }});
    }}


    Plotly.react(
        "individuoEventos",
        traces,
        {{
            title:
                "Evolução perceptiva do indivíduo",

            yaxis: {{
                range: [0, 1],

                title:
                    "Intensidade"
            }},

            xaxis: {{
                tickangle:
                    -40
            }},

            margin: {{
                t: 70,
                l: 60,
                r: 30,
                b: 130
            }}
        }},
        config
    );
}}


// ==========================================================
// CARDS
// ==========================================================

function atualizarCards(
    dados
) {{

    const container =
        document.getElementById(
            "cards"
        );

    container.innerHTML = "";

    for (
        let i = 0;
        i < PERCEPCOES.length;
        i++
    ) {{

        const valor =
            dados.media[i];

        const percentual =
            valor * 100;

        container.innerHTML += `

            <div class="card">

                <h3>
                    ${{PERCEPCOES[i]}}
                </h3>

                <div class="card-value">

                    ${{valor.toFixed(2)}}

                </div>

                <div class="progress">

                    <div
                        class="progress-fill"
                        style="width:
                            ${{percentual}}%"
                    ></div>

                </div>

                <p>

                    ${{percentual.toFixed(1)}}%
                    de intensidade

                </p>

            </div>
        `;
    }}
}}


// ==========================================================
// ATUALIZA TUDO
// ==========================================================

function atualizarDashboard() {{

    const eventoId =
        eventoSelect.value;

    const individuoId =
        Number(
            individuoSelect.value
        );

    const dados =
        DADOS[eventoId];


    // Evento

    document.getElementById(
        "eventoNome"
    ).textContent =
        dados.nome;


    document.getElementById(
        "eventoDescricao"
    ).textContent =
        dados.descricao;


    // Interpretação

    document.getElementById(
        "dominante"
    ).textContent =
        dados.interpretacao.dominante;


    document.getElementById(
        "intensidade"
    ).textContent =
        dados.interpretacao.intensidade
            .toFixed(2);


    document.getElementById(
        "nivel"
    ).textContent =
        dados.interpretacao.nivel;


    document.getElementById(
        "interpretacaoTexto"
    ).textContent =
        dados.interpretacao.texto;


    // Gráficos

    atualizarCards(
        dados
    );

    atualizarRadar(
        dados
    );

    atualizarBoxplot(
        dados
    );

    atualizarHeatmap(
        dados
    );

    atualizarRanking(
        dados
    );

    atualizarSensores(
        individuoId
    );

    atualizarIndividuoEventos(
        individuoId
    );
}}


// ==========================================================
// EVENTOS DOS CONTROLES
// ==========================================================

eventoSelect.addEventListener(
    "change",
    atualizarDashboard
);


individuoSelect.addEventListener(
    "change",
    atualizarDashboard
);


// ==========================================================
// EVENTO INICIAL
// ==========================================================

eventoSelect.value =
    "{primeiro_evento}";

individuoSelect.value =
    "0";


// ==========================================================
// PRIMEIRA RENDERIZAÇÃO
// ==========================================================

atualizarDashboard();

atualizarComparacao();

</script>


</body>

</html>
"""

    # --------------------------------------------------------
    # SALVA
    # --------------------------------------------------------

    caminho = (
        Path.cwd()
        / "dashboard_percepcao.html"
    )

    with open(
        caminho,
        "w",
        encoding="utf-8"
    ) as arquivo:

        arquivo.write(html)


    # --------------------------------------------------------
    # ABRE AUTOMATICAMENTE
    # --------------------------------------------------------

    url = caminho.resolve().as_uri()

    print()
    print("=" * 70)
    print("DASHBOARD GERADO COM SUCESSO")
    print("=" * 70)

    print(
        f"Arquivo: {caminho}"
    )

    print(
        f"Eventos: {len(eventos)}"
    )

    print(
        f"Indivíduos: {NUM_INDIVIDUOS}"
    )

    print()
    print(
        "Abrindo o dashboard no navegador..."
    )

    webbrowser.open_new_tab(
        url
    )


# ============================================================
# EXECUÇÃO
# ============================================================

if __name__ == "__main__":

    gerar_dashboard()