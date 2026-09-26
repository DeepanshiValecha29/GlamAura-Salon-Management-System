import pyodbc


class DBConnection:
    def __init__(self):
        self.conn = None
        self.cursor = None

    def connect(self):
        try:
            self.conn = pyodbc.connect(
                "DRIVER={ODBC Driver 17 for SQL Server};"
                "SERVER=.\\SQLEXPRESS;"
                "DATABASE=GlamAuraDB;"
                "Trusted_Connection=yes;"
                "Encrypt=yes;"
                "TrustServerCertificate=yes;"
            )

            self.cursor = self.conn.cursor()
            print("Database Connected Successfully")

        except Exception as e:
            print("Connection Error:", e)

    def disconnect(self):
        if self.cursor:
            self.cursor.close()

        if self.conn:
            self.conn.close()

        print("Database Disconnected")