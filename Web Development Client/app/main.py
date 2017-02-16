import random

from flask import render_template

from app import webapp

quotes = ["Wax on, wax off. Wax on, wax off.",
          "I love the smell of napalm in the morning.",
          "Hello, my name is Inigo Montoya. You killed my father. Prepare to die.",
          "He is looking at you, kid.",
          "You make me want to be a better man.",
          "Magic Mirror on the wall, who is the fairest one of all?",
          "It's alive! It's alive!",
          "You've got to ask yourself one question: 'Do I feel lucky?' Well, do ya punk?",
          "Leave the gun. Take the cannoli.",
          "There's no crying in baseball!",
          "I'll be back.",
          "This is the beginning of a beautiful friendship."
          ]


@webapp.route('/', methods=['GET'])
@webapp.route('/index', methods=['GET'])
@webapp.route('/main', methods=['GET'])
# Display an HTML page with links
def main():
    return render_template("main.html", title="Javascript, jQuery, AJAX")


@webapp.route('/movie_quote', methods=['GET', 'POST'])
def ajax_function():
    quote = quotes[random.randint(0, len(quotes) - 1)]
    return quote
