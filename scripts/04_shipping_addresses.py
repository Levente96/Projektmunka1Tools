import random
import json
import sqlalchemy as db

engine = db.create_engine("mysql+pymysql://projektmunka:projektmunka@localhost/projektmunka")
connection = engine.connect()
metadata = db.MetaData()
table = db.Table('Shipping_info', metadata, autoload=True, autoload_with=engine)

all_addresses = open("addresses.json", "r")
addresses_json = json.load(all_addresses)
num_addresses = len(addresses_json["addresses"])

for index, address in enumerate(addresses_json["addresses"]):
    query = db.insert(table).values(SHIPPING_INFO_ID=index+1,
                                    COUNTRY=address["state"],
                                    CITY=address["city"] if "city" in address  else "Unknown",
                                    STREET=address["address1"],
                                    STREET_NO=address["postalCode"],
                                    OTHER=address["address2"]) 
    result = connection.execute(query)
    print("{}/{}".format(index+1, num_addresses))

print("Done!")
