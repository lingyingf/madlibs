"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    "awesome",
    "terrific",
    "fantastic",
    "neato",
    "fantabulous",
    "wowza",
    "oh-so-not-meh",
    "brilliant",
    "ducky",
    "coolio",
    "incredible",
    "wonderful",
    "smashing",
    "lovely",
]


@app.route("/")
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route("/hello")
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route("/greet")
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliments = [
                    "awesome",
                    "terrific",
                    "fantastic",
                    "neato",
                    "fantabulous",
                    "wowza"
                    ]   

    return render_template("compliment.html", person=player, compliments=compliments)


@app.route("/game")
def show_madlib_form():
    """get the user response on whether they like to play game or not""" 

    response = request.args.get("play_game")

    if response == "no":
        return render_template("goodbye.html")
    else:
        return render_template("game.html")



TEMPLATE = ["madlib.html", "madlib_1.html"]

@app.route("/madlib")
def show_madlib():
    """show the madlib style story"""

    color = request.args.get("color")
    noun = request.args.get("noun")
    person = request.args.get("person")
    adjective = request.args.get("adjective")
    
    random_template = choice(TEMPLATE)

    return render_template( random_template,
                            color = color,
                            noun = noun,
                            person = person,
                            adjective = adjective)


if __name__ == "__main__":
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True, host="0.0.0.0")
