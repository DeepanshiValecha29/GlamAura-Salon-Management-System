from connection import DBConnection


class Employee(DBConnection):

    def insert_employee(self, employeename, role, phone, salary):
        self.connect()
        try:
            self.cursor.execute(
                "EXEC prcInsertEmployee ?, ?, ?, ?",
                employeename, role, phone, salary
            )
            self.conn.commit()
            print("Employee inserted successfully.")
        except Exception as e:
            print("Insert Error:", e)
        finally:
            self.disconnect()

    def view_employee(self):
        self.connect()
        try:
            self.cursor.execute("EXEC prcSelectEmployee")
            rows = self.cursor.fetchall()
            return rows
        except Exception as e:
            print("View Error:", e)
            return []
        finally:
            self.disconnect()

    def update_employee(self, employeeid, employeename, role, phone, salary):
        self.connect()
        try:
            self.cursor.execute(
                "EXEC prcUpdateEmployee ?, ?, ?, ?, ?",
                employeeid, employeename, role, phone, salary
            )
            self.conn.commit()
            print("Employee updated successfully.")
        except Exception as e:
            print("Update Error:", e)
        finally:
            self.disconnect()

    def delete_employee(self, employeeid):
        self.connect()
        try:
            self.cursor.execute(
                "EXEC prcDeleteEmployee ?",
                employeeid
            )
            self.conn.commit()
            print("Employee deleted successfully.")
        except Exception as e:
            print("Delete Error:", e)
        finally:
            self.disconnect()