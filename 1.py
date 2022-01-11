import requests
r = requests.get('https://github.com/solitariaa/cmput404-lab1/blob/main/1.py')
print(r.text)
