from connection import DBConnection


class Membership(DBConnection):

    def insert_membership(self, membershipname, durationmonths, price, description):
        self.connect()
        try:
            self.cursor.execute(
                "EXEC prcInsertMembership ?, ?, ?, ?",
                membershipname, durationmonths, price, description
            )
            self.conn.commit()
            print("Membership inserted successfully.")
        except Exception as e:
            print("Insert Error:", e)
        self.disconnect()

    def view_membership(self):
        self.connect()
        try:
            self.cursor.execute("EXEC prcSelectMembership")
            rows = self.cursor.fetchall()

            print("\nMembership List")
            for row in rows:
                print(row)

        except Exception as e:
            print("View Error:", e)
        self.disconnect()

    def update_membership(self, membershipid, membershipname, durationmonths, price, description):
        self.connect()
        try:
            self.cursor.execute(
                "EXEC prcUpdateMembership ?, ?, ?, ?, ?",
                membershipid, membershipname, durationmonths, price, description
            )
            self.conn.commit()
            print("Membership updated successfully.")
        except Exception as e:
            print("Update Error:", e)
        self.disconnect()

    def delete_membership(self, membershipid):
        self.connect()
        try:
            self.cursor.execute(
                "EXEC prcDeleteMembership ?",
                membershipid
            )
            self.conn.commit()
            print("Membership deleted successfully.")
        except Exception as e:
            print("Delete Error:", e)
        self.disconnect()