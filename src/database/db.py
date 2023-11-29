import sqlite3

def db_consulta(
        db: str,
        query: str, 
        parametros: tuple = ()
    ) -> sqlite3.Cursor:
    """
    Funcion para gestionar las consultas sobre la BBDD sobre 
    la que se esta trabajando.

    Args:
    -----
    db: str
        Ruta absoluta de la BBDD sobre la que se require hacer la consulta.
    
    query: str
        Consulta que se quiere realizar sobre la BBDD.
    
    parametros: tuple
        En caso de querer insertar parametros se podra utilizar esta tupla 
        para señalar los parametros a insertar.

    Returns:
    --------
    resultado: Cursor
        Cursor de la BBDD con los datos que se han obtenido 
        a traves de la consulta.
    """
    with sqlite3.connect(db) as conexion:
        cursor = conexion.cursor()
        resultado = cursor.execute(query, parametros)
        conexion.commit()
    return resultado