from __init__ import db

class Cookie(db.Model):
    __tablename__ = "Cookie"
    id = db.Column(db.Integer, primary_key=True)  # Define a primary key column
    Cookie_name = db.Column(db.String, nullable=False)
    image = db.Column(db.String, nullable=False)
    stock = db.Column(db.String, nullable=False)
    price = db.Column(db.String, nullable=False)

    def __init__(self, Cookie_name, image, stock, price):
        self.Cookie_name = Cookie_name
        self.image = image
        self.stock = stock
        self.price = price

    def to_dict(self):
        return {"Cookie_name": self.Cookie_name, "image": self.image, "stock": self.stock, "price": self.price}

def init_cookies():
    # You can keep the rest of your code as is
    Cookie1 = Cookie(Cookie_name="Double Chocolate Chip", image="https://stylesweet.com/wp-content/uploads/2022/08/DoubleChocolateChipCookies_featured.jpg", stock="100", price="4.99") #replace with real data
    Cookie2 = Cookie(Cookie_name="Snicker Doodle", image="https://cakemehometonight.com/wp-content/uploads/2021/12/Snickerdoodle-Cookies-FI.jpg", stock="100", price="5.99")
    Cookie3 = Cookie(Cookie_name="Choclate Chip", image="https://www.cookingclassy.com/wp-content/uploads/2014/06/chocolate-chip-cookie-16.jpg", stock="100", price="3.99")

    db.session.add(Cookie1)
    db.session.add(Cookie2)
    db.session.add(Cookie3)

    db.session.commit()

# Ensure you have imported the necessary modules and configured your database connection before running this code.
