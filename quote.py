# Prints a quote using the zenquotes api : https://zenquotes.io/
# ! The separator is a NerdFonts character !
# -> Separator as an argument ?

import requests
api_url = 'https://zenquotes.io/api/random'
response = requests.get(api_url)
if response.status_code == requests.codes.ok:
    print('▍'+response.json()[0]['q']+'\n▍ '+response.json()[0]['a'])
    
else:
    print("Error:", response.status_code, response.text)
