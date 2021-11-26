import random
import json
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker

engine = db.create_engine("mysql+pymysql://projektmunka:projektmunka@localhost/projektmunka")
connection = engine.connect()
Session = sessionmaker(bind=engine)
session = Session()
metadata = db.MetaData()
table = db.Table('customer', metadata, autoload=True, autoload_with=engine)
table_count = session.query(table).count()
_max_data = 7000

shipping = db.Table('Shipping_info', metadata, autoload=True, autoload_with=engine)
all_shipping = session.query(shipping).count()

firstnames_file = open("firstnames.json", "r")
firstnames = json.load(firstnames_file)
fname_length = len(firstnames)

lastnames_file = open("lastnames.json", "r")
lastnames = json.load(lastnames_file)
lname_length = len(lastnames)

for index in range(table_count+1,_max_data+1):
    bank_card = None
    if random.randint(1, 10) == 8:  # 1 a 10bol ad meg bankkartya adatot
        bank_card = ""
        for i in range(16):
            bank_card += str(random.randint(0, 9))

    query = db.insert(table).values(CUSTOMER_ID=index,
                                    CUSTOMER_NAME="{} {}".format(firstnames[random.randint(0, fname_length-1)], lastnames[random.randint(0, lname_length-1)]),
                                    SHIPPING_INFO_ID=random.randint(1,all_shipping-1),
                                    BANK_CARD_INFO=bank_card) 
    result = connection.execute(query)
    if index % 100 == 0:
        print("{}/{}".format(index, _max_data))

print("Done!")
