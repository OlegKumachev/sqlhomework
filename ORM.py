import json
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from models import create_tables, Publisher, Shop, Book, Stock, Sale


DSN = "postgresql://postgres:postgres@localhost:5432/database"
engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()


def load_json():
    with open('tests_data.json') as fd:
        data = json.load(fd)
    for record in data:
        model = {
            'publisher': Publisher,
            'shop': Shop,
            'book': Book,
            'stock': Stock,
            'sale': Sale,
        }[record.get('model')]

        session.add(model(id=record.get('pk'), **record.get('fields')))
    session.commit()


def get_data():
    id_name = input('Введите данные издателя: ')
    if id_name.isdigit():
        req = session.query(Book.title, Shop.name, Sale.price, Sale.date_sale). \
            filter(Sale.id_stock == Stock.id).filter(Shop.id == Stock.id_shop). \
            filter(Book.id == Stock.id_book).filter(Publisher.id == Book.id_publisher).\
            filter(Publisher.id == id_name)
        for с in req.all():
            print(f' {с.title:<40}|  {с.name: <10}| {с.price:<5} | {с.date_sale}')
    else:
        req = session.query(Shop.name, Book.title, Sale.price, Sale.date_sale). \
            filter(Sale.id_stock == Stock.id).filter(Shop.id == Stock.id_shop). \
            filter(Book.id == Stock.id_book).filter(Publisher.id == Book.id_publisher). \
            filter(Publisher.name.like(f'%{id_name}%'))
        for с in req.all():
            print(f' {с.title:<40}|  {с.name: <10}| {с.price:<5} | {с.date_sale}')


session.close()


if __name__ == '__main__':
    load_json()
    get_data()
