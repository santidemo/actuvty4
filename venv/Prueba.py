import psycopg2

# Conección a la base de datos
conexion = psycopg2.connect(user='postgres',
                            password='admin',
                            host='127.0.0.1',
                            port='5432',
                            database='db_personas')

# Para utilizar el cursor
cursor = conexion.cursor()

# Crear sentencia SQL
sql = 'SELECT * FROM personas'

cursor.execute(sql)

# Mostrar los datos
registros = cursor.fetchall()
print(registros)

# Cerrar el cursor y la conexión
cursor.close()
conexion.close()