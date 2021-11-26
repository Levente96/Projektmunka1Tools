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
table_count = session.query(table).count()
_max_data = 800000

customer = db.Table('customer', metadata, autoload=True, autoload_with=engine)
printers = db.Table('3d_printer', metadata, autoload=True, autoload_with=engine)
carts = db.Table('shopping_cart', metadata, autoload=True, autoload_with=engine)
models = db.Table('modell', metadata, autoload=True, autoload_with=engine)
plastics = db.Table('plastic', metadata, autoload=True, autoload_with=engine)

all_data = session.query(table).count()
customer_count = session.query(customer).count()
printer_count = session.query(printers).count()
plastics_count = session.query(plastics).count()
last_cart = session.query(carts).order_by(carts.c.CART_ID.desc()).first()[0]

plastic_prices = [9, 11, 12]

for index in range(table_count+1,_max_data+1):
    plastic = random.randint(1, plastics_count)
    cart = random.randint(1, last_cart)
    order_status = random.randint(0,3)
    order_priority = random.randint(1,3)
    order_sum = 300 *order_priority
    
    for row in session.query(carts).filter(carts.c.CART_ID == cart).all():
            item = session.query(models).filter(models.c.MODELL_ID == row[1]).one()
            order_sum += item["PLASTIC_REQUIRED"]*plastic_prices[plastic-1]*row[2] + item["LICENSE_FEE"]
    
    query = db.insert(table).values(ORDER_ID=index,
                                    CUSTOMER_ID=random.randint(1, customer_count),
                                    PRINTER_ID=random.randint(1, printer_count),
                                    PLASTIC_TYPE=plastic,
                                    CART_ID=cart,
                                    ORDER_PRICE=order_sum,
                                    ORDER_PRIORITY=order_priority,
                                    MANUFACTURED='\x01' if order_status >= 1 else '\x00',
                                    SHIPPED='\x01' if order_status >= 2 else '\x00',
                                    DELIVERED = '\x01' if order_status >= 3 else '\x00',
                                    FAILED='\x00') 
    result = connection.execute(query)
    if index % 100 == 0:
        print("{}/{}".format(index, _max_data))

print("Done!")
