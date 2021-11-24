import sqlalchemy as db
import random

engine = db.create_engine("mysql+pymysql://projektmunka:projektmunka@localhost/projektmunka")
connection = engine.connect()
metadata = db.MetaData()
table = db.Table('3d_printer', metadata, autoload=True, autoload_with=engine)

printer_manufacturer_names = ["Creality", "Prusa", "Sidewinder", "Biqu"]
printer_model_names = ["3", "3v2", "3 Pro", "5", "5 Pro", "Sidewinder"]
printer_prices = [59000, 63000, 98000, 139000, 145000]
printer_flow = [7.5, 5.9, 9.2, 11.2]

print("Inserting 1250 data.")

for index in range(1,1251):
    query = db.insert(table).values(PRINTER_ID=index,MAINTAINER_ID=random.randint(1, 12), PRINTER_NAME="{}_{}".format(printer_manufacturer_names[random.randint(0, 3)], printer_model_names[random.randint(0, 5)]), PRINTER_PRICE=printer_prices[random.randint(0, 4)], PRINTER_FLOW=printer_flow[random.randint(0, 3)]) 
    result = connection.execute(query)
    # print("inserted: {}".format(index))
print("Done!")
