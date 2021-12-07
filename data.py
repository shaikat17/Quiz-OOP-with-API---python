import requests
import json

q_num = int(input("How Many Question You Want? "))
print('\n')

para = {
  "amount": q_num,
  "difficulty": "easy",
  "type": "boolean"
  }

response = requests.get('https://opentdb.com/api.php', params=para)

question_data = response.json()['results']
