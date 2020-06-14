from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

# 매트릭스의 평점 가져오기

rate = db.movies.find_one({'title':'매트릭스'})['star']

# print(rate)

# 매트릭스와 같은 평점 영화 가져오기
def getStarFromTitle(title):
    star = db.movies.find_one({"title": title})['star']
    return star

def getTitlesFromTitle(title):
    star = getStarFromTitle(title)
    movies = list(db.movies.find({"star": star}))
    titles = []
    for movie in movies:
        titles.append(movie['title'])
    return titles

for title in getTitlesFromTitle('매트릭스'):
    print(title)

# same_rate_movies = list(db.movies.find({'star': rate}))

# for movie in same_rate_movies:
#     print(movie['title'], rate)
