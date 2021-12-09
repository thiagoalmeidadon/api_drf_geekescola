import requests, json, os

#GET Avaliações 
URL_AVALIACOES = 'http://localhost:8000/api/v2/avaliacoes/'
avaliacoes = requests.get(URL_AVALIACOES)
print(avaliacoes.status_code)
print(avaliacoes.json())

#POST Avaliações
avaliacao_curso_1 = {
        "curso": 1,
        "nome": "SILVA",
        "email" : "emailunico23@email.com",
        "comentario": "bom demais, mesmo em, showww!",
        "avaliacao": "5.0"
}

token = f'Token {os.getenv("TOKEN")}'
headers = {'Authorization' : token }

avaliacoes_post = requests.post(URL_AVALIACOES, avaliacao_curso_1, headers=headers) 
print(avaliacoes_post.status_code)
print(avaliacoes_post.json())