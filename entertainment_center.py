import media
import fresh_tomatoes

# Instances from the base class 'Movie' __init__ function
# Google URL shortner was used to make the URLs more manageable
# and follow PEP8 Style Guide
iron_giant = media.Movie("The Iron Giant",
                         "Boy befriends a giant robot during the Cold War",
                         "https://goo.gl/uuUvgf",
                         "https://goo.gl/4ipRly")

balto = media.Movie("Balto",
                    "Wolfdog braves the snow to save the children of Nome",
                    "https://goo.gl/u12LEZ",
                    "https://goo.gl/jYmxor")

twlv_angry_men = media.Movie("12 Angry Men",
                             "Twelve white jurors decide a black boys' fate",
                             "https://goo.gl/h4eZhW",
                             "https://goo.gl/7btrww")

big_lebowski = media.Movie("The Big Lebowski",
                           "A californian stoner is subjected to a series of unfortunate events",
                           "https://goo.gl/YCqBbd",
                           "https://goo.gl/PVKR1Q")


v_for_vendetta = media.Movie("V for Vendetta",
                             "A vigilante seeks to overthrow the totalitarian British government",
                             "https://goo.gl/ZzDwxa",
                             "https://goo.gl/QvsCKW")


copying_beethoven = media.Movie("Copying Beethoven",
                                "A female copy writer becomes an understudy to Ludwid Van Beethoven",
                                "https://goo.gl/2iVK4z",
                                "https://goo.gl/tAK5Rr")


ben_hur = media.Movie("Ben Hur",
                      "Jewish man overthrows the Roman Empire to rescue his wife and mother",
                      "https://goo.gl/QTUcWp",
                      "https://goo.gl/uSJKyc")


gladiator = media.Movie("Gladiator",
                        "Fallen general becomes a gladiator seeking to overthrow the illegitimate Caesar",
                        "https://goo.gl/JmT1Uy",
                        "https://goo.gl/9IGyCg")

jungle_book = media.Movie("The Jungle Book",
                          "Mowgli goes on an adventure to defeat Shere Khan",
                          "https://goo.gl/V0b3P7",
                          "https://goo.gl/JenB1g")

# fresh_tomatoes file reads this list and outputs a webpage
movie_l = [iron_giant, balto, twlv_angry_men, big_lebowski, v_for_vendetta,
           copying_beethoven, ben_hur, gladiator, jungle_book]

# Opens the movie webpage with the above movies
fresh_tomatoes.open_movies_page(movie_l)
