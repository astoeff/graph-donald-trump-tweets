import pymongo
from constants import (DATABASE_URL, DATABASE_NAME, LAST_TWEET_YEAR, LAST_COLLECTION_NAME,
                       CORRECT_INSERTION_TEXT, DATABASE_NEEDS_SETUP_WARNING)
from setup import get_data_in_json_for_given_year


def update():
    myclient = pymongo.MongoClient(DATABASE_URL)
    mydb = myclient[DATABASE_NAME]
    year_to_update = LAST_TWEET_YEAR

    if LAST_COLLECTION_NAME in mydb.list_collection_names():
        collection = mydb[LAST_COLLECTION_NAME]
        collection.drop()

        data = get_data_in_json_for_given_year(year_to_update)
        collection.insert_many(data)
        print(year_to_update + CORRECT_INSERTION_TEXT)
    else:
        print(DATABASE_NEEDS_SETUP_WARNING)


if __name__ == '__main__':
    update()
