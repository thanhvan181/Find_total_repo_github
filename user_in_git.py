

import requests
import sys

user = sys.argv[1]
link_of_user = 'https://api.github.com/users/{}/repos'.format(user)
resp = requests.get(link_of_user)
repos = resp.json()
link = resp.headers.get('link', None)

while link is not None:
    try:
        resp = requests.get(resp.links['next']['url'])
        repos.extend(resp.json())
        link = resp.headers.get('link', None)
    except KeyError:
        break

names = [d['name'] for d in repos]
print(names)
print('So repo cua {} la: {}'.format(user, len(names)))
