import random
import json
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker

engine = db.create_engine("mysql+pymysql://projektmunka:projektmunka@localhost/projektmunka")
connection = engine.connect()
Session = sessionmaker(bind=engine)
session = Session()
metadata = db.MetaData()
table = db.Table('orders', metadata, autoload=True, autoload_with=engine)
customer = db.Table('customer', metadata, autoload=True, autoload_with=engine)
printers = db.Table('3d_printer', metadata, autoload=True, autoload_with=engine)
carts = db.Table('shopping_cart', metadata, autoload=True, autoload_with=engine)
models = db.Table('modell', metadata, autoload=True, autoload_with=engine)

all_data = session.query(table).count()
all_customer = session.query(customer).count()
all_printers = session.query(printers).count()
all_carts = session.query(carts).order_by(carts.c.CART_ID.desc()).first()[0]

firstnames_file = open("firstnames.json", "r")
firstnames = json.load(firstnames_file)
fname_length = len(firstnames)

lastnames_file = open("lastnames.json", "r")
lastnames = json.load(lastnames_file)
lname_length = len(lastnames)

printer_flow = [7.5, 5.9, 9.2, 11.2]

while all_data < 900000:
    plastic = random.randint(1, 3)
    cart = random.randint(1, all_carts-1)
    order_sum = 0

    for row in session.query(carts).filter(carts.c.CART_ID == cart).all():
            item = session.query(models).filter(models.c.MODELL_ID == row[1]).one()
            order_sum += item["MODELL_PRICE"]*row[2]
    
    query = db.insert(table).values(ORDER_ID=all_data+1,
                                    CUSTOMER_ID=random.randint(1, all_customer),
                                    PRINTER_ID=random.randint(1, all_printers),
                                    PLASTIC_TYPE=plastic,
                                    CART_ID=cart,
                                    ORDER_PRICE=order_sum,
                                    PRIORITY=printer_flow[random.randint(0, 3)],
                                    MANUFACTURED='\x01' if random.randint(0, 1) == 0 else '\x00',
                                    SHIPPED='\x01' if random.randint(0, 1) == 0 else '\x00',
                                    DELIVERED = '\x01' if random.randint(0, 1) == 0 else '\x00',
                                    FAILED='\x00') 
    result = connection.execute(query)
    all_data += 1
    if all_data % 10 == 0:
        print("{}/900000".format(all_data))
print("Done!")
