import requests
model_url = "tdsptemplate-production.up.railway.app" # Agregue acá la url de railway

requests.post(model_url, json={"word": "lord"})
