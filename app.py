from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Hola mundo"

@app.route('/index')
def index():
    titulo = "IDGS803-FLASK"
    lista_parametros = ['pedro','mario','omar','juan']
    return render_template(
        'index.html', 
        titulo = titulo,
        lista_parametros = lista_parametros
    )
    
@app.route('/alumnos')
def alumnos():
    return render_template(
        'alumnos.html'
        
    )

@app.route('/operaBas', methods=['GET','POST'])
def operaBas():
    
    if request.method == "POST":
        n1 = request.form.get("n1")
        n2 = request.form.get("n2")
        tipo = request.form.get("operacion")
        resultado = 0
        if(tipo == "Sumar"): 
            resultado = float(n1) + float(n2)
        if(tipo == "Restar"): 
            resultado = float(n1) - float(n2)
        if(tipo == "Multiplicar"): 
            resultado = float(n1) * float(n2)
        if(tipo == "Dividir"): 
            resultado = float(n1) / float(n2)
        return render_template(
            'operaBas.html',
            resultado = resultado,
            n1 = n1,
            n2 = n2,
            operacion = tipo
        )
    else:
        return render_template(
            'operaBas.html'
            
        )

@app.route('/resultado', methods=['GET','POST'])
def resultado():
    n1 = request.form.get("n1")
    n2 = request.form.get("n2")
    tipo = request.form.get("operacion")
    resultado = 0
    if(tipo == "Sumar"): 
        resultado = float(n1) + float(n2)
    if(tipo == "Restar"): 
        resultado = float(n1) - float(n2)
    if(tipo == "Multiplicar"): 
        resultado = float(n1) * float(n2)
    if(tipo == "Dividir"): 
        resultado = float(n1) / float(n2)
    
    return f"<h1> EL RESULTADO ES: {resultado}</h1>"

@app.route('/usuarios')
def usuarios():
    return render_template(
        'usuarios.html'
        
    )

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