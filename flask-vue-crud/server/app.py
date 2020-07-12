from flask import Flask
from flask_cors import CORS
import pymongo

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from constants import (COLLECTION_NAMES, DATABASE_URL, DATABASE_NAME, RETURNED_DATA_TO_SERVER_SEPARATOR,
                       REQUEST_GET_METHOD, RUSSIA_WORD_FOR_SEARCH_IN_TWEETS, URL_FOR_RESULTS_BY_YEAR_SUFFIX,
                       URL_FOR_RESULTS_BY_DAY_SUFFIX, URL_FOR_RESULTS_FOR_RUSSIA_IN_TWEETS_SUFFIX, DATE_FIELD,
                       SELECT_BY_REGEX, TEXT_FIELD, MONDAY_IN_DATE, TUESDAY_IN_DATE, WEDNESDAY_IN_DATE,
                       THURSDAY_IN_DATE, FRIDAY_IN_DATE, SATURDAY_IN_DATE, SUNDAY_IN_DATE)

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


@app.route(URL_FOR_RESULTS_BY_DAY_SUFFIX, methods=[REQUEST_GET_METHOD])
def tweets_count_by_day():
    myclient = pymongo.MongoClient(DATABASE_URL)

    mydb = myclient[DATABASE_NAME]
    collections = [mydb[i] for i in COLLECTION_NAMES]
    monday_tweets = sum([i.find({DATE_FIELD: {SELECT_BY_REGEX: MONDAY_IN_DATE}}).count() for i in collections])
    tuesday_tweets = sum([i.find({DATE_FIELD: {SELECT_BY_REGEX: TUESDAY_IN_DATE}}).count() for i in collections])
    wednesday_tweets = sum([i.find({DATE_FIELD: {SELECT_BY_REGEX: WEDNESDAY_IN_DATE}}).count() for i in collections])
    thursday_tweets = sum([i.find({DATE_FIELD: {SELECT_BY_REGEX: TUESDAY_IN_DATE}}).count() for i in collections])
    friday_tweets = sum([i.find({DATE_FIELD: {SELECT_BY_REGEX: FRIDAY_IN_DATE}}).count() for i in collections])
    saturday_tweets = sum([i.find({DATE_FIELD: {SELECT_BY_REGEX: SATURDAY_IN_DATE}}).count() for i in collections])
    sunday_tweets = sum([i.find({DATE_FIELD: {SELECT_BY_REGEX: SUNDAY_IN_DATE}}).count() for i in collections])
    result_list = [monday_tweets, tuesday_tweets, wednesday_tweets, thursday_tweets, friday_tweets,
                   saturday_tweets, sunday_tweets]
    return RETURNED_DATA_TO_SERVER_SEPARATOR.join(str(i) for i in result_list)


@app.route(URL_FOR_RESULTS_FOR_RUSSIA_IN_TWEETS_SUFFIX, methods=[REQUEST_GET_METHOD])
def russia():
    myclient = pymongo.MongoClient(DATABASE_URL)

    mydb = myclient[DATABASE_NAME]
    word_to_search_in_tweets = RUSSIA_WORD_FOR_SEARCH_IN_TWEETS
    collections = [mydb[i] for i in COLLECTION_NAMES]
    monday_tweets = sum([i.find({DATE_FIELD: {SELECT_BY_REGEX: MONDAY_IN_DATE},
                                TEXT_FIELD: {SELECT_BY_REGEX: word_to_search_in_tweets}}).count() for i in collections])
    tuesday_tweets = sum([i.find({DATE_FIELD: {SELECT_BY_REGEX: TUESDAY_IN_DATE},
                                  TEXT_FIELD: {SELECT_BY_REGEX: word_to_search_in_tweets}}).
                         count() for i in collections])
    wednesday_tweets = sum([i.find({DATE_FIELD: {SELECT_BY_REGEX: WEDNESDAY_IN_DATE},
                                    TEXT_FIELD: {SELECT_BY_REGEX: word_to_search_in_tweets}}).
                           count() for i in collections])
    thursday_tweets = sum([i.find({DATE_FIELD: {SELECT_BY_REGEX: THURSDAY_IN_DATE},
                                   TEXT_FIELD: {SELECT_BY_REGEX: word_to_search_in_tweets}}).
                          count() for i in collections])
    friday_tweets = sum([i.find({DATE_FIELD: {SELECT_BY_REGEX: FRIDAY_IN_DATE},
                                 TEXT_FIELD: {SELECT_BY_REGEX: word_to_search_in_tweets}}).
                        count() for i in collections])
    saturday_tweets = sum([i.find({DATE_FIELD: {SELECT_BY_REGEX: SATURDAY_IN_DATE},
                                   TEXT_FIELD: {SELECT_BY_REGEX: word_to_search_in_tweets}}).
                          count() for i in collections])
    sunday_tweets = sum([i.find({DATE_FIELD: {SELECT_BY_REGEX: SUNDAY_IN_DATE},
                                 TEXT_FIELD: {SELECT_BY_REGEX: word_to_search_in_tweets}}).
                        count() for i in collections])
    result_list = [monday_tweets, tuesday_tweets, wednesday_tweets, thursday_tweets, friday_tweets,
                   saturday_tweets, sunday_tweets]
    return RETURNED_DATA_TO_SERVER_SEPARATOR.join(str(i) for i in result_list)


if __name__ == '__main__':
    app.run()
