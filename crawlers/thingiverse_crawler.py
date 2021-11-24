import requests
import json
import sys
import argparse
import os.path
from collections import OrderedDict
import configparser


api_base = "https://api.thingiverse.com/"
config_file = "api_credentials.ini"
config = configparser.ConfigParser()
config.read(config_file)

api_token = config.get("Thingiverse", "api_token")

def collect(pages):
    for index in range(1, pages+1):
        rest_url = api_base+"search/?access_token="+api_token+"&type=things&sort=newest&per_page=100&page="+str(index)
        print(rest_url)
        crawl_json(rest_url, "newest.json")

def crawl_json(rest_url, file_name):

    s = requests.Session() 
    r = s.get(rest_url)
    data = r.json()
    try:
        file = open(file_name, "r")
        prev_data = json.load(file)
        data["hits"] = prev_data["hits"] + data["hits"]
        file.close()
    except Exception as error:
        print("{0}".format(error))

    file = open(file_name, "w")
    file.write(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False).encode('utf-8', errors='ignore'))
    file.close()

    f = open(file_name)
    stat = json.load(f)
    
    print("Downloaded " + str(len(stat["hits"]))  +" things!")
 

if __name__ == "__main__":
    collect(100000) # oldalanként 100; összesen 1M modell linkje és neve
