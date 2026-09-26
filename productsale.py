from connection import DBConnection


class ProductSale(DBConnection):

    def insert_productsale(self, billid, productid, quantity, rate):
        self.connect()
        try:
            self.cursor.execute(
                "EXEC prcInsertProductSale ?, ?, ?, ?",
                billid, productid, quantity, rate
            )
            self.conn.commit()
            print("Product Sale inserted successfully.")
        except Exception as e:
            print("Insert Error:", e)
        self.disconnect()

    def view_productsale(self):
        self.connect()
        try:
            self.cursor.execute("EXEC prcSelectProductSale")
            rows = self.cursor.fetchall()

            print("\nProduct Sale List")
            for row in rows:
                print(row)

        except Exception as e:
            print("View Error:", e)
        self.disconnect()

    def update_productsale(self, productsaleid, billid, productid, quantity, rate):
        self.connect()
        try:
            self.cursor.execute(
                "EXEC prcUpdateProductSale ?, ?, ?, ?, ?",
                productsaleid, billid, productid, quantity, rate
            )
            self.conn.commit()
            print("Product Sale updated successfully.")
        except Exception as e:
            print("Update Error:", e)
        self.disconnect()

    def delete_productsale(self, productsaleid):
        self.connect()
        try:
            self.cursor.execute(
                "EXEC prcDeleteProductSale ?",
                productsaleid
            )
            self.conn.commit()
            print("Product Sale deleted successfully.")
        except Exception as e:
            print("Delete Error:", e)
        self.disconnect()