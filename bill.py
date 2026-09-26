from connection import DBConnection


class Bill(DBConnection):

    def insert_bill(self, appointmentid, billdate, totalamount, paymentmode):
        self.connect()
        try:
            self.cursor.execute(
                "EXEC prcInsertBill ?, ?, ?, ?",
                appointmentid, billdate, totalamount, paymentmode
            )
            self.conn.commit()
            print("Bill inserted successfully.")
        except Exception as e:
            print("Insert Error:", e)
        self.disconnect()

    def view_bill(self):
        self.connect()
        try:
            self.cursor.execute("EXEC prcSelectBill")
            rows = self.cursor.fetchall()

            print("\nBill List")
            for row in rows:
                print(row)

        except Exception as e:
            print("View Error:", e)
        self.disconnect()

    def update_bill(self, billid, appointmentid, billdate, totalamount, paymentmode):
        self.connect()
        try:
            self.cursor.execute(
                "EXEC prcUpdateBill ?, ?, ?, ?, ?",
                billid, appointmentid, billdate, totalamount, paymentmode
            )
            self.conn.commit()
            print("Bill updated successfully.")
        except Exception as e:
            print("Update Error:", e)
        self.disconnect()

    def delete_bill(self, billid):
        self.connect()
        try:
            self.cursor.execute("EXEC prcDeleteBill ?", billid)
            self.conn.commit()
            print("Bill deleted successfully.")
        except Exception as e:
            print("Delete Error:", e)
        self.disconnect()