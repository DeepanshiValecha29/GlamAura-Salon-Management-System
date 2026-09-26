from connection import DBConnection


class Customer(DBConnection):

    def insert_customer(self, customername, gender, phone, email):
        self.connect()
        try:
            self.cursor.execute(
                "EXEC prcInsertCustomer ?, ?, ?, ?",
                customername, gender, phone, email
            )
            self.conn.commit()
            print("Customer inserted successfully.")
        except Exception as e:
            print("Insert Error:", e)
        self.disconnect()

    def view_customer(self):
        self.connect()
        try:
            self.cursor.execute("EXEC prcSelectCustomer")
            rows = self.cursor.fetchall()

            print("\nCustomer List")
            for row in rows:
                print(row)

        except Exception as e:
            print("View Error:", e)
        self.disconnect()

    def update_customer(self, customerid, customername, gender, phone, email):
        self.connect()
        try:
            self.cursor.execute(
                "EXEC prcUpdateCustomer ?, ?, ?, ?, ?",
                customerid, customername, gender, phone, email
            )
            self.conn.commit()
            print("Customer updated successfully.")
        except Exception as e:
            print("Update Error:", e)
        self.disconnect()

    def delete_customer(self, customerid):
        self.connect()
        try:
            self.cursor.execute(
                "EXEC prcDeleteCustomer ?",
                customerid
            )
            self.conn.commit()
            print("Customer deleted successfully.")
        except Exception as e:
            print("Delete Error:", e)
        self.disconnect()