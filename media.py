class Movie():
    """Movie class that provide title, image, trailer for a movie"""
    def __init__(self, title, poster_image_url, trailer_youtube_url):
        """Construct instance of movie by passing title, image url,
        and youtube url"""
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        