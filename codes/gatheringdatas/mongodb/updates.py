## 몽고디비에서의 update와 추가적 사항을 해보기 


import pymongo as mg

client = mg.MongoClient(host='mongodb://localhost:27017')
database = client['study_data_analytics']
collection = database['collect_update'] # 테이블

# 여러 문서 삽입
documents = [
    {"name": "Alice", "age": 25, "city": "Seoul"},
    {"name": "Bob", "age": 30, "city": "Busan"},
    {"name": "Charlie", "age": 35, "city": "Incheon"}
]

# collection.insert_many(documents)

# 하나만 update 
collection.update_one({"name":"Alice"}, {"$set":{"age":26}})
# update를 looping 하는것보다 collection 새로운 곳에 집어 넣는게 더 편하다?