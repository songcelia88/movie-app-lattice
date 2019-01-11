import os
from jinja2 import StrictUndefined

from flask import Flask, render_template, redirect, request, flash, session, jsonify, json
from flask_debugtoolbar import DebugToolbarExtension
import requests


app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"
app.jinja_env.undefined = StrictUndefined
API_KEY = os.environ.get('API_KEY')
MOVIE_URL = "https://api.themoviedb.org/3"

# get the basic configuration parameters especially for the image urls
config_url = MOVIE_URL+"/configuration?api_key="+API_KEY+"butt"
config_resp = requests.get(config_url)
config = config_resp.json()

# handle case where API Key is invalid
if config_resp.status_code != 200:
    print(config_resp)
    # print(config)
    raise Exception(config['status_message'])

IMG_SIZE = 'w342'
IMG_URL = config['images']['secure_base_url'] + IMG_SIZE
PROFILE_IMG_SIZE = 'w185'
PROFILE_IMG_URL = config['images']['secure_base_url'] + PROFILE_IMG_SIZE

@app.route('/')
def homepage():
    """ Show the homepage and most popular movies today """

    payload = {
        'api_key': API_KEY,
        'page': 1
    }
    endpoint_url = MOVIE_URL + "/movie/popular"
    resp = requests.get(
        endpoint_url,
        params=payload)

    results = resp.json()
    # print(results['results'])

    return render_template("homepage.html", movies=results['results'], imgUrl=IMG_URL, searched=False)


@app.route('/search')
def search_page():
    """ Show the search results from the page """
    keyword = request.args.get('keyword')
    page = request.args.get('page')

    payload = {
        'api_key': API_KEY,
        'query': keyword,
        'page': page
    }
    endpoint_url = MOVIE_URL + "/search/movie"
    resp = requests.get(
        endpoint_url,
        params=payload
        )
    results = resp.json()
    # print(results)

    return render_template("homepage.html", movies=results['results'], 
        imgUrl=IMG_URL, searched=True, totalPages=results['total_pages'])


@app.route('/movie/<movie_id>')
def show_movie_details(movie_id):
    """ Show the details of the movie """

    # get movie details
    payload = {
        'api_key': API_KEY,
    }
    endpoint_url = MOVIE_URL + "/movie/" + movie_id
    resp = requests.get(
        endpoint_url,
        params=payload
    )
    results = resp.json()

    # get movie cast (only the top 4 cast members)
    credits_url = MOVIE_URL + "/movie/" + movie_id + "/credits"
    credits_resp = requests.get(
        credits_url,
        params=payload
    )
    credits = credits_resp.json()

    # get similar movies (only the top 4)
    similar_url = MOVIE_URL + "/movie/" + movie_id + "/similar"
    similar_resp = requests.get(
        similar_url,
        params=payload
    )
    similar = similar_resp.json()

    return render_template("movie-details.html", movie=results, 
        imgUrl=IMG_URL, profileImgUrl=PROFILE_IMG_URL, credits=credits['cast'][0:4],
        similar=similar['results'][0:4])


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = False
    app.jinja_env.auto_reload = app.debug
    
    # Use the DebugToolbar
    # DebugToolbarExtension(app)

    app.run(host='0.0.0.0')