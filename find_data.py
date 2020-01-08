import requests
import json
response=requests.get("https://yandex.ru/maps/api/masstransit/getLine?ajax=1&collapsedSidebar=true&csrfToken=0f1063c3f3041945686d7465fc5c5743556a9e95:1578468142&lang=ru&lineId=2107048884&locale=ru_RU&sessionId=1578466678133_222391").text
dictionary=json.loads(response)
print(response)
