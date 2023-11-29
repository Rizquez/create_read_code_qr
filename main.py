from datetime import datetime
from flask import Flask, render_template
from src.database.db import db_consulta

app = Flask(__name__)

@app.route('/')
@app.route('/<string:codigo>')
def index(codigo=None):

    # BBDD con los registros
    db = r'src\database\registros.db'
    
    # Realizamos una consulta sobre la BBDD para obtener todos los regsitros
    resultados = db_consulta(db,"SELECT * FROM registros")
    lst_data = [row[0] for row in resultados.fetchall()]

    # Instanciamos el contadores de los registros
    contador = len(lst_data)
    
    if codigo != None and codigo != "favicon.ico":
        db_consulta(
            db,
            "INSERT INTO registros VALUES (NULL, ?,?)",
                (
                str(
                    datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
                    ),
                codigo
            )
        )
        contador = contador + 1

    # Html
    return render_template(
        'index.html', codigo = codigo, contador = contador
        )

if __name__ == '__main__':
    app.run(debug=True)

