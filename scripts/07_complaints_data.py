import random
import json
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker

engine = db.create_engine("mysql+pymysql://projektmunka:projektmunka@localhost/projektmunka")
connection = engine.connect()
Session = sessionmaker(bind=engine)
session = Session()
metadata = db.MetaData()

all_data = 0
table = db.Table('complaints', metadata, autoload=True, autoload_with=engine)
orders = db.Table('orders', metadata, autoload=True, autoload_with=engine)
all_orders = session.query(orders).count()

reasons = ["Print quality issues", "Size does not match",
           "Color does not match", "Delivery was late",
           "Print not strong enough", "Changed mind", "No reason"]

while all_data < 12000:
    order = random.randint(1, all_orders)
    o = session.query(orders).filter_by(ORDER_ID=order).first()
    o.FAILED = True
    session.commit()

    query = db.insert(table).values(COMPLAINT_ID=all_data+1,
                                    ORDER_ID=order,
                                    REASON=reasons[random.randint(0, len(reasons)-1)]
                                    ) 
    result = connection.execute(query)
    all_data += 1
    if all_data % 10 == 0:
        print("{}/12000".format(all_data))
print("Done!")
