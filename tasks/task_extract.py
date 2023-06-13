import requests
import pandas as pd
import json, os

def task_extract():
    url_api = "https://api.bouyguestelecom.fr/ventes/produits?type=phone"
    header = {'Content-Type': 'application/json', 'x-version': '4'}

    req = requests.get(url_api, headers=header)
    req_json = req.json()

    if not os.path.exists("bouygues"):
        os.makedirs("bouygues")

    with open ("bouygues/bouygues.json", "w") as f:
        json.dump(req_json["produits"], f)
