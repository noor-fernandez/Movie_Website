#Imports the python files media and fresh_tomatoes
import media, fresh_tomatoes

iron_giant = media.Movie("The Iron Giant","A kid befriends a robot from outer space during the Cold War", #Provides instances (self) for the base class 'Movie'
                         "https://upload.wikimedia.org/wikipedia/en/d/d3/The_Iron_Giant_poster.JPG",      #with parameters from the 'Movie' __init__ function
                         "https://www.youtube.com/watch?v=fq2FZdvQXXg")                                   #There are ten movies in this file

balto = media.Movie("Balto","Wolfdog goes on an adventure to save the children of Nome, Alaska",
                    "https://upload.wikimedia.org/wikipedia/en/4/48/Balto_movie_poster.jpg",
                    "https://www.youtube.com/watch?v=sqkW0hVdFtY")

twlv_angry_men = media.Movie("12 Angry Men","Twelve white jurors decide a black boys' fate",
                             "https://upload.wikimedia.org/wikipedia/en/9/91/12_angry_men.jpg",
                             "https://www.youtube.com/watch?v=fSG38tk6TpI")

big_lebowski = media.Movie("The Big Lebowski","A californian stoner is subjected to a series of unfortunate events",
                           "https://upload.wikimedia.org/wikipedia/en/3/35/Biglebowskiposter.jpg",
                           "https://www.youtube.com/watch?v=knxhiwUspsA")


v_for_vendetta = media.Movie("V for Vendetta","A vigilante seeks to overthrow the totalitarian British government",
                             "https://upload.wikimedia.org/wikipedia/en/9/9f/Vforvendettamov.jpg",
                             "https://www.youtube.com/watch?v=lSA7mAHolAw")


copying_beethoven = media.Movie("Copying Beethoven","A female copy writer becomes an understudy to Ludwid Van Beethoven",
                                "https://upload.wikimedia.org/wikipedia/en/3/3e/CopyingbeethovenNEW.jpg",
                                "https://www.youtube.com/watch?v=ROsbGWFltU0")


ben_hur = media.Movie("Ben Hur","A jewish man overthrows the Roman Empire to rescue his wife and mother",
                      "https://upload.wikimedia.org/wikipedia/commons/7/74/Ben_hur_1959_poster.jpg",
                      "https://www.youtube.com/watch?v=NR1ZHKw09n8")


gladiator = media.Movie("Gladiator","A fallen general returns to Rome a gladiator seeking to overthrow the illegitimate Roman Emperor",
                       "https://upload.wikimedia.org/wikipedia/en/8/8d/Gladiator_ver1.jpg",
                        "https://www.youtube.com/watch?v=0BLZbrLogTo")



jungle_book = media.Movie("The Jungle Book","Mowgli goes on an adventure to escape, then defeat, Shere Khan",
                          "https://upload.wikimedia.org/wikipedia/en/a/a4/The_Jungle_Book_%282016%29.jpg",
                          "https://www.youtube.com/watch?v=HcgJRQWxKnw")

#This passes all of the movie instances into a list so the fresh_tomatoes file can read it
movie_l = [iron_giant,balto,twlv_angry_men,big_lebowski,v_for_vendetta,copying_beethoven,ben_hur,gladiator,jungle_book]

#Opens the movie webpage with the above movies
fresh_tomatoes.open_movies_page(movie_l)
