from __init__ import db

class Cookie(db.Model):
    __tablename__ = "Cookie"
    id = db.Column(db.Integer, primary_key=True)  #  Define a primary key column
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
        return {"id": self.id,"Cookie_name": self.Cookie_name, "image": self.image, "stock": self.stock, "price": self.price}

def init_cookies():
    # You can keep the rest of your code as is
    Cookie1 = Cookie(Cookie_name="cookie 1", image="image1.jpg", stock="100", price="2.00") #replace with real data
    Cookie2 = Cookie(Cookie_name="cookie 2", image="image2.jpg", stock="100", price="2.00")
    Cookie3 = Cookie(Cookie_name="cookie 3", image="image3.jpg", stock="100", price="2.00")

    db.session.add(Cookie1)
    db.session.add(Cookie2)
    db.session.add(Cookie3)

    db.session.commit()

# Ensure you have imported the necessary modules and configured your database connection before running this code.
