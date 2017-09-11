import media
import fresh_tomatoes

# Initialize 3 instance of Movie Class
space_oddysey_2001 = media.Movie(
    "2001: A Space Oddysey",
    "https://1.bp.blogspot.com/-RpZ1rglEeIk/T7TyEH0sEeI/AAAAAAAAEcA/O5XF3t56MY8/s1600/2001+A+Space+Odyssey+%281968%29+Space+Station+One+by+Robert+McCall.jpg",  # NOQA
    "https://www.youtube.com/watch?v=XHjIqQBsPjk"
    )

godfather = media.Movie(
    "The Godfather",
    "https://fontmeme.com/images/The-Godfather-Poster.jpg",
    "https://www.youtube.com/watch?v=sY1S34973zA&t=1s"
    )

star_wars_new_hope = media.Movie(
    "Star Wars A New Hope",
    "https://i.pinimg.com/originals/2c/a8/74/2ca8747d13f2f2ff028a80d6caf78113.jpg",  # NOQA
    "https://www.youtube.com/watch?v=vZ734NWnAHA"
    )

# Intitalize a list with 3 movies
movies = [
    space_oddysey_2001,
    godfather,
    star_wars_new_hope
    ]

# Call open_movies_page function to generate html from movies list
fresh_tomatoes.open_movies_page(movies)
