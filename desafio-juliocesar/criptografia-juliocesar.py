import requests
import json
import string
import hashlib

#My Token from Codenation
my_token = ''

# Request HTTP 
r = requests.get('https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token={token}'.format(token=my_token))
res_json = r.json()

# Create file .json
with open('answer.json', 'w') as json_file:
    json.dump(res_json, json_file, indent=2)

# Get the value from keys from the JSON
cifrado = res_json['cifrado']
numero_casas = res_json['numero_casas']

# Use the Alphabet from a to z
alphabet = string.ascii_lowercase 

#Create Function to decrypt the message
def decrypt(encrypted, rotation):
    result = ''
    for letter in encrypted:
        if letter in alphabet:
            position = alphabet.find(letter)
            position = (position - rotation) % 26
            result += alphabet[position]
        else:
            result += letter
    return result

# Use the Function to get the result 
decifrado = decrypt(cifrado, numero_casas)

# Update the .json file with new data for a Key
with open('answer.json', 'r') as json_file:
    new_data = json.load(json_file)
    new_data['decifrado'] = decifrado

with open('answer.json', 'w') as json_file:
    json_file.write(json.dumps(new_data, indent=2))

# 
resumo_criptografico = hashlib.sha1(str(decifrado).encode('utf-8')).hexdigest()

# Update the .json file again with new data for another Key
with open('answer.json', 'r') as json_file:
    new_data = json.load(json_file)
    new_data['resumo_criptografico'] = resumo_criptografico

with open('answer.json', 'w') as json_file:
    json_file.write(json.dumps(new_data, indent=2))

# Post the answer to Codenation as a multipart/form-data
r = requests.post(
    'https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token={token}'.format(token=my_token), 
    files={'answer': open('answer.json', 'rb')}
)

