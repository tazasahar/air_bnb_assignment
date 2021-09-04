import pymongo

connection = pymongo.MongoClient("class-mongodb.cims.nyu.edu", 27017,
                                username="ms11831",
                                password="EGWx53gx",
                                authSource="ms11831")
collection = connection["ms11831"]["listings"]

# the collection variable will be a reference to your collection
docs = collection.find({
    "beds":{"$gt": 2},
    "neighbourhood_cleansed":"Surf Coast","review_scores_rating": {"$ne": ""}}, {"_id":0,"name":1,"beds":1,"review_scores_rating":1,"price":1}).sort({"review_scores_rating": -1})

for doc in docs:
    print(doc)