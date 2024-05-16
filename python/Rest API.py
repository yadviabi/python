## Rest API
import requests
import pytest
import http 
import token
import json 
import types

def get():
    url=("https://gorest.co.in/public/v2/posts")
    response=requests.get(url=url)
    data=response.json()
    print(response.status_code)
    print(requests.head)

def post():

    head={
        
        'Content-Type':'application/json'

        }
    json_file=open('./new.json')
    payload=json.load(json_file)

   
    url=("https://gorest.co.in/public/v2/users")
    response=requests.post(url=url,headers=head,json=payload)
    data=response.json()
    print(response.status_code)
    print(response.json())
    payload = response.json()
    print(response)

def put():
    response=requests.get("https://gorest.co.in/public/v2/comments")
    print(response.status_code)
    print(response.json())
    print(response)

    head = {
            'Content-Type': 'application/json'
        }

    body_data = {
        "id": 1001002,
        "user_id":1234553,
        "title": "put.",
        "body": "new one"
      }

    response_put=requests.put("https://gorest.co.in/public/v2/comments", headers=head, json=body_data)
    print(response_put.status_code)
    print(response_put.json())


def delete():
    r =requests.delete('https://gorest.co.in/public/v2/todos/public/v2/users/2934536') 
    print(r.text) 
    print(r.status_code)
   


##method call
get()  
post()  
put()
delete()