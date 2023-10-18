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
    Cookie4 = Cookie(Cookie_name="cookie 4", image="image4.jpg", stock="100", price="2.00") #replace with real data
    Cookie5 = Cookie(Cookie_name="cookie 5", image="image5.jpg", stock="100", price="2.00")
    Cookie6 = Cookie(Cookie_name="cookie 6", image="image6.jpg", stock="100", price="2.00")
    db.session.add(Cookie1)
    db.session.add(Cookie2)
    db.session.add(Cookie3)
    db.session.add(Cookie4)
    db.session.add(Cookie5)
    db.session.add(Cookie6)
    
    db.session.commit()

# Ensure you have imported the necessary modules and configured your database connection before running this code.


# from __init__ import db

# class Song(db.Model):
#     __tablename__ = "Song"
#     id = db.Column(db.Integer, primary_key=True)  # Define a primary key column
#     character = db.Column(db.String, nullable=False)
#     song_name = db.Column(db.String, nullable=False)
#     artist = db.Column(db.String, nullable=False)
#     genre = db.Column(db.String, nullable=False)
#     def __init__(self, character, song_name, artist, genre):
#         self.character = character
#         self.song_name = song_name
#         self.artist = artist
#         self.genre = genre
#     def to_dict(self):
#         return {"character": self.character, "song_name": self.song_name, "artist": self.artist, "genre": self.genre}
# def initSongs():
#     # You can keep the rest of your code as is
#     song1 = Song(character="Walter White", song_name="Changes", artist="David Bowie", genre="Art Pop"); db.session.add(song1)#replace with real data
#     song2 = Song(character="Walter White", song_name="Back in Black", artist="AC/DC", genre="Hard Rock"); db.session.add(song2)
#     song3 = Song(character="Walter White", song_name="Baby Blue", artist="Badfinger", genre="Rock"); db.session.add(song3)
#     song4 = Song(character="Walter White", song_name="A Horse with No Name", artist="America", genre="Soft Rock"); db.session.add(song4)
#     db.session.commit()