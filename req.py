from requests import request

def get():
    r = request(method='post',url='http://127.0.0.1:8000/api/alternativa/2',json={

        'alternativa':'base X altura',
        'certo':False,
        'questao':'2'
    })
    print(r.json())

get()