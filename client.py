'''
Simple REST Client
send a put request to REST server and obtain a response message
'''

from requests import put, get
msg = get('http://localhost:5000').json()
print('msg get:\n{}'.format(msg))

data={'filename':'test.jpg'}  # filename uploaded to server
print('data put:\n{}'.format(data))

msgPut = put('http://localhost:5000', data=data).json()
print('msg get from data put:\n{}'.format(msgPut))
