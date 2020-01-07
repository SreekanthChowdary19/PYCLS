import json
import requests


params={'q': 'requests+language:python'}

# Search GitHub's repositories for requests
response = requests.get('https://api.github.com/search/repositories', params)

# Inspect some attributes of the `requests` repository
json_response = response.json()
repository = json_response['items'][0]
print(f'Repository name: {repository["name"]}')  # Python 3.6+
print(f'Repository description: {repository["description"]}')  # Python 3.6+

"""
resp = requests.get('https://api.github.com')

resp = json.loads(resp.content)
print(resp['current_user_url'])
"""
"""

f = open('response.json', 'r')
data = f.read()
f.close()

#print(data['issues_url'])
print(type(data))

resp = json.loads(data)
print(type(resp))

for key in resp:
    if key == 'issues_url':
        print(resp[key])
        break
    else:
        print("Key is not available")
"""
