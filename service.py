from connection import DBConnection


class Service(DBConnection):

    def insert_service(self, servicename, price, duration):
        self.connect()
        try:
            self.cursor.execute(
                "EXEC prcInsertService ?, ?, ?",
                servicename, price, duration
            )
            self.conn.commit()
            print("Service inserted successfully.")
        except Exception as e:
            print("Insert Error:", e)
        self.disconnect()

    def view_service(self):
        self.connect()
        try:
            self.cursor.execute("EXEC prcSelectService")
            rows = self.cursor.fetchall()

            print("\nService List")
            for row in rows:
                print(row)

        except Exception as e:
            print("View Error:", e)
        self.disconnect()

    def update_service(self, serviceid, servicename, price, duration):
        self.connect()
        try:
            self.cursor.execute(
                "EXEC prcUpdateService ?, ?, ?, ?",
                serviceid, servicename, price, duration
            )
            self.conn.commit()
            print("Service updated successfully.")
        except Exception as e:
            print("Update Error:", e)
        self.disconnect()

    def delete_service(self, serviceid):
        self.connect()
        try:
            self.cursor.execute(
                "EXEC prcDeleteService ?",
                serviceid
            )
            self.conn.commit()
            print("Service deleted successfully.")
        except Exception as e:
            print("Delete Error:", e)
        self.disconnect()