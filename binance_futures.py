import logging
import requests
import pprint
import json

logger = logging.getLogger()




def get_contracts(count=10):
    response = requests.get("https://testnet.binancefuture.com/fapi/v1/exchangeInfo")
    print(response.status_code)
    # pprint.pprint(response.json()['symbols'][0])
    contracts = []
    for contract in response.json()['symbols']:
        # pprint.pprint(contract)
        contracts.append(contract['pair'])
        # pprint.pprint(contracts)
    return contracts[:count]  

# print(get_contracts())