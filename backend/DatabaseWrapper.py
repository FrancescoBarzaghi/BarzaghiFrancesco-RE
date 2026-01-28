import pymysql
from pymysql.cursors import DictCursor

class DatabaseWrapper:
    def __init__(self, host, port, user, password, database):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        if self.connection is None:
            try:
                self.connection = pymysql.connect(
                    host=self.host,
                    port=self.port,
                    user=self.user,
                    password=self.password,
                    database=self.database,
                    cursorclass=DictCursor
                )
                print("Connessione al DB stabilita.")
            except Exception as e:
                print(f"Errore nella connessione: {e}")
                raise e

    def execute_query(self, query, params=None):
        """Esegue query SQL di tipo SELECT."""
        self.connect()
        with self.connection.cursor() as cursor:
            cursor.execute(query, params)
            result = cursor.fetchall()
        return result

    def execute_update(self, query, params=None):
        """Esegue query SQL di tipo INSERT, UPDATE, DELETE."""
        self.connect()
        with self.connection.cursor() as cursor:
            cursor.execute(query, params)
            self.connection.commit()
            return cursor.lastrowid

    def close(self):
        """Chiude la connessione."""
        if self.connection:
            self.connection.close()
            self.connection = None
            print("Connessione al DB chiusa.")
    def create_tables(self):
        """Crea le tabelle necessarie all'applicazione."""
        create_grades_table = """
        CREATE TABLE IF NOT EXISTS grades (
            id INT AUTO_INCREMENT PRIMARY KEY,
            student_name VARCHAR(255) NOT NULL,
            subject VARCHAR(100) NOT NULL,
            grade INT NOT NULL,
            grade_date DATE NOT NULL
        );
        """
        self.execute_update(create_grades_table)
        print("Tabelle create correttamente.")