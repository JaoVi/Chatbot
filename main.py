from flask import Flask, request, jsonify, render_template
from openai import OpenAI

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=['POST'])
def chat():
    mensagem_usuario = request.json.get('mensagem')
    if not mensagem_usuario:
        return jsonify({'erro': 'Mensagem vazia'}), 400

    try:
        client = OpenAI(
            api_key="key"
        )
        resposta = client.chat.completions.create(
            model="gpt-5.4-mini",
            store=True,
            messages=[
                {"role": "system", "content": "Voce é um bot conversante"},
                {"role": "user", "content": mensagem_usuario}
            ]
        )

        conteudo_resposta = resposta.choices[0].message.content
        return jsonify({'resposta': conteudo_resposta})
    except Exception as e:
        return jsonify({'erro', str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)