from requests import request

class Request_test():
    def get_unauth():
        req = request("get",'http://127.0.0.1:8000/auth/edit/')
        print(req.json())
    
    def post_unauth():
        req = request("post",'http://127.0.0.1:8000/auth/edit/',json={
            'pk':'4',
            'username':'vitor',
            'email':'sapoalado070@gmail.com',
            'password':'victor070'},headers={
                'Content-Type':'application/json',
                'Authorization': 'Token 28cfdcf140478c54f3ea5dc3db5b23abe1058d04'
            }
            )
        print(req.json())

    def get_auth():
        req = request("get",'http://127.0.0.1:8000/api/tarefa/4',headers={
                'Content-Type':'application/json',
                'Authorization': 'Token 28cfdcf140478c54f3ea5dc3db5b23abe1058d04'
            })
        print(req.json())

    def post_auth():
        req = request("post",'http://127.0.0.1:8000/api/tarefa/4',json={
            'user':'4',
            'tarefa':'paralela',
            'feito':True},headers={
                'Content-Type':'application/json',
                'Authorization': 'Token 28cfdcf140478c54f3ea5dc3db5b23abe1058d04'
            }
            )
        print(req.json())
    
    def put_auth():
        req = request("put",'http://127.0.0.1:8000/auth/edit/',json={
            'pk':'4',
            'new_password':'victor070',
            'username':'vitor',
            'email':'sapoalado070@gmail.com',
            'password':'sapo'},headers={
                'Content-Type':'application/json',
                'Authorization': 'Token 28cfdcf140478c54f3ea5dc3db5b23abe1058d04'
            }
            )
        print(req.json())
    

Request_test.post_auth()