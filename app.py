from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def result():
    name = request.form.get("name", "").strip()
    technology = request.form.get("technology", "").strip()

    if not name or not technology:
        return render_template("index.html", error="Моля, попълнете всички полета!")

    return render_template("result.html", name=name, technology=technology)

if __name__ == "__main__":
    app.run(debug=True)
