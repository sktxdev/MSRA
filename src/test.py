################################################################################################
# Fetch Stored Procs to be tested
#
#   GetBatteryGasProduction
#
################################################################################################

import requests
import json
# from argparse import Namespace


class DataMuseLookup():
    def lookup(self, words):

        url = 'https://api.datamuse.com/words?ml='+str(words)+'&max=5'

        resp  = requests.get(url)
        if resp.status_code == 200:
             return json.loads(resp.content.decode('utf-8'))
        else:
             print(resp.status_code)
             print(resp.content.decode('utf-8'))
        return resp.content.decode('utf-8')

    def format_output(self, jsonobject):
        for item in resp:
            print(item)



lookup = DataMuseLookup()

terms = ['accident', 'fender+bender', 'renew+policy', 'pranged+car']
for term in terms:
    resp = lookup.lookup(term)
    lookup.format_output(resp)
    print('\n');



