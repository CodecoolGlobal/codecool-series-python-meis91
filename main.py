from flask import Flask, render_template, url_for, request
from data import queries
from flask_paginate import Pagination, get_page_args
import math
from dotenv import load_dotenv

load_dotenv()
app = Flask('codecool_series')

@app.route('/')
def index():
    shows = queries.get_shows()
    return render_template('index.html', shows=shows)


def get_shows_per_page(per_page, offset):
    shows = queries.get_shows_most_rated(per_page, offset)
    return shows


@app.route('/shows/most-rated')
def most_rated():
    page = int(request.args.get("page", 1))
    per_page = 15
    offset = (page - 1) * per_page
    total_shows = len(queries.get_shows())
    pagination_shows = get_shows_per_page(per_page=per_page, offset=offset)
    pagination = Pagination(page=page, per_page=per_page, total=total_shows,
                            css_framework="bootstrap4")
    return render_template('shows-most-rated.html', shows=pagination_shows, page=page, per_page=per_page, pagination=pagination)


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
