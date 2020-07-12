# graph-donald-trump
A single-page project that downloads Donald Trump tweets for 2014-2020 period from [here](http://trumptwitterarchive.com/) and represents a few statistics using flask and Vue.js.

![outlook](tweets-by-year.png) ![outlook](tweets-by-day.png) ![outlook](tweets-containing-russia-by-day.png)


# Installation:

1. Install MongoDB: https://docs.mongodb.com/manual/administration/install-community/
2. Clone this repo: `$ git clone https://github.com/astoeff/graph-donald-trump-tweets.git`
3. Navigate to it: `$ cd graph-donald-trump-tweets`
4. Install pymongo: `$ pip install pymongo`
5. Install flask: `$ pip install Flask==1.0.2 Flask-Cors==3.0.7`
6. Start MongoDB database server:

- `$ sudo service mongod start` on Linux / `$ brew services start mongodb-community` on macOS

7. Open a new terminal in the same folder in order to download the tweet data and start the Flask server:

- `$ python setup.py`

- `$ python flask-crud-vue/server/app.py`

8. Open a new terminal in the same folder and build the front-end app:

- `$ cd flask-crud-vue/client`

- `$ npm install`

- `$ npm run serve`

**The statistics are visible on:**

https://localhost:8080/by-year

https://localhost:8080/by-day

https://localhost:8080/by-russia

NOTE: check the port of the client when executing the last command - it might be different than the default (8080)!