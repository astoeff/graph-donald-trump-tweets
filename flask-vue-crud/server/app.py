from flask import Flask
from flask_cors import CORS
import pymongo

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from constants import (COLLECTION_NAMES, DATABASE_URL, DATABASE_NAME, RETURNED_DATA_TO_SERVER_SEPARATOR,
                       REQUEST_GET_METHOD, RUSSIA_WORD_FOR_SEARCH_IN_TWEETS, URL_FOR_RESULTS_BY_YEAR_SUFFIX,
                       URL_FOR_RESULTS_BY_DAY_SUFFIX, URL_FOR_RESULTS_FOR_RUSSIA_IN_TWEETS_SUFFIX, DATE_FIELD,
                       SELECT_BY_REGEX, TEXT_FIELD, LIST_OF_DAYS_IN_DATE)

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
@app.route(URL_FOR_RESULTS_BY_YEAR_SUFFIX, methods=[REQUEST_GET_METHOD])
def tweets_count_by_year():
    myclient = pymongo.MongoClient(DATABASE_URL)
    mydb = myclient[DATABASE_NAME]
    tweets_count_for_years = [str(mydb[i].count()) for i in COLLECTION_NAMES]
    returned_result = RETURNED_DATA_TO_SERVER_SEPARATOR.join(tweets_count_for_years)
    return returned_result


def get_list_of_tweets_count_per_day_of_week_in_given_collections(collections):
    list_of_tweets_count_per_day_of_week = []
    for day in LIST_OF_DAYS_IN_DATE:
        current_day_of_week_tweets_count = sum([i.find({DATE_FIELD: {SELECT_BY_REGEX: day}}).
                                               count() for i in collections])
        list_of_tweets_count_per_day_of_week.append(current_day_of_week_tweets_count)
    return list_of_tweets_count_per_day_of_week


@app.route(URL_FOR_RESULTS_BY_DAY_SUFFIX, methods=[REQUEST_GET_METHOD])
def tweets_count_by_day():
    myclient = pymongo.MongoClient(DATABASE_URL)
    mydb = myclient[DATABASE_NAME]
    collections = [mydb[i] for i in COLLECTION_NAMES]
    result_list = get_list_of_tweets_count_per_day_of_week_in_given_collections(collections)
    result_data = RETURNED_DATA_TO_SERVER_SEPARATOR.join(str(i) for i in result_list)
    return result_data


def get_list_of_tweets_count_per_day_of_week_containing_given_word_in_collections(word_to_search, collections):
    list_of_tweets_count_per_day_of_week_containing_word = []
    for day in LIST_OF_DAYS_IN_DATE:
        current_day_of_week_tweets_containing_word_count = sum([i.find({DATE_FIELD: {SELECT_BY_REGEX: day},
                                                               TEXT_FIELD: {SELECT_BY_REGEX: word_to_search}}).
                                                               count() for i in collections])
        list_of_tweets_count_per_day_of_week_containing_word.append(current_day_of_week_tweets_containing_word_count)
    return list_of_tweets_count_per_day_of_week_containing_word


@app.route(URL_FOR_RESULTS_FOR_RUSSIA_IN_TWEETS_SUFFIX, methods=[REQUEST_GET_METHOD])
def russia():
    myclient = pymongo.MongoClient(DATABASE_URL)
    mydb = myclient[DATABASE_NAME]
    word_to_search = RUSSIA_WORD_FOR_SEARCH_IN_TWEETS
    collections = [mydb[i] for i in COLLECTION_NAMES]
    result_list = get_list_of_tweets_count_per_day_of_week_containing_given_word_in_collections(word_to_search,
                                                                                                collections)
    result_data = RETURNED_DATA_TO_SERVER_SEPARATOR.join(str(i) for i in result_list)
    return result_data


if __name__ == '__main__':
    app.run()
