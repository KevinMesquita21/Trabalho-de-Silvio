
# 🛒 Assistente Virtual para Loja de Eletrônicos

Este projeto consiste em um **chatbot inteligente** capaz de simular o atendimento a clientes em uma loja de produtos eletrônicos. Desenvolvido em **Python 3** com **Flask**, ele responde perguntas frequentes, recomenda produtos e mantém o contexto da conversa de forma leve e funcional.

---

## 💡 Objetivo

Automatizar o atendimento inicial em um ambiente de e-commerce, oferecendo respostas rápidas e contextualizadas sobre produtos, formas de pagamento, prazos de entrega e suporte, além de sugerir eletrônicos por categoria.

---

## 🚀 Funcionalidades

- 🤖 Chatbot via interface web (Flask + HTML/CSS)
- 🧠 Reconhecimento de intenção com NLTK
- 📦 Recomendação de produtos com nome, preço e descrição
- 💬 Respostas variadas e humanizadas
- 📚 Banco de dados modular (`dados.py`)
- 🔁 Memória de contexto com sessões Flask
- 🎯 Sinônimos para entendimento mais flexível

---

## 📂 Estrutura de Arquivos

```
assistente_virtual/
├── app.py (ou silvio.py)     # Arquivo principal com Flask
├── dados.py                  # Banco de dados de produtos e FAQ
├── templates/
│   └── index.html            # Interface web do chat
└── static/
    └── style.css (opcional) # Estilo adicional
```

---

## ⚙️ Tecnologias Usadas

- Python 3
- Flask
- NLTK
- HTML5 / CSS3 / JavaScript
- Bootstrap (opcional)

---

## 🔧 Como Executar

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/assistente-virtual.git
   cd assistente-virtual
   ```

2. **Instale as dependências:**
   ```bash
   pip install flask nltk
   ```

3. **Rode o servidor:**
   ```bash
   python silvio.py
   ```

4. **Acesse o chatbot:**
   Abra `http://localhost:5000` no seu navegador.

---

## 📋 Exemplo de Uso

**Usuário:** "Quero ver notebooks"  
**Bot:**  
```
Esses são alguns dos nossos notebooks mais populares:

- Dell Inspiron i15 — R$ 3.299,00
  Notebook versátil para o dia a dia.

- MacBook Air M2 — R$ 9.499,00
  Desempenho silencioso e bateria longa.
...
```

---

## 📌 Melhorias Futuras

- Integração com API de produtos reais
- Aprendizado contínuo com feedback do usuário
- Análise de sentimento com IA
- Interface mais interativa com animações

---

## 👨‍💻 Autor

Desenvolvido por [Seu Nome] – Estudante de Programação  
📫 Contato: [seu-email@email.com]  
🎲 Hobbies: Codar, RPG, D&D 5e

---

## 📝 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
