import random
import json
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker

engine = db.create_engine("mysql+pymysql://projektmunka:projektmunka@localhost/projektmunka")
connection = engine.connect()
Session = sessionmaker(bind=engine)
session = Session()
metadata = db.MetaData()
table = db.Table('shipping_info', metadata, autoload=True, autoload_with=engine)
table_count = session.query(table).count()
_max_data = 5000

all_addresses = open("addresses.json", "r")
addresses_json = json.load(all_addresses)
num_addresses = len(addresses_json["addresses"])

for index in range(table_count+1,_max_data+1):
    address = addresses_json["addresses"][random.randint(0, num_addresses-1)]
    query = db.insert(table).values(SHIPPING_INFO_ID=index+1,
                                    COUNTRY=address["state"],
                                    CITY=address["city"] if "city" in address  else "Unknown",
                                    STREET=address["address1"],
                                    STREET_NO=address["postalCode"],
                                    OTHER=address["address2"]) 
    result = connection.execute(query)
    print("{}/{}".format(index, _max_data))

print("Done!")