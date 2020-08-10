import pymongo as p

client=p.MongoClient("mongodb://localhost:27017/")

db=client['vendor']
details=db.details
print(client.list_database_names())
for d in details.find():
    print(d['password'])