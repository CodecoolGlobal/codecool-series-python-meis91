from flask import Flask, render_template, url_for
from data import queries
import math
from dotenv import load_dotenv

load_dotenv()
app = Flask('codecool_series')

@app.route('/')
def index():
    shows = queries.get_shows()
    return render_template('index.html', shows=shows)


@app.route('/shows/most-rated')
def most_rated():
    shows = queries.get_shows_most_rated()
    print(shows)
    return render_template('shows-most-rated.html', shows=shows)


@app.route('/show/<id>')
def show(id):
    show = queries.get_show(id)
    print(show)
    return render_template('show.html', show=show)




@app.route('/design')
def design():
    return render_template('design.html')


def main():
    app.run(debug=False)


if __name__ == '__main__':
    main()
