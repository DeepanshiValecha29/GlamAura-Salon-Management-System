from connection import DBConnection


class Appointment(DBConnection):

    def insert_appointment(self, customerid, employeeid, serviceid, appointmentdate, appointmenttime, status):
        self.connect()
        try:
            self.cursor.execute(
                "EXEC prcInsertAppointment ?, ?, ?, ?, ?, ?",
                customerid, employeeid, serviceid,
                appointmentdate, appointmenttime, status
            )
            self.conn.commit()
            print("Appointment inserted successfully.")
        except Exception as e:
            print("Insert Error:", e)
        self.disconnect()

    def view_appointment(self):
        self.connect()
        try:
            self.cursor.execute("EXEC prcSelectAppointment")
            rows = self.cursor.fetchall()

            print("\nAppointment List")
            for row in rows:
                print(row)

        except Exception as e:
            print("View Error:", e)
        self.disconnect()

    def update_appointment(self, appointmentid, customerid, employeeid, serviceid, appointmentdate, appointmenttime, status):
        self.connect()
        try:
            self.cursor.execute(
                "EXEC prcUpdateAppointment ?, ?, ?, ?, ?, ?, ?",
                appointmentid, customerid, employeeid,
                serviceid, appointmentdate,
                appointmenttime, status
            )
            self.conn.commit()
            print("Appointment updated successfully.")
        except Exception as e:
            print("Update Error:", e)
        self.disconnect()

    def delete_appointment(self, appointmentid):
        self.connect()
        try:
            self.cursor.execute("EXEC prcDeleteAppointment ?", appointmentid)
            self.conn.commit()
            print("Appointment deleted successfully.")
        except Exception as e:
            print("Delete Error:", e)
        self.disconnect()