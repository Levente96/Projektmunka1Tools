import random
import json
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker

engine = db.create_engine("mysql+pymysql://projektmunka:projektmunka@localhost/projektmunka")
connection = engine.connect()
Session = sessionmaker(bind=engine)
session = Session()
metadata = db.MetaData()
table = db.Table('complaints', metadata, autoload=True, autoload_with=engine)
table_count = session.query(table).count()
_max_data = 12000

orders = db.Table('orders', metadata, autoload=True, autoload_with=engine)
all_orders = session.query(orders).count()

reasons = ["Print quality issues", "Size does not match",
           "Color does not match", "Delivery was late",
           "Print not strong enough", "Changed mind", "No reason"]

for index in range(table_count+1,_max_data+1):
    order = random.randint(1, all_orders)
    update_query = orders.update().where(orders.c.ORDER_ID == order).values(FAILED = '\x01')
    engine.execute(update_query)
    query = db.insert(table).values(COMPLAINT_ID=index,
                                    ORDER_ID=order,
                                    REASON=reasons[random.randint(0, len(reasons)-1)]) 
    result = connection.execute(query)
    if index % 100 == 0:
        print("{}/{}".format(index, _max_data))

print("Done!")

