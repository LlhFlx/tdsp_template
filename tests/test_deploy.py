import requests

model_url = "https://tdsptemplate-production.up.railway.app" # Agregue acá la url de railway
path = 'predict'
r = requests.post(f"{model_url}/{path}", json={"words": ["lord", "day"]})
print(r.json())