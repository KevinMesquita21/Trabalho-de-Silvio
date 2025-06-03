from flask import Flask, render_template, request, jsonify, session
import nltk
import random

nltk.download('punkt')
from nltk.tokenize import word_tokenize

app = Flask(__name__)
app.secret_key = "superseguro"

# Banco de dados para o bot pegar
produtos = {
    "smartphone": [
        {"nome": "iPhone 13 128GB", "preco": 4599.0, "descricao": "Desempenho poderoso com câmeras incríveis."},
        {"nome": "iPhone 14 Pro 256GB", "preco": 7499.0, "descricao": "Tecnologia de ponta e design elegante."},
        {"nome": "Samsung Galaxy S22", "preco": 3999.0, "descricao": "Alta performance com tela AMOLED."},
        {"nome": "Samsung Galaxy A54", "preco": 2299.0, "descricao": "Ótimo custo-benefício para o dia a dia."},
        {"nome": "Motorola Edge 30", "preco": 2499.0, "descricao": "Leve, rápido e com boas câmeras."},
        {"nome": "Xiaomi Redmi Note 12", "preco": 1299.0, "descricao": "Bateria duradoura e tela fluida."},
        {"nome": "Realme 11x 5G", "preco": 1399.0, "descricao": "Conectividade 5G e ótimo desempenho."},
        {"nome": "Asus ROG Phone 6", "preco": 5999.0, "descricao": "Smartphone gamer com performance extrema."},
        {"nome": "Nokia G60", "preco": 1599.0, "descricao": "Robusto, confiável e acessível."},
        {"nome": "Zenfone 9", "preco": 4599.0, "descricao": "Compacto, potente e cheio de recursos."}
    ],
    "notebook": [
        {"nome": "Dell Inspiron i15", "preco": 3299.0, "descricao": "Notebook versátil para o dia a dia."},
        {"nome": "Acer Aspire 5", "preco": 2999.0, "descricao": "Bom desempenho com ótimo preço."},
        {"nome": "Samsung Book i5", "preco": 3499.0, "descricao": "Processador Intel Core i5 e SSD."},
        {"nome": "MacBook Air M2", "preco": 9499.0, "descricao": "Desempenho silencioso e bateria longa."},
        {"nome": "Lenovo Ideapad 3", "preco": 2799.0, "descricao": "Ideal para estudos e trabalho."},
        {"nome": "Asus VivoBook X1500", "preco": 3199.0, "descricao": "Leve e com ótimo custo-benefício."},
        {"nome": "Avell A70 MOB", "preco": 8499.0, "descricao": "Alta performance para criadores."},
        {"nome": "Positivo Motion Q", "preco": 1499.0, "descricao": "Modelo básico para tarefas simples."},
        {"nome": "HP Pavilion x360", "preco": 3899.0, "descricao": "2 em 1 com tela touch."},
        {"nome": "LG Gram 16", "preco": 7999.0, "descricao": "Ultraleve com tela grande."}
    ],
    "tablet": [
        {"nome": "iPad 10ª Geração", "preco": 3999.0, "descricao": "Ideal para produtividade e lazer."},
        {"nome": "Samsung Galaxy Tab S8", "preco": 4799.0, "descricao": "Tablet com alto desempenho e S Pen."},
        {"nome": "Lenovo Tab P11", "preco": 1999.0, "descricao": "Bom para estudos e entretenimento."},
        {"nome": "Amazon Fire HD 10", "preco": 899.0, "descricao": "Simples e funcional para leitura."},
        {"nome": "Xiaomi Pad 6", "preco": 2499.0, "descricao": "Tela grande e bom desempenho."},
        {"nome": "Multilaser M10A", "preco": 699.0, "descricao": "Tablet básico para uso leve."},
        {"nome": "Philco PTB10Q", "preco": 799.0, "descricao": "Simples, mas eficiente para tarefas básicas."}
    ],
    "fones": [
        {"nome": "AirPods Pro 2ª Geração", "preco": 1899.0, "descricao": "Cancelamento de ruído e áudio imersivo."},
        {"nome": "Samsung Galaxy Buds2", "preco": 699.0, "descricao": "Confortável e com som de qualidade."},
        {"nome": "JBL Tune 510BT", "preco": 279.0, "descricao": "Som potente e bateria longa."},
        {"nome": "Sony WH-1000XM5", "preco": 2499.0, "descricao": "Top de linha em áudio e conforto."},
        {"nome": "Redmi Buds 4 Pro", "preco": 399.0, "descricao": "Preço acessível com ótima qualidade."},
        {"nome": "Logitech G435", "preco": 499.0, "descricao": "Leve e ideal para games."},
        {"nome": "Edifier W820NB", "preco": 399.0, "descricao": "Cancelamento ativo de ruído com ótimo som."},
        {"nome": "HyperX Cloud Alpha", "preco": 599.0, "descricao": "Excelente para jogos com som claro."}
    ],
    "monitor": [
        {"nome": "Samsung 24' Curvo", "preco": 849.0, "descricao": "Visual imersivo com curvatura."},
        {"nome": "LG 27' Ultrawide", "preco": 1499.0, "descricao": "Mais espaço para produtividade."},
        {"nome": "AOC Hero 144Hz", "preco": 1299.0, "descricao": "Monitor gamer com alta taxa de atualização."},
        {"nome": "Dell P2419H", "preco": 1149.0, "descricao": "Ideal para escritório e conforto visual."},
        {"nome": "Acer Nitro 165Hz", "preco": 1399.0, "descricao": "Alta performance para games."},
        {"nome": "Philips 27M1N5500ZA", "preco": 1899.0, "descricao": "Alta resolução e taxa de atualização."}
    ],
    "console": [
        {"nome": "PlayStation 5", "preco": 4299.0, "descricao": "Nova geração de jogos com gráficos incríveis."},
        {"nome": "Xbox Series X", "preco": 4199.0, "descricao": "Poderoso e com ótima biblioteca de jogos."},
        {"nome": "Nintendo Switch OLED", "preco": 2399.0, "descricao": "Versatilidade e diversão portátil."},
        {"nome": "PlayStation 4 Slim", "preco": 2199.0, "descricao": "Ainda uma excelente opção para jogos."},
        {"nome": "Xbox Series S", "preco": 2199.0, "descricao": "Compacto, mas com desempenho de sobra."},
        {"nome": "Steam Deck 512GB", "preco": 3999.0, "descricao": "PC gamer portátil com Steam OS."}
    ],
    "componentes": [
        {"nome": "Processador Ryzen 5 5600G", "preco": 749.0, "descricao": "Ótima performance com vídeo integrado."},
        {"nome": "Intel Core i7 12700K", "preco": 1899.0, "descricao": "Processador potente para multitarefas."},
        {"nome": "Placa de vídeo RTX 3060 Ti", "preco": 2199.0, "descricao": "Excelente para jogos em 1440p."},
        {"nome": "SSD Kingston NV2 1TB", "preco": 399.0, "descricao": "Velocidade e espaço com ótimo preço."},
        {"nome": "HD Seagate 2TB", "preco": 299.0, "descricao": "Armazenamento em grande quantidade."},
        {"nome": "Fonte Corsair 650W", "preco": 499.0, "descricao": "Eficiência e estabilidade energética."},
        {"nome": "Placa-mãe B450M Steel Legend", "preco": 699.0, "descricao": "Boa compatibilidade e recursos."},
        {"nome": "Gabinete Redragon Diamondstorm", "preco": 399.0, "descricao": "Design moderno com ótimo fluxo de ar."}
    ],
    "perifericos": [
        {"nome": "Teclado Mecânico Logitech G Pro", "preco": 699.0, "descricao": "Alta performance para gamers."},
        {"nome": "Mouse Gamer Razer Viper", "preco": 349.0, "descricao": "Sensor de precisão e leveza."},
        {"nome": "Headset HyperX Cloud Stinger", "preco": 299.0, "descricao": "Confortável e som imersivo."},
        {"nome": "Webcam Logitech C920", "preco": 449.0, "descricao": "Imagem Full HD para videochamadas."},
        {"nome": "Microfone Blue Yeti", "preco": 699.0, "descricao": "Gravação profissional com facilidade."},
        {"nome": "Cadeira Gamer ThunderX3", "preco": 999.0, "descricao": "Conforto e estilo para longas sessões."}
    ]
}

