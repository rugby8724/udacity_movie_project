import fresh_tomatoes
import media


""" UP movie: movie title, movie description, movie poster, movie trailer"""
up = media.Movie(
    'UP',
    'How an old grumpy man and young ambitious boy scout'
    'conquer challenges together',
    'https://upload.wikimedia.org/wikipedia/en/0/05/Up_%282009_film%29.jpg',
    'https://www.youtube.com/watch?v=qas5lWp7_R0'
    )

""" Saving Private Ryan movie: movie title, movie description, movie poster,
    movie trailer"""
saving_private_ryan = media.Movie(
    'Saving Private Ryan',
    'Marines look to save a private that lost his brothers in the war',
    'https://upload.wikimedia.org/wikipedia/en/a/ac/Saving_Private_Ryan_poster.jpg',  # NOQA
    'https://www.youtube.com/watch?v=RYExstiQlLc'
    )

""" Office Space movie: movie title, movie description, movie poster,
    movie trailer"""
office_space = media.Movie(
    'Office Space',
    'A group of co-workers tired of the daily work grind',
    'https://upload.wikimedia.org/wikipedia/en/8/8e/Office_space_poster.jpg',
    'https://www.youtube.com/watch?v=3_fG_zLbBeU'
    )

""" Little Giants movie: movie title, movie description, movie poster,
    movie trailer"""
little_giants = media.Movie(
    'Little Giants',
    'A group of underdog kids working together against all odds',
    'https://upload.wikimedia.org/wikipedia/en/6/66/Little_giants_movie.jpg',
    'https://www.youtube.com/watch?v=MN5aY9Fq2Nk'
    )

""" Monty Python movie: movie title, movie description, movie poster,
    movie trailer"""
monty_python_and_the_holy_grail = media.Movie(
    'Monty Python and The Holy Grail',
    'British comedy of the quest for the grail',
    'https://upload.wikimedia.org/wikipedia/en/0/08/Monty-Python-1975-poster.png',  # NOQA
    'https://www.youtube.com/watch?v=urRkGvhXc8w'
    )

""" A Beautiful Mind movie: movie title, movie description, movie poster,
    movie trailer"""
a_beautiful_mind = media.Movie(
    'A Beautiful Mind',
    'American biographical drama film based on the life of John Nash',
    'https://upload.wikimedia.org/wikipedia/en/b/b8/A_Beautiful_Mind_Poster.jpg',  # NOQA
    'https://www.youtube.com/watch?v=YWwAOutgWBQ'
    )


movies = [up, saving_private_ryan, office_space, little_giants,
          monty_python_and_the_holy_grail, a_beautiful_mind]

""" fresh_tomatoes.open_movies_page takes in the list of movies
    and generates a HTML file"""

fresh_tomatoes.open_movies_page(movies)


