import mysql.connector

class MySQLDatabase:
    def __init__(self, host='localhost', port=3306, user='root', password='password', database='mysql'):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.databases = []

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.database
            )
            print("Connected to MySQL database.")
        except mysql.connector.Error as error:
            print("Failed to connect to MySQL database:", error)

    def get_databases(self):
        if self.connection.is_connected():
            cursor = self.connection.cursor()
            cursor.execute("SHOW DATABASES")
            self.databases = [database[0] for database in cursor]
            cursor.close()
            return self.databases
        else:
            print("Not connected to MySQL database.")
            return []

    def get_tables(self):
        tables = {}
        if self.connection.is_connected():
            for database in self.databases:
                cursor = self.connection.cursor()
                cursor.execute(f"SHOW TABLES FROM `{database}`")
                tables[database] = [table[0] for table in cursor]
                cursor.close()
        else:
            print("Not connected to MySQL database.")
        return tables


def main():
    # host = 'localhost'
    host = '10.10.68.240'
    port = 3306
    user = 'root'
    password = 'password'
    database = 'mysql'

    db = MySQLDatabase(host, port, user, password, database)
    db.connect()


    databases = db.get_databases()
    print(f"[+] Total Databases: {len(databases)}")
    print("Databases:", databases)

    tables = db.get_tables()
    for database, table_list in tables.items():
        print(f"[+] Datase: {database}")
        print(f"[+] Total Tables in {database}: {len(table_list)}")
        print(table_list)
        print("-"*80,"\n")

    db.connection.close()
    print("Connection closed.")

if __name__ == '__main__':
    main()
