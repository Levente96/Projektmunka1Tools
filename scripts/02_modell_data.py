import random
import json
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker

engine = db.create_engine("mysql+pymysql://projektmunka:projektmunka@localhost/projektmunka")
connection = engine.connect()
metadata = db.MetaData()
Session = sessionmaker(bind=engine)
session = Session()
table = db.Table('modell', metadata, autoload=True, autoload_with=engine)
table_count = session.query(table).count()
_max_data = 1000000

modellfile = open("model.json", "r")
jsondata = json.load(modellfile)
jsonsize = jsondata["total"]

licenses = [0, 200, 500, 1000, 1500]

for index in range(table_count+1,_max_data+1):
    weight = random.randint(2, 450)
    r = random.randint(0, jsonsize-1)
    query = db.insert(table).values(MODELL_ID=index,
                                    MODELL_NAME=jsondata["hits"][r]["name"],
                                    MODELL_LINK=jsondata["hits"][r]["public_url"],
                                    PLASTIC_REQUIRED=weight,
                                    LICENSE_FEE=licenses[random.randint(0, 4)]) 
    result = connection.execute(query)
    if index % 100 == 0:
        print("{}/{}".format(index, _max_data))

print("Done!")