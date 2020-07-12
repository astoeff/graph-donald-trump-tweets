import requests
import pymongo
from constants import (DATABASE_URL, DATABASE_NAME, URL_WITH_DATA_PREFIX, URL_WITH_DATA_SUFFIX,
                       TWEETS_YEARS, COLLECTION_NAMES, CORRECT_INSERTION_TEXT, ALREADY_INSERTED_TEXT)


def setup():
    myclient = pymongo.MongoClient(DATABASE_URL)
    mydb = myclient[DATABASE_NAME]

    collection_number = 0
    for year in TWEETS_YEARS:
        request_url = URL_WITH_DATA_PREFIX + year + URL_WITH_DATA_SUFFIX
        r = requests.get(request_url)
        data = r.json()

        if COLLECTION_NAMES[collection_number] not in mydb.list_collection_names():
            collection = mydb[COLLECTION_NAMES[collection_number]]
            collection.insert_many(data)
            collection_number += 1
            print(year + CORRECT_INSERTION_TEXT)
        else:
            print(year + ALREADY_INSERTED_TEXT)


if __name__ == '__main__':
    setup()
