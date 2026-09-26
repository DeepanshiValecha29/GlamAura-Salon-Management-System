from connection import DBConnection


class Product(DBConnection):

    def insert_product(self, productname, brand, price, stock):
        self.connect()
        try:
            self.cursor.execute(
                "EXEC prcInsertProduct ?, ?, ?, ?",
                productname, brand, price, stock
            )
            self.conn.commit()
            print("Product inserted successfully.")
        except Exception as e:
            print("Insert Error:", e)
        self.disconnect()

    def view_product(self):
        self.connect()
        try:
            self.cursor.execute("EXEC prcSelectProduct")
            rows = self.cursor.fetchall()

            print("\nProduct List")
            for row in rows:
                print(row)

        except Exception as e:
            print("View Error:", e)
        self.disconnect()

    def update_product(self, productid, productname, brand, price, stock):
        self.connect()
        try:
            self.cursor.execute(
                "EXEC prcUpdateProduct ?, ?, ?, ?, ?",
                productid, productname, brand, price, stock
            )
            self.conn.commit()
            print("Product updated successfully.")
        except Exception as e:
            print("Update Error:", e)
        self.disconnect()

    def delete_product(self, productid):
        self.connect()
        try:
            self.cursor.execute("EXEC prcDeleteProduct ?", productid)
            self.conn.commit()
            print("Product deleted successfully.")
        except Exception as e:
            print("Delete Error:", e)
        self.disconnect()