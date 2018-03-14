import pymongo
from pymongo import MongoClient

client =MongoClient()
# client = MongoClient('localhost', 27017)
# client = MongoClient('mongodb://localhost:27017/')

db = client.adrecom
# db = client['adrecom']

AgPrediction = db.AgPrediction
# collection =db['AgPrediction']
Gnprediction = db.Gnprediction

PredictionGn= db.predictiongn

#print(collection)
import pprint
pprint.pprint(AgPrediction.find_one())
print('_*_'*20)
pprint.pprint(Gnprediction.find_one())
print('_*_'*20)
pprint.pprint(PredictionGn.find_one())
