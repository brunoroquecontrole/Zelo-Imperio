from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "dev-secret-key-troque-em-producao"

PRAGAS_VALIDAS = {"Baratas", "Formigas", "Ratos", "Cupins", "Escorpioes"}
TIPOS_IMOVEL_VALIDOS = {"Residencial", "Comercial"}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/orcamento", methods=["POST"])
def orcamento():
    nome = request.form.get("nome", "").strip()
    whatsapp = request.form.get("whatsapp", "").strip()
    tipo_imovel = request.form.get("tipo_imovel", "").strip()
    praga_alvo = request.form.get("praga_alvo", "").strip()

    if not nome or not whatsapp or tipo_imovel not in TIPOS_IMOVEL_VALIDOS or praga_alvo not in PRAGAS_VALIDAS:
        flash("Por favor, preencha todos os campos corretamente.", "erro")
        return redirect(url_for("home") + "#orcamento")

    # Simulação de salvamento — aqui entraria a gravação em banco de dados
    # ou envio para um CRM/planilha em uma versão futura.
    print("=== NOVO PEDIDO DE ORÇAMENTO ===")
    print(f"Nome: {nome}")
    print(f"WhatsApp: {whatsapp}")
    print(f"Tipo de Imóvel: {tipo_imovel}")
    print(f"Praga Alvo: {praga_alvo}")
    print("================================")

    flash(f"Obrigado, {nome}! Recebemos sua solicitação e entraremos em contato em breve pelo WhatsApp.", "sucesso")
    return redirect(url_for("home") + "#orcamento")


if __name__ == "__main__":
    app.run(debug=True)
