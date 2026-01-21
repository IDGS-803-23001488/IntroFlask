from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Hola mundo"

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/hola')
def hola():
    return "HOLAAAAAAAA"

@app.route('/user/<string:user>')
def user(user):
    return f"HEllo, {user}"

@app.route("/numero/<int:n>")
def numero(n):
    return f"TU NUMERO ES: {n}"

@app.route("/user/<int:id>/<string:username>")
def username(id,username):
    return f"<h1>¡HOLAAAAA USUARIO: {id}, DE NOMBRE {username}</h1>"

@app.route("/fotante/<float:n>")
def flotante(n):
    return f"TU NUMERO FLOTANTE ES: {n}"


@app.route("/suma/<float:n>/<float:n2>")
def suma(n,n2):
    return f"TU SUMA FLOTANTE ES: {n + n2}"

@app.route("/default")
@app.route("/default/<string:param>")
def default(param="JOSE ANGEL"):
    return f"HOLA: {param}"

@app.route("/operas")
def opera():
    return """
            <form>
                <label for="name">NAME:</label>
                <input type="text" id="name", name="name" required>
                </br>
                <label for="apaterno">A. PATERNO:</label>
                <input type="text" id="apaterno", name="apaterno" required>
            </form> 
            """

if __name__ == "__main__":
    app.run(debug=True);