# BookpalReccomendation
A content based recommendation system for books

You need to use python 2.7 and django 1.11. 

SET UP 
-----

First clone this repository on to your local or wherever you have to run it. 
Use the following commands on a terminal window to set it up. 

You will need to install python-pip if you haven't already. 

$ cd BookpalReccomendation/ReccomendationAPI
$ pip install -r requirements.txt

To start the django server, use the follwing command. Run it on a different
port from your primary port, obviously. I'm using port 80 here. 

$ python manage.py runserver 0.0.0.0:80

Now open up a browser and type in http://127.0.0.1:80 and you should see a page
which says "Book reccomendation system is running" 

API
---

method: GET 
url: '/reccomend'
parameters:
	id: Integer
		The bookid of the book whose similar books you wish to find


response:
	Json Response of the schema
	{"similar_books": []} # value of key 'similar_books' is an array of book ids for similar books

DATA
----

The file books.csv in ReccomendationAPI/recommender contains all the data that we used for
building the reccomendation engine. Please refer it to find the bookids for books that you're
interested in. 

MODEL
-----

A brief description of the modelling that has been done is as follows:

We started off with a plan for a collaborative filtering system, but had to settle
for content based filtering because of the lack of data. Since both parties have agreed
to build the engine based on freely available online data, we went forth with it.

A special case of pairwise cosine similarity was used to find the distance between vector
representation of books in high dimentional space. This took significant amount of time and 
resource to compute. We have not added the source code for the modelling and feature 
engineering since statistical tools that we've used are not solely based on
python. However, the model is saved as python-pickle file in the repository and can be used 
however you like. 




