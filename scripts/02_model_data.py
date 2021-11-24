import random
import json
import sqlalchemy as db

engine = db.create_engine("mysql+pymysql://projektmunka:projektmunka@localhost/projektmunka")
connection = engine.connect()
metadata = db.MetaData()
table = db.Table('modell', metadata, autoload=True, autoload_with=engine)

modellfile = open("model.json", "r")
jsondata = json.load(modellfile)
jsonsize = jsondata["total"]

licenses = [0, 200, 500, 1000, 1500]

for index in range(1,1000000):
    weight = random.randint(300, 100000)
    r = random.randint(0, jsonsize-1)
    query = db.insert(table).values(MODELL_ID=index,
                                    MODELL_NAME=jsondata["hits"][r]["name"],
                                    MODELL_PRICE=(weight*10) + (weight*2.5)*10,
                                    MODELL_LINK=jsondata["hits"][r]["public_url"],
                                    PLASTIC_REQUIRED=weight,
                                    LICENSE_FEE=licenses[random.randint(0, 4)]) 
    result = connection.execute(query)
    if index % 10000 == 0:
        print("inserted: {}".format(index))
