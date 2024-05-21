import sqlite3 as sql


'''
def mod_data_profs(dni,x,y):
            conn = sql.connect('ProyectoProgramacion\Colegio.db')
            c = conn.cursor()

            c.execute(UPDATE profesores
                      SET
                        nombre = ?,
                        apellido = ?
                      WHERE
                         DNI_prof = ?

            ,(x,y,dni))


            conn.commit()
            conn.close()

'''


# Fetch data from the database

def mod_data_profs(dni,x,y):
            try:
              conn = sql.connect('Colegio.db')
              c = conn.cursor()

              c.execute('''UPDATE profesores
                      SET
                          nombre = ?,
                          apellido = ?
                      WHERE
                          DNI_prof = ?

              ''',(x,y,dni))


              conn.commit()
              print("Update successful")
            except:
              print("Error Ocurred")
            finally:
              conn.close()

          
mod_data_profs('X11111111','Ricardo','Palomos')



conn = sql.connect('Colegio.db')
c = conn.cursor()
c.execute("SELECT * FROM profesores")  # Replace 'your_table_name' with the actual table name
data = c.fetchall()
print(data)
for column in c.description: 
    print(f'{column[0]}',end=",") 
     

# Close the connection
conn.close()