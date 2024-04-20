import psycopg2

# Conección a la base de datos
conexion = psycopg2.connect(user='postgres',
                            password='admin',
                            host='127.0.0.1',
                            port='5432',
                            database='db_personas')


# Para utilizar el cursor
cursor = conexion.cursor()

# sentencia 
sql = 'SELECT * FROM personas'

#
cursor.execute(sql)
#muestro
registro = cursor.fetchall()

#muestro al usario
for fila in registro:
    print(fila)

#cierro todo

cursor.close()
conexion.close()
