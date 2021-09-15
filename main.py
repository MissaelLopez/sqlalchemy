import db
from model import Product

def run():
    arroz = Product('Arroz', 1.25)
    db.session.add(arroz)
    print(arroz.id)
    agua = Product('Agua', 0.3)
    db.session.add(agua)
    db.session.commit()
    print(arroz.id)

if __name__ == '__main__':
    db.Base.metadata.create_all(db.engine)
    run()