faq = {
    "formas de pagamento": [
        "Aceitamos cartão, boleto, Pix e débito em conta.",
        "Você pode pagar com Pix, boleto, crédito ou débito.",
        "Claro! Temos várias formas de pagamento: cartão, boleto e Pix."
    ],
    "garantia": [
        "Todos os nossos produtos têm 1 ano de garantia de fábrica.",
        "Sim, garantimos 12 meses para qualquer produto.",
        "Pode ficar tranquilo, os produtos têm garantia de um ano."
    ],
    "prazo de entrega": [
        "Normalmente entre 3 a 7 dias úteis, depende da sua região.",
        "O prazo médio de entrega é de 3 a 7 dias úteis.",
        "Você recebe rapidinho: em até 7 dias úteis em média!"
    ],
    "atendimento": [
        "Nosso horário é das 8h às 18h, de segunda a sexta.",
        "Atendemos de segunda a sexta, das 8h às 18h.",
        "Você pode falar conosco em horário comercial, das 8h às 18h!"
    ]
}

respostas_indefinidas = [
    "Hmm... não entendi bem 😅. Você pode perguntar sobre: formas de pagamento, garantia, prazo de entrega, atendimento ou nossos produtos.",
    "Desculpe, acho que não entendi. Tente perguntar sobre produtos ou dúvidas comuns como garantia, pagamento, etc.",
    "Pode repetir? Eu sou bom com dúvidas sobre produtos, prazos ou formas de pagamento!"
]

