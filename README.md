## How to Run this Locally (in development mode):
After setting up and activating your own local virtual environment, run the requirements.txt file with
`pip3 install -r requirements.txt`

Load the Movie DB API Key into the environment:

Create a secrets.sh file in the directory with the following line:
`export API_KEY="XXXXXXXXXXXXX"`
where the XXXXXXXX is the API Key

Run `source secrets.sh`

Run the app locally with
`python3 server.py`

Navigate to http://0.0.0.0:5000/ in your browser to view the site!

## Background
I created a movie search app that uses the Movie DB API to query for movies by title. This implementation involves using a backend (Python/Flask) to query the Movie DB API. The user can type their query
in the search field and the results will appear below. For each movie result, the poster, movie title, ratings and 
release date is shown. The results are paginated. 

Clicking on each movie will give you more details about the movie itself, including cast members and an overview of the plot.

Homepage with Most Popular movies:
![screenshot1](/static/img/homepage.png)

Search Results:
![screenshot2](/static/img/search-results.png)

Movie Details:
![screenshot3](/static/img/movie-details01.png)
![screenshot4](/static/img/movie-details02.png)

