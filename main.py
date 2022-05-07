import requests

link = 'https://minhaApi.perealvees.repl.co'

requisicao = requests.get(link)

print(requisicao)
print(requisicao.json())