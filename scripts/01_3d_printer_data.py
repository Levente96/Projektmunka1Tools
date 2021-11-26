import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
import random

engine = db.create_engine("mysql+pymysql://projektmunka:projektmunka@localhost/projektmunka")
connection = engine.connect()
metadata = db.MetaData()
Session = sessionmaker(bind=engine)
session = Session()
table = db.Table('3d_printer', metadata, autoload=True, autoload_with=engine)
table_count = session.query(table).count()
_max_data = 1250

printer_manufacturer_names = ["Creality", "Prusa", "Sidewinder", "Biqu"]
printer_model_names = ["3", "3v2", "3 Pro", "5", "5 Pro", "Sidewinder"]
printer_prices = [59000, 63000, 98000, 139000, 145000]
printer_flow = [7.5, 5.9, 9.2, 11.2, 13.4]

for index in range(table_count+1,_max_data+1):
    quality = random.randint(0, 4)
    query = db.insert(table).values(PRINTER_ID=index,
                                    MAINTAINER_ID=random.randint(1, 12),
                                    PRINTER_NAME="{}_{}".format(printer_manufacturer_names[random.randint(0, 3)], printer_model_names[random.randint(0, 5)]),
                                    PRINTER_PRICE=printer_prices[quality],
                                    PRINTER_FLOW=printer_flow[quality]) 
    result = connection.execute(query)

    if index % 10 == 0:
        print("{}/{}".format(index, _max_data))

print("Done!")
