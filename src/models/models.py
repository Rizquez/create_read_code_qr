import os
import csv
import qrcode
import sqlite3
from ..database.db import db_consulta
from ..utils.functions import generate_unique_token, dataframe_from_tbl_excel

class GenerateQR():
    """
    Clase para generar los codigos QR sobre 
    un Usuario, es posible asignar Token para 
    generar los QR si se desea o en caso contrario 
    se podra pedir que de manera interna las diferentes 
    funciones generen el Token y el QR sobre los usuarios.

    Args:
    -----
    None

    Internal Methods:
    -----------------

    generate_qr
    """
    def __init__(self) -> None:
        self.__db = r'src\database\existing_qr.db'

    def generate_qr(
            self,
            path_input: str,
            path_output: str,
            type_file: str,
            tbl_name: None = None,
            delimiter: str = ';',
            internal_sha: str = 'No'
        ) -> None:
        """
        Funcion creada para realizar la generacion de codigos QR 
        a partir de una fichero que recibe como input con los datos 
        con el nombre del Usuario y el QR que se le esta asignando 
        a dicho Usuario. Tanto si el fichero es Excel como si es CSV, 
        dicho fichero debera contener unicamente dos columna, una 
        donde se indicara el Usuario y otra donde se indicara el 
        Token. En caso de querer que se genere el token de manera 
        interna, bastara con que el fichero contenga una sola 
        columna, la cual debera la de usuarios.
        
        Args:
        -----

        path_input: str
            Ruta absoluta de los archivo que permite recibir esta 
            funcion sera ficheros Excel y ficheros CSV.

        path_output: str
            Ruta NO absoluta en donde se quieran almacenar los QR 
            generados, esta funcion de manera interna nombrara a 
            cada QR que se genere en funcion del Usuarios al que 
            se le asigne.
        
        type_file: str
            Parametro puede tomar el valor de ``Excel`` o el ``CSV`` 
            segun el tipo de dato que entre.

        tbl_name: NoneType
            Este parametro entrara en afecto en el caso de que el fichero 
            Excel que se reciba como parametro contenga la informacion en 
            una tabla, en ese caso se debera indicar aqui el nombre de la 
            tabla.
        
        delimiter: str
            Default ;
            Parametro utilizado en el caso de que el fichero sea un CSV, 
            se debera indicar el tipo de delimitador que se selecciono.

        internal_sha: str
            Default No
            Con este parametro se indica si el QR a generar debe tener en 
            consideracion la generacion del token para los usuarios de 
            manera interna, en caso contrario se tomara el que se contenga 
            en el fichero que se recibe como input.
        
        Returns:
        --------

        None
        """
        # Comprobamos si el tipo de archivo que esta entrando en la funcion es Excel
        if type_file.lower() == 'excel':
            
            # Llamamos al metodo para que genere los QR
            self.__qr_from_excel(
                path_input, path_output, tbl_name, internal_sha
                )

        # En caso de que sea un CSV
        elif type_file.lower() == 'csv':
            
            # Llamamos al metodo para que genere los QR
            self.__qr_from_csv(
                path_input, path_output, delimiter, internal_sha
                )
        
        # En ultima instancia arrojamos un error
        else:
            raise ValueError(
                "Verifique el parametro `type_file`"
                )

    def __qr_from_csv(
            self,
            path_input: str,
            path_output: str,
            delimiter: str,
            internal_sha: str
        ) -> None:
        """
        Metodo para generar los codigos QR a partir de un fichero CSV.

        Args:
        -----

        path_input: str
            Ruta absoluta del fichero CSV.

        path_output: str
            Ruta NO absoluta en donde se quieran almacenar los QR 
            generados, esta funcion de manera interna nombrara a 
            cada QR que se genere en funcion del Usuarios al que 
            se le asigne.

        delimiter: str
            Default ;
            Parametro utilizado en el caso de que el fichero sea un CSV, 
            el cual indica el tipo de delimitador que contiene el fichero.

        internal_sha: str
            Con este parametro se indica si el QR a generar debe tener en 
            consideracion la generacion del token para los usuarios de 
            manera interna, en caso contrario se tomara el que se contenga 
            en el fichero que se recibe como input.

        Returns:
        --------

        None
        """
        # Verificamos la existencia del fichero CSV
        if not os.path.exists(path_input):
            raise FileNotFoundError(f"El archivo {path_input} no existe.")
    
        # Asegurando que la ruta de salida exista, si no la creamos
        if not os.path.exists(path_output):
            os.makedirs(path_output)

        # Abrimos el CSV y extraemos la informacion
        with open(path_input, 'r') as csv_file:
            data = csv.reader(csv_file, delimiter=delimiter)
            next(data, None)

            # Verificamos si necesitamos buscar los tokens existentes para extraerlos de la BBDD
            if internal_sha.lower() == 'si':
                lst_existing_token = self.__get_existing_token()

            # Recorremos la data del CSV para crear el user y token
            for lst_info_row in data:
                user = lst_info_row[0]
                token = generate_unique_token(lst_existing_token) if internal_sha.lower() == 'si' else lst_info_row[1]
                
                # Llamamos al metodo que se encargara de almacenar y generar el Token y QR
                self.__save_code_qr(path_output, user, token)

    def __qr_from_excel(
            self,
            path_input: str,
            path_output: str,
            tbl_name: str,
            internal_sha: str
        ) -> None:
        """
        Metodo para generar los codigos QR a partir de un fichero Excel.

        Args:
        -----

        path_input: str
            Ruta absoluta del fichero Excel.

        path_output: str
            Ruta NO absoluta en donde se quieran almacenar los QR 
            generados, esta funcion de manera interna nombrara a 
            cada QR que se genere en funcion del Usuarios al que 
            se le asigne.

        tbl_name: str
            Posible nombre de la tabla existente dentro del fichero 
            Excel que contiene la informacion para generar los QR.

        internal_sha: str
            Con este parametro se indica si el QR a generar debe tener en 
            consideracion la generacion del token para los usuarios de 
            manera interna, en caso contrario se tomara el que se contenga 
            en el fichero que se recibe como input.

        Returns:
        --------

        None
        """
        # Verificamos la existencia del fichero Excel
        if not os.path.exists(path_input):
            raise FileNotFoundError(f"El archivo {path_input} no existe.")
    
        # Asegurando que la ruta de salida exista, si no la creamos
        if not os.path.exists(path_output):
            os.makedirs(path_output)

        # Extraemos la data de la tabla
        df_data = dataframe_from_tbl_excel(path_input, tbl_name)

        # Verificamos si necesitamos buscar los tokens existentes para extraerlos de la BBDD
        if internal_sha.lower() == 'si':
            lst_existing_token = self.__get_existing_token()
    
        # Recorremos la data del CSV para crear el user y token
        for idx in df_data.index:
            user = df_data.at[idx, 'Usuario']
            token = generate_unique_token(lst_existing_token) if internal_sha.lower() == 'si' else df_data.at[idx, 'Token']
            
            # Llamamos al metodo que se encargara de almacenar y generar el Token y QR
            self.__save_code_qr(path_output, user, token)

    def __get_existing_token(self):
        """
        Metodo para obtener la lista de token que 
        se encuentra ya existentes si asignados.

        Args:
        -----

        None

        Returns:
        --------
        
        lst_existing_token: list
            Lista con los valores de los tokens existentes
        """
        resultados = db_consulta(self.__db, "SELECT Token From existing_code_qr")
        return [row[0] for row in resultados.fetchall()]

    def __save_code_qr(
            self,
            path_output: str,
            user:str,
            token: str
        ) -> None:
        """
        Metodo para realizar el almacenado de los distintos QR, 
        ademas de que tambien registra en la BBDD los tokens 
        que se van generando junto a los usuarios que a los que 
        se le van asignando dicho token.

        Args:
        -----

        path_output: str
            Ruta NO absoluta en donde se quieran almacenar los QR 
            generados, esta funcion de manera interna nombrara a 
            cada QR que se genere en funcion del Usuarios al que 
            se le asigne.
        
        user: str
            Usuario al cual se le esta asignado el Token
        
        token: str
            Token que se esta generando o asignando al Usuario

        Returns:
        --------

        None
        """
        # Ahora creamos el Codigo QR y lo
        qr_code = qrcode.make(token)
        path_output_qr = os.path.join(path_output, f'{user}.png')

        # Almacenamos usuario y token en la bbdd
        db_consulta(self.__db, "INSERT INTO existing_code_qr VALUES(?, ?)", (user, token))
        
        # Por ultimo almacenamos cada QR generado
        with open(path_output_qr, 'wb') as qr_file:
            qr_code.save(qr_file)
