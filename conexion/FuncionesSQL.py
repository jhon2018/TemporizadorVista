from conexion.SQLserver import SQLServer
import pyodbc


class FuncionesSQL():

    def __init__(self):

        try:
            print("Entrando class Funcion_SQL()")
            self.sql_ = SQLServer()
            self.cnxn = self.sql_.connect()
            self.cursor = self.cnxn.cursor()
            self.cursor.fast_executemany = True
            #self.tabla_sql_server = 'BASE_PRUEBA'


        except pyodbc.Error as ex:
            print(
                f"Se produjo un error SQLServer __init__(): {ex.args[0]}: {ex.args[1]}")

    def __del__(self):  # limpieza y liberación de recursos
            self.cursor.close()
            self.cnxn.close()

    def MOSTRAR_CINTA(self):
        sql_cinta = ("SELECT * FROM CINTAS")
        self.cursor.execute(sql_cinta)
        unoProces=self.cursor.fetchall()
       # print("MOSTRAR CINTA" , unoProces)
        return unoProces        
    


# if __name__=='__main__':
#     fsql=FuncionesSQL()
#     fsql.MOSTRAR_CINTA()