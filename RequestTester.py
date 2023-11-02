import requests
import json


existingPageIds = []
currentId = 100100 ## inicial ID

while currentId <= 102000:
    try:
        response = requests.get(f'https://kb.daxoptimizer.com/d/{currentId}')
        response.raise_for_status()

        existingPageIds.append(currentId)
        print(f'Found page with id {currentId}')
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            print(f'Page with id {currentId} not found')

    currentId += 1

with open('existingPageIds.json', 'w') as file:
    json.dump({'ids': existingPageIds}, file, indent=2)
