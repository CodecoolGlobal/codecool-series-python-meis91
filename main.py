from flask import Flask, render_template, url_for, request, jsonify
from data import queries
from flask_paginate import Pagination
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


@app.route('/shows')
@app.route('/shows/most-rated')
def most_rated():
    page = int(request.args.get("page", 1))
    per_page = 15
    offset = (page - 1) * per_page
    total_shows = len(queries.get_shows())
    pagination_shows = get_shows_per_page(per_page=per_page, offset=offset)
    pagination = Pagination(page=page, per_page=per_page, total=total_shows,
                            css_framework="bootstrap4")
    return render_template('shows-most-rated.html', shows=pagination_shows,
                                                    page=page,
                                                    per_page=per_page,
                                                    pagination=pagination)

@app.route('/show/<id>')
@app.route('/tv-show/<id>')
def show(id):
    show = queries.get_show(id)[0]
    print(show)
    runtime = show["runtime"]
    yt_link = show["trailer"]
    if runtime / 60 > 1:
        hours = int(runtime / 60)
        min = runtime % 60
        runtime = f"{hours}h {min}"
        show["runtime"] = runtime
    if yt_link:
        yt_link = yt_link.replace("watch?v=", "embed/")
        show["trailer"] = yt_link
    seasons = queries.get_season(id)
    print(seasons)
    return render_template('show.html', show=show, seasons=seasons)


@app.route('/actors')
def get_actors():
    actors = queries.get_actors()
    return render_template('actors.html', actors=actors)


@app.route('/api/actors/show')
def get_actors_show():
    actor_id = request.args["actorId"]
    print(actor_id)
    shows = queries.get_actors_shows(actor_id)
    print(shows)
    return jsonify(shows)


@app.route('/rating')
def rating():
    return render_template('rating.html')


@app.route('/api/rating')
def get_shows_rating():
    shows = queries.get_shows_most_actors()
    return jsonify(shows)


@app.route('/ordered-shows')
def ordered_shows():
    return render_template('ordered-shows.html')


@app.route('/api/ordered-shows')
def get_ordered_shows():
    direction = request.args["direction"]
    print(direction)
    shows = queries.get_ordered_shows(direction)
    print(shows)
    return jsonify(shows)


@app.route('/design')
def design():
    return render_template('design.html')


def main():
    app.run(debug=False)


if __name__ == '__main__':
    main()
