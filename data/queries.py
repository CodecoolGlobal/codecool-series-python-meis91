from data import data_manager


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
                ROUND(shows.rating,1) as rating,
                shows.trailer
            FROM shows
            INNER JOIN show_genres ON shows.id = show_genres.show_id
            INNER JOIN genres g on g.id = show_genres.genre_id
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
            INNER JOIN show_characters sc on shows.id = sc.show_id
            INNER JOIN actors a on a.id = sc.actor_id
            WHERE shows.id = %s
            GROUP BY shows.id
            ORDER BY shows.id
            """
    return data_manager.execute_select(query, (id,))

# 'SELECT id, title, year, genre, runtime, rating FROM shows ORDER BY rating DESC LIMIT 5 '