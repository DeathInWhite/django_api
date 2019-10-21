import requests

headers = {}
headers['Authorization'] = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTcxNjcyNjkxLCJqdGkiOiJhMDRiNDg4MzM1NDE0YTIxOTIzNjA3YzkzMjhhMzg1MSIsInVzZXJfaWQiOjF9.6z8Ktjf0BMxMG0Z4jF_1bt_Nz1oTlOG0lgDtR8FmxuQ'

r = requests.get('http://localhost:8000/parading/',headers=headers)

print(r.text)