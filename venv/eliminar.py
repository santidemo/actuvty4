import psycopg2

# Conección a la base de datos
conexion = psycopg2.connect(user='postgres',
                            password='admin',
                            host='127.0.0.1',
                            port='5432',
                            database='db_personas')


# Para utilizar el cursor
cursor = conexion.cursor()

#Sentencia
sql ='DELETE FROM personas WHERE idpersona=%s'

#solicitar dato al usuario
idpersona= input('ingrese el id de persona a eliminar: ')

#
cursor.execute(sql,idpersona)

#Guardar 
conexion.commit()

#conteo de lo eliminado
registro_eliminado=cursor.rowcount

#muestro
print(f"registro eliminados {registro_eliminado}")

#
cursor.close()
conexion.close()