sinonimos_produtos = {
    "smartphone": ["celular", "telefone", "smartphone"],
    "notebook": ["notebook", "laptop", "computador"],
    "tablet": ["tablet", "ipad"],
    "fones": ["fones", "fones de ouvido", "headset", "fone"],
    "monitor": ["monitor", "tela"],
    "console": ["console", "videogame", "playstation", "xbox", "nintendo"],
    "componentes": ["componentes", "pecas", "hardware", "processador", "placa", "memoria"],
    "perifericos": ["perifericos", "teclado", "mouse", "webcam", "cadeira", "microfone"]
}

def detectar_intencao(frase):
    frase = frase.lower()
    palavras = set(word_tokenize(frase))

    saudacoes = {"oi", "olá", "ola", "bom dia", "boa tarde", "boa noite", "e aí", "opa"}
    if palavras.intersection(saudacoes):
        return ("saudacao", None)

    for categoria, termos in sinonimos_produtos.items():
        for termo in termos:
            if termo in frase:
                return ("recomendacao", categoria)

    if any(p in frase for p in ["comprar", "quero comprar", "gostaria de comprar", "tem produto", "quais produtos"]):
        return ("compra", None)

    faq_chaves = {
        "formas de pagamento": ["forma", "pagamento", "pagar", "pix", "boleto", "cartão", "credito", "débito"],
        "garantia": ["garantia", "garante", "defeito", "troca"],
        "prazo de entrega": ["prazo", "entrega", "frete", "chegar", "envio"],
        "atendimento": ["atendimento", "horário", "abrir", "falar", "suporte"]
    }
    for chave, termos in faq_chaves.items():
        for termo in termos:
            if termo in frase:
                return ("faq", chave)

    if palavras.intersection({"sair", "tchau", "obrigado", "encerrar"}):
        return ("encerrar", None)

    return ("indefinido", None)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    intencao, dado = detectar_intencao(user_input)

    ultimo_topico = session.get("topico")
    ultima_intencao = session.get("intencao")

    if intencao == "faq":
        resposta = random.choice(faq[dado])
        session["intencao"] = "faq"
        session["topico"] = dado

    elif intencao == "recomendacao":
        recomendados = produtos[dado]
        intro = random.choice([
            f"Esses são alguns dos nossos {dado}s mais populares:",
            f"Claro! Aqui vai uma recomendação de {dado}s para você:",
            f"Se você procura por {dado}, veja essas opções que se destacam:",
            f"Ótima escolha! Dê uma olhada nesses {dado}s:"
        ])
        lista_formatada = "\n\n".join(
            f"- {item['nome']} — R$ {item['preco']:,.2f}\n  {item['descricao']}"
            for item in recomendados
        )
        resposta = f"{intro}\n\n{lista_formatada}"
        session["intencao"] = "recomendacao"
        session["topico"] = dado

    elif intencao == "compra":
        categorias = ", ".join(produtos.keys())
        resposta = f"Claro! Temos várias categorias de produtos: {categorias}. Qual você quer ver primeiro?"
        session["intencao"] = "compra"
        session["topico"] = None

    elif intencao == "encerrar":
        resposta = random.choice([
            "Foi um prazer te atender! Até a próxima. 👋",
            "Tchau tchau! Qualquer coisa, é só chamar!",
            "Nos vemos em breve! Boa sorte nas suas compras 😄"
        ])
        session.clear()

    elif intencao == "saudacao":
        resposta = "Olá! Como posso te ajudar hoje?"

    elif intencao == "indefinido":
        if ultima_intencao == "recomendacao" and ultimo_topico:
            recomendados = produtos[ultimo_topico]
            intro = random.choice([
                f"Ainda falando de {ultimo_topico}, aqui vão mais opções interessantes:",
                f"Se ainda estiver buscando {ultimo_topico}, experimente esses:",
                f"Continuando, veja mais alguns {ultimo_topico}s recomendados:"
            ])
            lista_formatada = "\n\n".join(
                f"- {item['nome']} — R$ {item['preco']:,.2f}\n  {item['descricao']}"
                for item in recomendados
            )
            resposta = f"{intro}\n\n{lista_formatada}"
        elif ultima_intencao == "faq" and ultimo_topico:
            resposta = f"Você queria saber mais sobre {ultimo_topico}? {random.choice(faq[ultimo_topico])}"
        else:
            resposta = random.choice(respostas_indefinidas)

    return jsonify({'response': resposta})

if __name__ == '__main__':
    app.run(debug=True)
