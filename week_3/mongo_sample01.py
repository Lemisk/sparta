from pymongo import MongoClient
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

# MongoDB에 insert 하기

# # 'users'라는 collection에 {'name':'bobby','age':21}를 넣습니다.
# db.users.insert_one({'name':'bobby','age':21})
# db.users.insert_one({'name':'kay','age':27})
# db.users.insert_one({'name':'john','age':30})

all_users = list(db.users.find())
# print(all_users)

condition_users = list(db.users.find({'age':19}))
# print(condition_users)
print(condition_users[0]['name'])

#수정하기
# db.people.update_many(찾을조건,{ '$set': 어떻게바꿀지 })
# db.users.update_many({'name':'bobby'},{'$set': {'age':19}})

db.users.delete_one({'name':'bobby'})

# # 참고) MongoDB에서 특정 조건의 데이터 모두 보기
# same_ages = list(db.users.find({'age':21}))

# print(all_users[0])         # 0번째 결과값을 보기
# print(all_users[0]['name']) # 0번째 결과값의 'name'을 보기

# for user in all_users:      # 반복문을 돌며 모든 결과값을 보기
#     print(user)