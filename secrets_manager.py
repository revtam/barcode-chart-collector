import json


with open('secrets.json') as f:
    data = json.load(f)
    
class Api_keys:
    okex_public = data["okex"]["api_key"]
    okex_private = data["okex"]["private_key"]
    okex_passphrase = data["okex"]["passphrase"]

    kucoin_public = data["kucoin"]["api_key"]
    kucoin_private = data["kucoin"]["private_key"]
    kucoin_passphrase = data["kucoin"]["passphrase"]