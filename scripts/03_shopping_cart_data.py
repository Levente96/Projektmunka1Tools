import random
import json
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker

engine = db.create_engine("mysql+pymysql://projektmunka:projektmunka@localhost/projektmunka")
connection = engine.connect()
Session = sessionmaker(bind=engine)
session = Session()
metadata = db.MetaData()
table = db.Table('Shopping_cart', metadata, autoload=True, autoload_with=engine)
modell = db.Table('modell', metadata, autoload=True, autoload_with=engine)
all_data = session.query(table).count()
cart_no = 56133
modell_no = session.query(modell).count()

while all_data < 800000:
    item_types = random.randint(1, 10)

    item_numbers = [0] * item_types
    for i in range(item_types):
        item_numbers[i] = random.randint(1, 20)
    
    for item in item_numbers:
        rand = random.randint(1, modell_no)
        # print("{} {} {}".format(cart_no, rand, item))
        query = db.insert(table).values(CART_ID=cart_no,
                                        MODELL_ID=rand,
                                        QUANTITY=item) 
        result = connection.execute(query)
        all_data += 1
        if all_data % 10 == 0:
            print("{}/800000".format(all_data))
    cart_no += 1
print("Done!")
