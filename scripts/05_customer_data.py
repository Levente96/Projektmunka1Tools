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
shipping = db.Table('Shipping_info', metadata, autoload=True, autoload_with=engine)

all_data = session.query(table).count()
all_shipping = session.query(shipping).count()

firstnames_file = open("firstnames.json", "r")
firstnames = json.load(firstnames_file)
fname_length = len(firstnames)

lastnames_file = open("lastnames.json", "r")
lastnames = json.load(lastnames_file)
lname_length = len(lastnames)

while all_data < 7000:
    bank_card = ""
    for i in range(16):
        bank_card += str(random.randint(0, 9))
    query = db.insert(table).values(CUSTOMER_ID=all_data+1,
                                    CUSTOMER_NAME="{} {}".format(firstnames[random.randint(0, fname_length-1)], lastnames[random.randint(0, lname_length-1)]),
                                    SHIPPING_INFO_ID=all_shipping,
                                    BANK_CARD_INFO=bank_card) 
    result = connection.execute(query)
    all_data += 1
    if all_data % 10 == 0:
        print("{}/7000".format(all_data))
print("Done!")
