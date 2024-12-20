import psycopg2

# Database connection parameters
DB_PARAMS = {
    'dbname': 'mvpdb',
    'user': 'postgres',
    'password': 'Maurya@12345',
    'host': 'localhost',  # or the IP address of your server
    'port': 5432          # default PostgreSQL port
}

def dbconnection():
    try:
        # Establish the connection
        connection = psycopg2.connect(**DB_PARAMS)
        print("Database connection successful!")
        return connection
        
    except psycopg2.Error as e:
        print("Error connecting to the database:", e)
