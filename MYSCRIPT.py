import requests
response = requests.get("http://labs.bible.org/api/?passage=John+3:16-17")
print(response.content)