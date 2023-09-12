import requests


cepRequest = requests.get("https://viacep.com.br/ws/53050260/json/")

print(cepRequest.json())
