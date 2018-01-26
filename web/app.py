from flask import *

app = Flask(__name__)

@app.route("/")
def hello():
    return "UOCIS docker demo!"

@app.route("/<extension>")
def do(extension):
    from pathlib import Path
    file = Path("./templates/" + extension)
    if file.is_file():
        return render_template(extension), 200
    else:
        for badChar in ["//","..","~"]:
            if badChar in extension:
                abort(403)
        if ".html" in extension:
            abort(404)
        else:
            abort(403)
    

@app.errorhandler(404)
def error4(e):
    return render_template("404.html"), 404

@app.errorhandler(403)
def error3(e):
    return render_template("403.html"), 403

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
