import webbrowser

class Movie():
    def __unit__(self,movie_title, movie_storyine,poster_image,trailer_youtube):
        self.title = movie_title
        self.storyline = storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrower.open(self.trailer_youtube_url)
