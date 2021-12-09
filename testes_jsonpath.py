import requests
import jsonpath

avaliacoes = requests.get('http://localhost:8000/api/v2/avaliacoes/')

resultados = jsonpath.jsonpath(avaliacoes.json(), 'results')

print(resultados)

#nome de todos os usuarios que avaliaram 
nomes = jsonpath.jsonpath(avaliacoes.json(), 'results[*].nome')
print(nomes)