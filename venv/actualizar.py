import psycopg2

# Conección a la base de datos
conexion = psycopg2.connect(user='postgres',
                            password='admin',
                            host='127.0.0.1',
                            port='5432',
                            database='db_personas')

# Para utilizar el cursor
cursor = conexion.cursor()


#creo sentencia
sql= 'UPDATE personas SET nombre=%s,apellido=%s,edad=%s WHERE idpersona = %s'

#recolecto los datos
idpersona= input('Ingrese el id de la persona que quiera modificar: ')
nombre= input('dime su nuevo nombre: ')
apellido= input('dime su nuevo apellido: ')
edad= input('dime su nueva edad: ')

#recolecto datos
datos= (nombre,apellido,edad,idpersona)

#
cursor.execute(sql,datos)
#guardo lo que edite
conexion.commit()

#cuantas actulizacion hicieron
actualizacion = cursor.rowcount

#muestro lo que modifico 
print(f"registro actualizado {actualizacion}")


#Cierro conexion 
cursor.close()
conexion.close()

