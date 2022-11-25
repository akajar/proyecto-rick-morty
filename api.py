from pymongo import MongoClient
import requests

URL = 'https://rickandmortyapi.com/api/character'
MONGO_URI_DATABASE_URI = "mongodb://localhost:27017/"

response = requests.get(URL)
data = response.json()
results = data['results']


client = MongoClient(MONGO_URI_DATABASE_URI)
db = client["db"]
col = db["results"]


op = col.insert_many(results)
