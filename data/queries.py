from data import data_manager
from psycopg2 import sql


def get_shows():
    return data_manager.execute_select('SELECT id, title FROM shows;')


def get_shows_most_rated(per_page=15, page=0):
    query = """
            SELECT
                shows.id,
                shows.title,
                EXTRACT(YEAR FROM year)::integer AS year,
                shows.runtime,
                STRING_AGG(g.name, ', ' ORDER BY g.name) genre,
                ROUND(shows.rating,1) AS rating,
                shows.trailer
            FROM shows
            INNER JOIN show_genres ON shows.id = show_genres.show_id
            INNER JOIN genres g ON g.id = show_genres.genre_id
            GROUP BY shows.id
            ORDER BY rating 
                DESC 
                LIMIT %s
                OFFSET %s
            """
    return data_manager.execute_select(query, (per_page, page))


def get_show(id):
    query = """
            SELECT DISTINCT 
                shows.id,
                shows.title,
                EXTRACT(YEAR FROM year)::integer AS year,
                shows.runtime,
                shows.overview,
                STRING_AGG(DISTINCT g.name, ', ' ORDER BY g.name) AS genre,
                STRING_AGG(DISTINCT a.name, ', ' ORDER BY a.name) AS actors,
                ROUND(shows.rating,1) as rating,
                shows.trailer
            FROM shows
            INNER JOIN show_genres ON shows.id = show_genres.show_id
            INNER JOIN genres g ON g.id = show_genres.genre_id
            INNER JOIN show_characters sc ON shows.id = sc.show_id
            INNER JOIN actors a ON a.id = sc.actor_id
            WHERE shows.id = %s
            GROUP BY shows.id
            ORDER BY shows.id
            """
    return data_manager.execute_select(query, (id,))


def get_season(show_id):
    query = """ SELECT
                    show_id,
                    season_number,
                    title,
                    overview   
                FROM seasons
                WHERE show_id = %s
                """
    return data_manager.execute_select(query, (show_id,))


def get_actors():
    query = """SELECT
                    id,
                    name,
                    birthday
                FROM actors
                ORDER BY birthday
                        LIMIT 100
                """
    return data_manager.execute_select(query)


def get_actors_shows(actor_id):
    query = """SELECT
                    title,
                    a.id,
                    a.name
                FROM shows
                JOIN show_characters sc on shows.id = sc.show_id
                JOIN actors a on a.id = sc.actor_id
                WHERE a.id = %s  
                GROUP BY a.id, a.name, title
                """
    return data_manager.execute_select(query, (actor_id,))


def get_shows_most_actors():
    query = """
            SELECT
                title,
                COUNT(actor_id) as actor_count,
                ROUND((SELECT AVG(rating) FROM shows) - rating, 2) AS rating_average
            FROM shows
            JOIN show_characters sc on shows.id = sc.show_id
            GROUP BY title, rating
            ORDER BY actor_count
                    DESC
                    LIMIT 10;
    """
    return data_manager.execute_select(query)


def get_ordered_shows(direction):
    query = sql.SQL("""
            SELECT
                shows.title,
                COUNT(e.id) AS episode_count,
                ROUND(rating, 2) AS rating
            FROM shows
            JOIN seasons s on shows.id = s.show_id
            JOIN episodes e on s.id = e.season_id
            GROUP BY shows.title, rating
            ORDER BY episode_count {dir} LIMIT 10
    """).format(dir=sql.SQL(direction))
    print(query)
    return data_manager.execute_select(query)
