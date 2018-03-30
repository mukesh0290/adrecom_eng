import pymongo
from pymongo import MongoClient
import pandas as pd

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
#pprint.pprint(AgPrediction.find_one())
print('_*_'*20)
#pprint.pprint(Gnprediction.find_one())
print('_*_'*20)
#pprint.pprint(PredictionGn.find_one())


#load_all_data =[]  ###  list will  contain  all json files
#for all_info in db_my_col.find({}):load_all_data .append(all_info)

#####################################################################################################
agprediction_data =[]  # read dat from mongo db one by one and append to the list
for all_info in AgPrediction.find({}):
    agprediction_data.append(all_info)

# conver list items to Data frame
agprediction_df = pd.DataFrame(agprediction_data)
#print(agprediction_df.head())

#####################################################################################################
# read data from Gnprediction one by one append to list and convert to dat frame
Gnprediction_data=[]
for all_info in Gnprediction.find({}):
    Gnprediction_data.append(all_info)

#convert list to dat frame
gnprediction_df = pd.DataFrame(Gnprediction_data)
#print(gnprediction_df.head())

######################################################################################################
# read data from PredictionGn one by one and append to list and convert to data frame
PredictionGn_data=[]
for all_info in PredictionGn.find({}):
    PredictionGn_data.append(all_info)

predictiongn_df = pd.DataFrame(PredictionGn_data)
print(predictiongn_df.head())


print(predictiongn_df.shape)
print('*'*4)
print(gnprediction_df.shape)
print('*'*4)
print(agprediction_df.shape)

print(predictiongn_df.info)
print(agprediction_df.info)
print(gnprediction_df.info)

predictiongn_df =predictiongn_df.drop(['_id','uid','site','rcat','scat'],axis=1)
print(predictiongn_df.head())
print('*'*4)
gnprediction_df = gnprediction_df.drop(['_id','uid','site','rcat','scat'],axis=1)
print(gnprediction_df.head())
print('*'*4)
agprediction_df= agprediction_df.drop(['_id','uid','site','rcat','scat'],axis=1)
print(agprediction_df.head())

print(predictiongn_df.columns)

# get the count of unique values column wise for predictiongn_df
for i in predictiongn_df.loc[:,'ab':'pr']:
    print(i,":",predictiongn_df[i].unique(),"\n")
    print(i,":",len(predictiongn_df[i].unique()),"\n")

for i in predictiongn_df.loc[:,['sf', 'tc', 'tm', 'tr']]:
    print(i,":",predictiongn_df[i].unique(),"\n")
    print(i,":",len(predictiongn_df[i].unique()),"\n")

 # check nan count columnwise
print(predictiongn_df.isnull().sum())

# df = df.apply(lambda x:x.fillna(x.value_counts().index[0]))
# fillna with most frequesnt value
predictiongn_df= predictiongn_df.apply(lambda x: x.fillna(x.value_counts().index[0]))

# after imputing na with mode
predictiongn_df.isnull().sum()

for i in predictiongn_df.loc[:,'ab':'pr']:
    print(i,":",len(predictiongn_df[i].unique()))

for i in predictiongn_df.loc[:,['sf', 'tc', 'tm', 'tr']]:
    print(i,":",len(predictiongn_df[i].unique()))

# analysisng gnprediction_df dataset
print(gnprediction_df.columns, "\n")

# get the count of uniwue values column wise for predictiongn_df
for i in gnprediction_df.loc[:, 'ab':'pr']:
    print(i, ":", gnprediction_df[i].unique(), "\n")
    print(i, ":", len(gnprediction_df[i].unique()), "\n")

for i in gnprediction_df.loc[:, ['sf', 'tc', 'tm', 'tr']]:
    print(i, ":", gnprediction_df[i].unique(), "\n")
    print(i, ":", len(gnprediction_df[i].unique()), "\n")


# check nan count columnwise
gnprediction_df.isnull().sum()

# df = df.apply(lambda x:x.fillna(x.value_counts().index[0]))
# fillna with most frequesnt value
gnprediction_df= gnprediction_df.apply(lambda x: x.fillna(x.value_counts().index[0]))

# after imputing na with mode
gnprediction_df.isnull().sum()

for i in gnprediction_df.loc[:,'ab':'pr']:
    print(i,":",len(gnprediction_df[i].unique()))

for i in gnprediction_df.loc[:,['sf', 'tc', 'tm', 'tr']]:
    print(i,":",len(gnprediction_df[i].unique()))

# analysisng agprediction_df dataset
print(agprediction_df.columns, "\n")

# get the count of uniwue values column wise for predictiongn_df
for i in agprediction_df.loc[:, 'ab':'pr']:
    print(i, ":", agprediction_df[i].unique(), "\n")
    print(i, ":", len(agprediction_df[i].unique()), "\n")

for i in agprediction_df.loc[:, ['sf', 'tc', 'tm', 'tr']]:
    print(i, ":", agprediction_df[i].unique(), "\n")
    print(i, ":", len(agprediction_df[i].unique()), "\n")

# check nan count columnwise
print(agprediction_df.isnull().sum())

# df = df.apply(lambda x:x.fillna(x.value_counts().index[0]))
# fillna with most frequesnt value
agprediction_df= agprediction_df.apply(lambda x: x.fillna(x.value_counts().index[0]))

# after imputing na with mode
print(agprediction_df.isnull().sum())

for i in agprediction_df.loc[:,'ab':'pr']:
    print(i,":",len(agprediction_df[i].unique()))

for i in agprediction_df.loc[:,['sf', 'tc', 'tm', 'tr']]:
    print(i,":",len(agprediction_df[i].unique()))

