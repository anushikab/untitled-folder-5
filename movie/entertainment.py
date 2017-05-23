import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=3JnKU9Stmyw")

#print(toy_story.storyline)


avatar = media.Movie("avatar",
                     "Marine on the alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")
#print(avatar.storyline)
avatar.show_trailer()
                     

finding_nemo = media.Movie("Finding Nemo",
                           "A story of Fish (Nemo) lost in the sea and finding his way out connect with his dad again.",
                           "https://upload.wikimedia.org/wikipedia/en/2/29/Finding_Nemo.jpg",
                           "https://www.youtube.com/watch?v=wZdpNglLbt8")

movies = [Toy_story,avatar,Finding_Nemo]
fresh_tomatoes.open_movies_page(movies)
