from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')

# cоздание словаря
Witcher = {
    'appid': 292030,
    'positive': 632627,
    'negative': 25245,


    'name': 'The Wither 3: Wild Hand',
    'developer': 'CD PROJECT RED',
    'publisher': 'CD PROJECT RED',
    'genre': 'RPG',
    'release_date': '2015/05/18',


    'tags': {
        'Open World': 11677,
        'RPG': 10024,
        'Story Rich': 9219,
        'Atmospheric': 6478,
        'Mature': 6234,
        'Fantasy': 6057
    }
}


# подключение к bd на сервере монго
db = client.Game

db.Witcher.insert_one(Witcher)

# найти все доументы в колекции witcher и вызвать их в консоль

for a in db.Witcher.find():
    print(a)
