from flask import Flask
import random as r

app = Flask(__name__)

rand_num = r.randint(0, 10)


@app.route('/')
def home_title():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/JdFEeta1hLNnO/giphy.gif">'


@app.route('/<int:num>')
def input_page(num):
    if num > rand_num:
        return f'<h1>{num} is too high! Try again</h1>' \
               f'<img src="https://media0.giphy.com/media/K1tgb1IUeBOgw/giphy.gif?cid=ecf05e47pik0xjn8v4vkb6i16ebuo2x3gvg5b4hbsq6md27n&rid=giphy.gif&ct=g">'
    elif num < rand_num:
        return f'<h1>{num} is too low! Try again</h1>' \
               f'<img src="https://media.giphy.com/media/YTETMtpsueseikztWR/giphy-downsized-large.gif">'
    else:
        return '<h1>You got it right! Congrats!</h1>' \
               '<img src="https://media.giphy.com/media/2z0OViv5TdAGs/giphy.gif">'


if __name__ == "__main__":
    app.run(debug=True)
