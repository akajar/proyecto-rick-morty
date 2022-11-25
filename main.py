from flask import render_template
from app import create_app

app = create_app()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/perfil/<int:id>")
def perfil(id):
    return render_template("perfil.html")

if __name__ == "__main__":
    app.run()