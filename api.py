# Importing from Flask, jsonify, request from flask
from flask import Flask, jsonify, request

import random


# Creating a Flask app using the 'Flask' class.
app = Flask(__name__)

# Defining the '/' route below for a 'GET' request
@app.route('/jokes/<int:nums>', methods = ['GET'])
def home(nums):
	if(request.method == 'GET'):

        # Below is the list of 10 Jokes :-
		jokes = [ 
			"Why do not scientists trust atoms? Because they make up everything!",
            "What did one wall say to the other wall? I will meet you at the corner!",
            "Why do not skeletons fight each other? They do not have the guts!",
            "I used to play piano by ear, but now I use my hands.",
            "Why do not seagulls fly over the bay? Because then they would be bagels!",
            "Why did the scarecrow win an award? Because he was outstanding in his field!",
            "What do you call a snowman with a six-pack? An abdominal snowman!",
            "How do you organize a space party? You planet!",
            "Did you hear about the mathematician who is afraid of negative numbers? He will stop at nothing to avoid them!",
            "Why do not skeletons fight each other? They do not have the guts!"
	    ]
		joke = jokes[nums]
		
        # Below, we are selecting a random joke out of the 10 jokes in
        # the list above.
		# joke = jokes[random.randint(0, len(jokes)-1)]
        

    # returing a JSON Version of a Joke.
	return jsonify({'joke': joke})


if __name__ == '__main__':

	app.run(debug = True)
