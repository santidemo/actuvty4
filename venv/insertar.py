import psycopg2

# Conección a la base de datos
conexion = psycopg2.connect(user='postgres',
                            password='admin',
                            host='127.0.0.1',
                            port='5432',
                            database='db_personas')

# Para utilizar el cursor
cursor = conexion.cursor()

# Creo sentencia sql 
sql = 'INSERT INTO personas(nombre,apellido,edad) VALUES(%s,%s,%s)'

#pido los datos al usuarios
nombre= input('dime un nombre: ')
apellido = input('Ingrese apellido: ')
edad = input('Ingrese su edad :')
# reconecto los datos
datos = (nombre,apellido,edad)

#
cursor.execute(sql,datos)

#guardo el registro 
conexion.commit()

#registro que se registran
registro = cursor.rowcount #junta los registros 


#muestro el mensajes 
print(f"registro insertado :{registro}")

#cierro conexion
cursor.close()
conexion.close()
