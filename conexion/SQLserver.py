import pyodbc
from PyQt5.QtWidgets import QMessageBox


class SQLServer:
    #def __init__(self, server, database, username, password):#para que reciba parametros
    def __init__(self):
        self.server = ""
        self.database = "PELICULA"
        self.username = ""
        self.password = ""
        self.driver = "ODBC Driver 17 for SQL Server"

    def connect(self):
        try:
            if self.password:
                # Autenticación con contraseña
                connection = pyodbc.connect(f'DRIVER={self.driver};SERVER={self.server};DATABASE={self.database};UID={self.username};PWD={self.password};')
            else:
                # Autenticación de Windows
                connection = pyodbc.connect(f'DRIVER={self.driver};SERVER={self.server};DATABASE={self.database};UID={self.username};Trusted_Connection=yes;')

            print('Conectado Servidor:', connection.getinfo(pyodbc.SQL_SERVER_NAME))
            print('Conectado Base De Datos:', connection.getinfo(pyodbc.SQL_DATABASE_NAME))

            return connection
        except pyodbc.Error as e:
            print(f"ERROR CONEXION SQL Server: {e}")
            QMessageBox.critical(None, "Error", "No se pudo establecer la conexión a la base de datos tabla")

# # #ESTO ES LA FORMA QUE LO DEBES LLAMAR EN OTRAS CLASES
# # if __name__=='__main__':
# #       sql_=SQLServer()
# #       cnxn=sql_.connect()
# #       cursor = cnxn.cursor()
# #       cursor.close()            