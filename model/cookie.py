from __init__ import app, db
from flask_login import UserMixin
from sqlalchemy.exc import IntegrityError
import os
import pandas as pd

# Cookie model
class Cookie(db.Model, UserMixin):
    __tablename__ = 'cookies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), unique=True, nullable=False)
    ingredients = db.Column(db.String(256), nullable=False)
    stock = db.Column(db.String(256), nullable=True)  # Assuming stock can be nullable
    image_name = db.Column(db.String(64), nullable=True)  # Assuming image_name can be nullable
    price = db.Column(db.String(256), nullable=True)  # Assuming price can be nullable

    def __init__(self, title, ingredients, stock, image_name, price):
        self.title = title
        self.ingredients = ingredients
        self.stock = stock
        self.image_name = image_name
        self.price = price

    def alldetails(self):
        return {
            "id": self.id,
            "title": self.title,
            "ingredients": self.ingredients,
            "stock": self.stock,  # Added stock
            "image_name": self.image_name,
            "price": self.price
        }

# Favorite mode
# Function to initialize cookies
def initCookies():
    with app.app_context():
        print("Creating cookie tables")
        db.create_all()
        if db.session.query(Cookie).count() > 0:
            return

        basedir = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(basedir, "../static/data/cookies.csv")
        df = pd.read_csv(file_path)

        print("Number of rows in CSV:", len(df))

        for index, row in df.iterrows():
            try:
                cookie = Cookie(
                    title=row['Title'],
                    ingredients=row['Ingredients'],
                    stock=row.get('Instructions', None),
                    image_name=row.get('Image_Name', None),
                    price=row.get('price', None)
                )

                db.session.add(cookie)
                db.session.commit()
            except IntegrityError:
                db.session.rollback()
                print(f"Duplicate cookie or error: {cookie.title}")
            except Exception as e:
                db.session.rollback()
                print(f"Error adding cookie at index {index}: {str(e)}")

if __name__ == "__main__":
    initCookies()