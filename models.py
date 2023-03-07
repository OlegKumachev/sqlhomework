
import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Publisher(Base):
    __tablename__ = "publisher"

    id_publisher = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=40), unique=True)


class Book(Base):
    __tablename__ = "book"

    id_book = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String(length=50), unique=True)
    id_publisher = sq.Column(sq.Integer, sq.ForeignKey("publisher.id_publisher"), nullable=False)

    publisher = relationship(Publisher, backref= "book")


class Shop(Base):
    __tablename__ = "shop"

    id_shop = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=50))

class Stok(Base):
    __tablename__ = "stok"

    id_stok = sq.Column(sq.Integer, primary_key=True)
    id_book = sq.Column(sq.Integer, sq.ForeignKey("book.id_book"), nullable=False)
    id_shop = sq.Column(sq.Integer, sq.ForeignKey("shop.id_shop"), nullable=False)
    count = sq.Column(sq.Integer)

    book = relationship(Book, backref="book")
    shop = relationship(Shop, backref="shop")


class Sale(Base):
    __tablename__ = "sale"

    id_sale = sq.Column(sq.Integer, primary_key=True)
    id_stok = sq.Column(sq.Integer, sq.ForeignKey("stok.id_stok"), nullable=False)
    data_sale = sq.Column(sq.Date)
    price = sq.Column(sq.Integer)
    count = sq.Column(sq.Integer)

    stok = relationship(Stok, backref="stok")

def create_tables(engine):
    Base.metadata.create_all(engine)


