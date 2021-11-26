import random
import json
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker

engine = db.create_engine("mysql+pymysql://projektmunka:projektmunka@localhost/projektmunka")
connection = engine.connect()
Session = sessionmaker(bind=engine)
session = Session()
metadata = db.MetaData()
table = db.Table('shopping_cart', metadata, autoload=True, autoload_with=engine)
table_count = session.query(table).count()
_max_data = 800000

modell = db.Table('modell', metadata, autoload=True, autoload_with=engine)
modell_count = session.query(modell).count()

# a legutolso cart_id utantol kezdjuk beilleszteni az ujakat
cart_no = session.query(table).order_by(table.c.CART_ID.desc()).first()[0]+1 if table_count > 0 else 1

while table_count < _max_data:
    item_types = random.randint(1, 5)
    item_numbers = [0] * item_types

    for i in range(item_types):
        item_numbers[i] = random.randint(1, 3)
    
    for item in item_numbers:
        rand = random.randint(1, modell_count)
        query = db.insert(table).values(CART_ID=cart_no,
                                        MODELL_ID=rand,
                                        QUANTITY=item) 
        result = connection.execute(query)
        table_count += 1
        if table_count % 10 == 0:
             print("{}/{}".format(table_count, _max_data))
    cart_no += 1
print("Done!")
