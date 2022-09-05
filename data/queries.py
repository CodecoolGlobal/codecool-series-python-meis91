from data import data_manager


def get_shows():
    return data_manager.execute_select('SELECT id, title FROM shows;')


def get_shows_most_rated():
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
                LIMIT 15
            """
    return data_manager.execute_select(query)

# 'SELECT id, title, year, genre, runtime, rating FROM shows ORDER BY rating DESC LIMIT 5 '