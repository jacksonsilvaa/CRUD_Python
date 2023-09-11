import psycopg2
import logging

#System error register
logging.basicConfig(filename='error.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')


def insert_data_table(table, dataloop):
    con = psycopg2.connect(host='localhost', database='db_dados_usuario',
    user='postgres', password='4b4c4t3@D')
    cur = con.cursor()
    

    try:
        
        
        query = f'insert into {table} (phone, name, email) values (%s,%s,%s)'
            
        #print to check the values

        for data in dataloop:
            #print to check the values ​​during the loop
            print (f'loop data entrada for {data[0]}')
            if len(data) >= 3:
                print (f'loop data inside the if {data}')

                phone = dataloop[0]
                name = dataloop[1]
                email = dataloop[2]

                print (f'Property {phone}, {name}, {email}')
        #Execute insert
        cur.execute(query, (phone, name, email))
        print(query)

        #Commit

        con.commit()

        #close conection

        cur.close()
        con.close()

        print("Data entered successfully!")
    except (Exception, psycopg2.Error) as error:

        logging.error("Error inserting data: %s", error)

def read_select_table(table):
    con = psycopg2.connect(host='localhost', database='db_dados_usuario',
    user='postgres', password='4b4c4t3@D')
    cur = con.cursor()

    try:

        query = f"select * from {table}"

        #execute select
        cur.execute(query)

        results = cur.fetchall()

        message = ''

        

        for line in results:
            message += str(line) + "\n"
            print(message)

        #clone conection

        cur.close()
        con.close()

        return message

        print("Select success")
    except (Exception, psycopg2.Error) as error:

        logging.error("Error select data: %s", error)