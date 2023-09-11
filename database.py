import psycopg2
import configparser
import logging

config = configparser.ConfigParser()
config.read('config\config.ini')

db_host = config['database']['host']
db_database = config['database']['database']
db_user = config['database']['user']
db_password = config['database']['password']

#System error register
logging.basicConfig(filename='error.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

def connect_to_database():
    con = psycopg2.connect(
        host = db_host,
        database = db_database,
        user = db_user,
        password = db_password)
    return con

def insert_data_table(table, dataloop):
    con = connect_to_database()
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
    con = connect_to_database()
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