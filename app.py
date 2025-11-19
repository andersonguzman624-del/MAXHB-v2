from flask import Flask, render_template, request
import random

app = Flask(__name__)

def generar_codigo(prefijo, digitos):
    return prefijo + ''.join(str(random.randint(0,9)) for _ in range(digitos))

@app.route("/", methods=["GET","POST"])
def index():
    codigo_result = None
    lote_result = None
    prefi = "1800006"
    dig = 4
    if request.method == "POST":
        prefi = request.form.get("prefijo", prefi)
        dig = int(request.form.get("dig", dig))
        modo = request.form.get("modo", "uno")
        if modo == "uno":
            codigo_result = generar_codigo(prefi, dig)
        elif modo == "lote":
            lote_result = [
                generar_codigo(prefi, dig) for _ in range(100)
            ]
    return render_template("index.html", code=codigo_result, lote=lote_result, prefi=prefi, dig=dig)

if __name__ == "__main__":
    app.run(debug=True)


